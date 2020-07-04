'''Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]'''

class elements:
 def Sum(self, num):
        num, result, i = sorted(num), [], 0
        while i < len(num) - 2:
            j, k = i + 1, len(num) - 1
            while j < k:
                if num[i] + num[j] + num[k] < 0:
                    j += 1
                elif num[i] + num[j] + num[k] > 0:
                    k -= 1
                else:
                    result.append([num[i], num[j], num[k]])
                    j, k = j + 1, k - 1
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
            i += 1
            while i < len(num) - 2 and num[i] == num[i - 1]:
                i += 1
        return result

print(elements().Sum([-25, -10, -7, -3, 2, 4, 8, 10]))
