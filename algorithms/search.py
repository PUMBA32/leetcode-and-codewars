from typing import List, Any


class Search:
    @staticmethod
    def linear_search(arr: List[Any], el: Any) -> int:
        for i, k in enumerate(arr): 
            if k == el: return i
        return -1

    @staticmethod
    def binary_search(arr: List[Any], el: Any) -> int: ... 