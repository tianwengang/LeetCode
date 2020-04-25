from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 遍历，记录历史num，如果target - 当前num在历史nums_his中，则找到
        nums_his = dict()
        for i, num in enumerate(nums):
            ret = nums_his.get(target - num)
            if ret == None:
                nums_his[num] = i
            else:
                return [ret, i]
        assert 0


if __name__ == '__main__':
    s = Solution()

    ret = s.twoSum(nums=[2, 7, 11, 15], target=9)
    print(ret)
    assert ret == [0, 1]
