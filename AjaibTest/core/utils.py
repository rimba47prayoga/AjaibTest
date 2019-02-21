from typing import List, Tuple, Dict
from django.db import connection
from django.db.backends.utils import CursorDebugWrapper


class AjaibTests:

    def __init__(self):
        self.__tree_result = []

    #  --- common function/method class

    @staticmethod
    def sort_array(arr: List) -> List:
        """
        :param arr: Array
        :return: new sorted array
        """
        arr = arr.copy()  # don't change original array
        len_arr = len(arr)
        for index in range(len_arr):
            for j in range(index + 1, len_arr):
                if arr[index] > arr[j]:
                    arr[index], arr[j] = arr[j], arr[index]
        return arr

    def remove_duplicates_array(self, array: List) -> List:
        """
        remove duplicates value in array without change ordering.
        :param array: Array
        :return:
        """
        seen = set()
        seen_add = seen.add
        return [x for x in array if not (x in seen or seen_add(x))]

    def dictfetchall(self, cursor: CursorDebugWrapper) -> List[Dict]:
        """
        :param cursor:
        :return: all rows from a cursor as a dict
        """
        fetchall = cursor.fetchall()
        if fetchall == ():
            return []  # don't loop if no result
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in fetchall
        ]

    # --- end

    def max_diff(self, arr: List) -> int:
        """
        :param arr: Array
        :return: element / number that maximum diff
        """
        result = None
        diff = None
        for index, number in enumerate(arr):
            try:
                if diff is None:
                    diff = number - arr[index + 1]
                    result = number
                else:
                    _diff = (number - arr[index + 1])
                    if diff < _diff:
                        diff = _diff
                        result = number
            except IndexError:
                pass
        return result

    def merge_sorted_arrays(self, *args: Tuple[List]) -> List:
        """
        :param args: Arrays (can multiple or more).
        :return: new sorted arrays.
        """
        arrays = []
        for arr in args:
            arrays += arr
        return self.sort_array(arrays)

    def print_tree(self, which=None) -> None:
        tree = [
            {
                "A": "B"
            },
            {
                "A": "C"
            },
            {
                "C": "D"
            },
            {
                "A": "E"
            }
        ]
        if which is None:
            which = input("Select the path that will be printed: ")
        try:
            child = list(filter(lambda x: which in list(x.values()), tree))[0]
            next_path = None
            for key, value in child.items():
                self.__tree_result.insert(0, value)
                self.__tree_result.insert(0, key)
                next_path = key

            assert next_path is not None
            return self.print_tree(which=next_path)
        except IndexError:
            if not self.__tree_result:
                raise ValueError("'%s' does not exist in tree node" % which)
        res = self.remove_duplicates_array(self.__tree_result.copy())
        res = " -> ".join(res)
        self.__tree_result.clear()  # make sure to clear result after it.
        print(res)

    def transaction_balance(self) -> List[Dict]:
        query = """
        SELECT id, amount, (
            SELECT SUM(amount) FROM transaction_balance as temp
            WHERE trx.id >= temp.id
        ) as total FROM transaction_balance as trx
        """
        cursor = connection.cursor()
        cursor.execute(query)
        return self.dictfetchall(cursor=cursor)


"""
INSTRUCTIONS.

The Usage is Simple. ->
run.
`python manage.py shell`

`from core.utils import AjaibTests`

`test = AjaibTests()`

`test.max_diff([4, 2, 1, 5])`

etc .. .

for API endpoints.
localhost:8000/api/v1/user
"""
