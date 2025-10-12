# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         count = 0
#         original = x
#         reverse = 0

#         if x == 0:
#             return True
        
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False

#         while x > reverse:
#                 remainder = x % 10
#                 reverse = reverse * 10 + remainder
#                 x //= 10

#         return x == reverse or x == reverse // 10


# if __name__ == "__main__":
    
#     input = 1234
#     Solution.isPalindrome(self=None,x=input)



# class Solution(object):
#     def romanToInt(self, s):
#         roman_map = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50,
#             'C': 100, 'D': 500, 'M': 1000,
#             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
#             'CD': 400, 'CM': 900
#         }
#         i = 0
#         number = 0
#         while i < len(s):
#             if i + 1 < len(s) and s[i:i+2] in roman_map:
#                 number += roman_map[s[i:i+2]]
#                 i += 2
#             else:
#                 number += roman_map[s[i]]
#                 i += 1
#         return number

# if __name__ == "__main__":
#     string = "MCMXCIV"
#     print(Solution().romanToInt(string))



# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
        
#         prefix = strs[0]
#         for string in strs[1:]:
#             # print(f"Current prefix: {prefix}, comparing with: {string}")
#             # print("string",string[0:2])÷
#             while not string.startswith(prefix):
#                 prefix = prefix[:-1]
#                 print(f"Updated prefix: {prefix}")
#                 if not prefix:
#                     return ""
#                 # print(string[:len(prefix)] == prefix[:len(string)])
        
#         return prefix

# if __name__ == "__main__":
#     input = ["flower", "flow", "flight"]
#     print(Solution().longestCommonPrefix(input))

# import numpy as np
# class Solution(object):
#     def maxTotalFruits(self, fruits, startPos, k):
#         """
#         :type fruits: List[List[int]]
#         :type startPos: int
#         :type k: int
#         :rtype: int
#         """
#         harvested_fruit = []
#         total_fruits = 0
        
#         for i in range(0,np.size(fruits, 0)):
#             if startPos == fruits[i][0]:
#                     harvested_fruit.append(fruits[i][1])
#                     startPos = fruits[i][0]
#                     print(f"Harvested {harvested_fruit} fruits from position {startPos}.")
        
#         while k > 0 and i < np.size(fruits, 0):
#             if fruits[i][0] < startPos - k or fruits[i][0] > startPos + k:
#                 i += 1
#                 continue

#             first_min_dis = min(fruits[i][0], startPos - k, startPos + k)

#             if  abs(startPos - k ) == abs(startPos + k):
#                 if fruites[i][0] == startPos - k or fruits[i][0] == startPos + k:
#                     harvested_fruit.append(fruits[i][1])
#                     startPos = fruits[i][0]
#                     k -= abs(startPos - fruits[i][0])
#             else:
#                 k -= first_min_dis
#                 harvested_fruit.append(fruits[i][1])
#                 startPos = fruits[i][0]
#                 i += 1  
       
            
#         total_fruits = sum(harvested_fruit)
#         print(f"Total fruits harvested: {total_fruits}")
#         return total_fruits






# if __name__ == "__main__":
#     fruits = [[2, 3], [4, 5], [6, 7]]
#     startPos = 4
#     k = 3
#     print(Solution().maxTotalFruits(fruits, startPos, k))


# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """

        
#         if numRows == 0:
#             return []
#         if numRows == 1:
#             return [[1]]
#         if numRows == 2:
#             return [[1], [1, 1]]

#         triangle = [[1] * (i + 1) for i in range(numRows)]
#         for i in range(2, numRows):
#             for j in range(1, i):
#                 triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         return triangle


# if __name__ == "__main__":
#     numRows = 5
    
#     print(Solution().generate(numRows))


# class Solution(object):
#     def countHillValley(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         if len(nums) < 3:
#             return 0

#         nums = [nums[i] for i in range(len(nums)) if i==0 or nums[i] != nums[i-1]]

#         for i in range(1, len(nums) - 1):
#                 if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
#                     count += 1
#                 elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
#                     count += 1
               
#         return count



# if __name__ == "__main__":
#     nums =[25,67,67,83,27,27,50,13,50,27,41,16,17,29,51,57,44,87,3,75,20,8,92,83,72,85,80,50,7,52,64,69,15,68,84,98,66,17,47,41,87,55,44,22,19,90,72,8,93,15,9,25,43,17,50,33,100,2,94,64,18,34,19,52,31,75,28,29,84,67,16,89,61,47,29,96,48]
#     print(Solution().countHillValley(nums))

# class Solution(object):
#     def countMaxOrSubsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         max_or = 0
#         n = len(nums)           
#         for i in range(1 << n):
#             current_or = 0
#             for j in range(n):
#                 if i & (1 << j):
#                     current_or |= nums[j]
#             if current_or > max_or:
#                 max_or = current_or
#                 count = 1
#             elif current_or == max_or:
#                 count += 1

#         return count    
# if __name__ == "__main__":
#     nums = [3, 1]
#     print(Solution().countMaxOrSubsets(nums))


# class Solution(object):
#     def maxSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_sum = 0
#         n = len(nums)
        
#         for i in range(n):
#             for j in range(i + 1, n):
#                 current_sum = nums[i] + nums[j]
#                 if current_sum > max_sum:
#                     max_sum = current_sum
        
#         return max_sum

# if __name__ == "__main__":  
#     nums = [2,7]
#     print(Solution().maxSum(nums))

# import asyncio

# async def fetch_data(n):
#     await asyncio.sleep(5)  # simulate network delay
#     print(f"Fetched {n}")

# async def main():
#     await asyncio.gather(fetch_data(1), fetch_data(2), fetch_data(3))

# asyncio.run(main())


# async function fetchData() {
#   try {
#     const response = await fetch('https://api.example.com/data'); // Pauses until fetch Promise resolves
#     if (!response.ok) {
#       throw new Error(`HTTP error! status: ${response.status}`);
#     }
#     const data = await response.json(); // Pauses until json parsing Promise resolves
#     console.log(data);
#   } catch (error) {
#     console.error('Error fetching data:', error);
#   }
# }

# fetchData();

# import threading, time
# semaphore = threading.Semaphore(2)  # allow 2 threads at a time

# def task(name):
#     with semaphore:
#         print(f"{name} started")
#         time.sleep(1)
#         print(f"{name} finished")

# for i in range(5):
#     threading.Thread(target=task, args=(f"Task-{i}",)).start()


# "id" : "1234567890",
# "name" : "John Doe",  
# "email" : "
#

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s

#         start, end = 0, 0
#         for i in range(n):
#             len1 = self.expandAroundCenter(s, i, i)
#             len2 = self.expandAroundCenter(s, i, i + 1)
#             max_len = max(len1, len2)
#             if max_len > end - start:
#                 start = i - (max_len - 1) // 2
#                 end = i + max_len // 2

#         return s[start:end+1]       
    
#     def expandAroundCenter(self, s: str, left: int, right: int) -> int:
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return right - left - 1 # length of the palindrome      
# if __name__ == "__main__":
#     input = "babad"
#     print(Solution().longestPalindrome(input))  
#**************************************************************
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         updated_num = []
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 updated_num.append(nums[i])
#                 updated_num.sort()
#         nums[:] = updated_num
#         return len(nums)
    
#**************************************************************
#    
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left, right = 0, len(height) - 1
#         max_area = 0

#         while left < right:
#             width = right - left
#             current_height = min(height[left], height[right])
#             current_area = width * current_height
#             max_area = max(max_area, current_area)

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1

#         return max_area

##################################################################
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # result = []
        # for i in range(len(nums) - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     left, right = i + 1, len(nums) - 1
        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]
        #         if total < 0:
        #             left += 1
        #         elif total > 0:
        #             right -= 1
        #         else:
        #             result.append([nums[i], nums[left], nums[right]])
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left += 1
        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -= 1
        #             left += 1
        #             right -= 1
        # return result   
###################################################################
# class Solution:
#     def threeSumClosest(self, nums: list[int], target: int) -> int:
#         nums.sort()
#         print(nums)
#         result =[]
#         diff=[]
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             print("nums",nums[i],nums[i+1],nums[i+2])
#             temp = nums[i] + nums[i+1] +nums[i+2]
#             print("temp",temp)
#             diff.append(abs(temp - target))
#             if min(diff)== 0:
#                 return nums[i] + nums[i+1] + nums[i+2]
#             result = nums[diff.index(min(diff))] + nums[diff.index(min(diff))+1] + nums[diff.index(min(diff))+2]
#             print("diff:",diff)
#             print(nums[diff.index(min(diff))] , nums[diff.index(min(diff))+1] , nums[diff.index(min(diff))+2])

#         if result == []:
#             result = nums[0] + nums[1] + nums[2]
#         print("result",result)

#         return result 
    
# if __name__ == "__main__":
#     # input = [10,20,30,40,50,60,70,80,90]
#     # input = [-1,2,1,-4]
#     input = [4,0,5,-5,3,3,0,-4,-5]
#     target = -2
#     print(Solution().threeSumClosest(input,target))


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        final = []
        result = ""
        count = 1
        final = self.countAndSay(n - 1)

        for i in range(1, len(final)):
            if final[i] == final[i - 1]:
                count += 1
            else:
                result += str(count) + final[i - 1]
                count = 1
        result += str(count) + final[-1]
        return result

if __name__ == "__main__":
    n = 10
    print(Solution().countAndSay(n))
