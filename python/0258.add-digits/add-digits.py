class Solution:
    # 利用数据推理来计算，对于0和9进行特殊处理
    def addDigits(self, num: int) -> int:
        return num % 9 or 9 * bool(num)

    # 利用题目意思，结合 Python特性进行循环处理
    def addDigits2(self, num: int) -> int:
        while num > 9:
            num = eval('+'.join(n for n in str(num)))
        return num

