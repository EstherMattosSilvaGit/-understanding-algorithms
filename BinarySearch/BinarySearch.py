from typing import List

class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs binary search on a sorted list to find the index of the target.

        Args:
            nums (List[int]): A sorted list of integers in ascending order.
            target (int): The target value to search for in the list.

        Returns:
            int: The index of the target in the list if found, otherwise -1.
        """
        inicio = 0
        fim = len(nums) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            n = nums[meio]
            if n == target:
                return meio
            elif n > target:
                fim = meio - 1
            elif n < target:
                inicio = meio + 1
        return -1


        