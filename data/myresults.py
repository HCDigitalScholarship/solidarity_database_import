from __future__ import unicode_literals

from collections import OrderedDict

from tablib import Dataset

from import_export.results import Error, RowResult



class myResult(object):
    def __init__(self, *args, **kwargs):
        super(myResult, self).__init__()
        self.base_errors = []
        self.diff_headers = []
        self.rows = []  # RowResults
        self.failed_dataset = Dataset()
        self.totals = OrderedDict([(RowResult.IMPORT_TYPE_NEW, 0),
                                   (RowResult.IMPORT_TYPE_UPDATE, 0),
                                   (RowResult.IMPORT_TYPE_DELETE, 0),
                                   (RowResult.IMPORT_TYPE_SKIP, 0),
                                   (RowResult.IMPORT_TYPE_ERROR, 0)])
        self.total_rows = 0
        '''the rest properties are customized'''
        self.deleted_rows = []
        self.deleted_rows_count = 0

    def append_row_result(self, row_result):
        self.rows.append(row_result)

    def append_base_error(self, error):
        self.base_errors.append(error)

    def add_dataset_headers(self, headers):
        self.failed_dataset.headers = headers + ["Error"]

    def append_failed_row(self, row, error):
        row_values = [v for (k, v) in row.items()]
        row_values.append(str(error.error))
        self.failed_dataset.append(row_values)

    def increment_row_result_total(self, row_result):
        if row_result.import_type:
            self.totals[row_result.import_type] += 1

    def row_errors(self):
        return [(i + 1, row.errors)
                for i, row in enumerate(self.rows) if row.errors]

    def has_errors(self):
        return bool(self.base_errors or self.row_errors())

    def __iter__(self):
        return iter(self.rows)
