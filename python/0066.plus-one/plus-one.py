class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        carry = 0
        while index >= 0:
            carry = 1 if digits[index] == 9 else 0
            if carry == 1:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits