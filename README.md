# coding just for fun #
前阵公司搞可信认证考试，才开始关注LeetCode，以前听过但没想过进来练练。

一线编码很多年了，一直做业务，很少练习提升，考前利用周末练了几道题，找到一些感觉，然后一次性通过了专业级的认证，咱们团队近十人一起考竟然就我一个过了。。

工作以来编程语言主要是c和c++，略懂python，打算用python不定期刷题，coding just for fun，顺便提升python水平。

# 刷题经验总结持续更新 #

## 参数校验 ##

typing包用于增加入参校验，python代码太灵活，带来的缺点是需要注释去明确入参类型。

但最好的注释是自注释，所以通过下面的方式限制入参、返回值的类型

`from typing import List`

`twoSum(self, nums: List[int], target: int) -> List[int]`

## 重载 ##

### 构造函数重载 ###
`def __init__(self, x):`

当参数个数相同时，python按类型重载可以在构造函数中判断入参类型，用内置的isinstance进行判断，如：

`isinstance(a,int)`

`isinstance(a,(str,int,list))`
### 打印函数重载 ###
    def __str__(self):
        ret = []
        cur = self
        while cur != None:
            ret.append(cur.val)
            cur = cur.next
        return str(ret)
        
### 等于运算符重载(不等于运算符也走这个逻辑) ###
    def __eq__(self, other):
        if other == None:
            return False

        cur_self = self
        cur_other = other
        while cur_self != None and other != None:
            if cur_self.val != cur_other.val:
                return False
            cur_self = cur_self.next
            cur_other = cur_other.next

        if cur_self != None or cur_other != None:
            return False
        return True
        
# 编程思维总结 #
### 不盲目追求性能，在性能满足需求的前提下，可读性压倒一切 ###