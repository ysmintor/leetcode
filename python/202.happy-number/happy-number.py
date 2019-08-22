class Solution:
    # 方法一 使用一个集合了记录新产生的元素，重复时退出并检查是否为1进行判断
    def isHappy(self, n: int) -> bool:
        coll_set = set()

        while n != 1 :
            sum = 0
            while n != 0 :
                sum += (n % 10) ** 2
                n //=10
            # replace sum to n
            n = sum
            if n in coll_set:
                break
            coll_set.add(n)
        return n == 1

    # 方法二 重复时必然会含有4，证明过程可在网络上查询
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4 :
            sum = 0
            while n != 0 :
                sum += (n % 10) ** 2
                n //=10
            # replace sum to n
            n = sum
        return n == 1