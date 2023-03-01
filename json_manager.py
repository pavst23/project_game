import json
import os

from configs import ResultsFileConfig


class JSONResults(object):

    _results_filename = ResultsFileConfig.FILENAME

    def __init__(self):
        if not os.path.exists(self._results_filename):
            with open(self._results_filename, "x") as _:
                json.dump({"Noname": 0}, _)

    def save_result(self, data: dict, rewrite_flag=False):
        if rewrite_flag:
            self.clear_results()
        if os.path.exists(self._results_filename):
            filemode = "w"
        else:
            filemode = "x"
        with open(self._results_filename, filemode) as result_file:
            json.dump(data, result_file)

    def get_results(self):
        with open(self._results_filename) as result_file:
            return json.load(result_file)

    def clear_results(self):
        os.remove(self._results_filename)
