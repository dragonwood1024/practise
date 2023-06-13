#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        numbers = [1]
        next_numbers = [i for i in primes]
        index = [0] * len(primes)
        while len(numbers) < n:
            next_number = min(next_numbers)
            numbers.append(next_number)
            for i in range(len(primes)):
                if next_number == next_numbers[i]:
                    index[i] += 1
                    next_numbers[i] = primes[i] * numbers[index[i]]
        return numbers[-1]

        
# @lc code=end

