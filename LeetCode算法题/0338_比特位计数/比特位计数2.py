class Solution:
    def countBits(self, num: int):
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits
