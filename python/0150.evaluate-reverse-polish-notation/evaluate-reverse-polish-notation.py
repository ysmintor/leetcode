class Solution:
    # 利用字典和 lambda 表达式计算结果
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        compute = {
            '+': lambda op1, op2: op1 + op2,
            '-': lambda op1, op2: op1 - op2,
            '*': lambda op1, op2: op1 * op2,
            '/': lambda op1, op2: int(op1 / op2)
        }

        for num in tokens:
            if num in compute:
                op2 = stack.pop()
                op1 = stack.pop()
                tmp = compute[num](int(op1), int(op2))
                stack.append(str(tmp))
            else:
                stack.append(num)
        return stack[-1]
    # 使用 eval 直接计算表达式
    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num in ['+', '-', '*', '/']:
                b, a = stack.pop(), stack.pop()
                stack.append(str(int(eval(a+num+b))))
            else:
                stack.append(num)
        return stack[-1]