from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_missing_values = {}
        for i in range(len(nums)):
            potential_first_num = target - nums[i]
            if prev_missing_values and nums[i] in prev_missing_values.keys():
                return [prev_missing_values[nums[i]], i]
            else:
                prev_missing_values[potential_first_num] = i

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums) - 1):
    #         potential_second_num = target - nums[i]
    #         try:
    #             second_num_index = nums[i + 1:].index(potential_second_num)+i+1
    #             return [i, second_num_index]
    #         except:
    #             pass

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     potential_first_nums = []
    #     for i in range(len(nums)):
    #         if len(potential_first_nums)>0:
    #             try:
    #                 first_num_index = potential_first_nums.index(nums[i])
    #                 return [first_num_index, i]
    #             except:
    #                 potential_first_nums.append(target-nums[i])
    #         else:
    #             potential_first_nums.append(target - nums[i])

# Как сократить время выполнения?
# ИСПОЛЬЗОВАТЬ dict ВМЕСТО list!
# Вместо суммирования каждого числа, отнять от таргета первое число и проверить есть ли это число в списке
# Каждое последующее число суммируется только с элементами списка после себя - не нужно, проверка идет по предыдущим числам
# Убрать дубли (проверив не суммируются ли они в таргет) - бессмысленно, добавляет цикл лишний