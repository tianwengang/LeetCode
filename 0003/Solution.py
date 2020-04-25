from typing import List

# 注意提交时要import这个包
import queue


# 本人编程思维：不追求性能，在性能满足产品需求的条件前提下，可读性大于一切
# 本题没有要求性能，就以好理解的思路来作答
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 例如pwwkew，容器依次存储p0,w1,w2
        # 发现w2重复，移除在w2的位置2以前的元素，容器存放的就是<w2>
        his_queue = queue.Queue()
        his_set = set()
        max_len = 0

        for c in s:
            if c not in his_set:
                his_set.add(c)
                his_queue.put(c)
                continue

            max_len = max(max_len, his_queue.qsize())
            while not his_queue.empty():
                top = his_queue.get()
                his_set.remove(top)

                if top == c:
                    break

            his_set.add(c)
            his_queue.put(c)

        return max(max_len, his_queue.qsize())


if __name__ == '__main__':
    s = Solution()

    ret = s.lengthOfLongestSubstring("abcabcbb")
    print(ret)
    assert ret == 3

    ret = s.lengthOfLongestSubstring("bbbbb")
    print(ret)
    assert ret == 1

    ret = s.lengthOfLongestSubstring("pwwkew")
    print(ret)
    assert ret == 3
