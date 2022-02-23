# alist= []
# i=0
# j=1
# alist.append(i)
# alist.append(j)
# print(alist)
# print(len(alist))
# class Solution:
#     def __init__(self, nums, target):
#         self.nums = nums
#         self.target = target
#     def twoSum(self):
#         result = []
#         length = len(self.nums)
#         i = 0
#         while i <= length - 1:
#             if self.nums.index(self.target - self.nums[i]):
#                 result.append(i)
#                 result.append(self.nums.index(self.target - self.nums[i]))
#                 return result
#             i += 1
        # result = []
        # length = len(self.nums)
        # i=0
        # while i<=length-2:
        #     j=i+1
        #     while j<=length-1:
        #         if self.nums[i]+ self.nums[j] == self.target:
        #             result.append(i)
        #             result.append(j)
        #             return result
        #         j+=1
        #     i+=1

class Solution:
    def __init__(self, s, numRows):
        self.s = s
        self.numRows = numRows
    def convert(self):
        s=self.s
        numRows=self.numRows
        global i
        i = 0
        global column
        column = 0
        row = -1
        global resultMatrix
        resultMatrix = {}
        resultStr = ''
        if self.numRows < 2:
            return s
        while i < len(s):
            while row < numRows-1:
                if i >= len(s):
                    break
                else:
                    row += 1
                    coordinate = (row, column)
                    dict2 = {coordinate: s[i]}
                    resultMatrix.update(dict2)
                    i += 1
                    del coordinate
            while row > 0:
                if i >= len(s):
                    break
                else:
                    column += 1
                    row -= 1
                    coordinate = (row, column)
                    dict2 = {coordinate: s[i]}
                    resultMatrix.update(dict2)
                    i += 1
                    del coordinate

        print("resultMatrix:", resultMatrix)
        k=0
        j=0
        while k < numRows:
            while j < column+1:
                if (k, j) in resultMatrix:
                    resultStr += resultMatrix[(k, j)]
                j += 1
            k += 1
            j=0
        return resultStr
solution = Solution("AB",1)
print(solution.convert())