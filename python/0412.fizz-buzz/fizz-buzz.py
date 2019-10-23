class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            flag1 = i % 3 == 0
            flag2 = i % 5 == 0
            if flag1 and flag2 :
                res.append('FizzBuzz')
            elif flag1:
                res.append('Fizz')
            elif flag2:
                res.append('Buzz')
            else:
                res.append(str(i))

        return res