# 2 cases if even add 2 middle, odd return middle
# even:
# 2 pointer iterate through left and right depedning which is bigger until you reach middle//2
#   odd:
#   iterate once with for loop  if l is greater than len nums1 add to r and vice versa
#  if l and r less than then you add the largest one .


# 1 2 3 4 5 6


# 2 pointer iterate through left and right depedning which is bigger until you reach middle//2. then have leftVal = that and rightVal = next largest
# return right+left / 2


# {2  4  8  14}}

# { 3 5 7} 11 12 }
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> len(nums2): 
            nums1,nums2= nums2,nums1
        n1,n2 = len(nums1), len(nums2)

        tot  = n1+ n2
        half = (tot+1) //2
        l,r = 0, len(nums1)
        while l <= r:
            m1 = (l+r)//2
            m2 = half-m1

            l1, l2 = nums1[m1 - 1] if m1>0 else float('-inf'),  nums2[m2 - 1] if m2>0 else float('-inf')
            r1, r2 = nums1[m1] if m1< n1 else float('inf'),  nums2[m2] if m2 < n2 else float('inf')


            if l1 <= r2 and l2<= r1:
                if tot %2 ==1: return max(l1,l2)
                else: return (max(l1,l2) + min(r1,r2)) /2
            
            elif l1 >r2:
                r = m1-1
            else:
                l= m1 +1


        return 0
#         6

#         if tot&1 

# # 5,7}

# # 4},8,12


# # 7 8




# # 1 }3 5

# # 2 4 }6

# # 1,2,4
# # 4

# # 3,5,6
# # 3


# # 13}5 2}46

# # 1 2 }5 

# # 3} 4 6

# # 3 <= 4: return this /2

# # []

# # [1,2,3] | [4,5]


# # L = 3 r = 4. this is odd. so return left. = 3







        len1, len2 = len(nums1), len(nums2)
        i = j = median1 = median2 = 0
        for count in range(((len1 + len2) // 2) + 1):
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
        if (len1 + len2) % 2 == 0:
            return float((median1 + median2) / 2.0)
        else:
            return float(median1)

    # totalLength = len(nums1) + len(nums2)
    # l,r = 0,0
    # if totalLength %2 == 0:
    #     currCount = 0
    #     while r and l and currCount != (totalLength//2) +1:
    #         currCount +=1
    #         if nums1[l] > nums2[r]:
    #             if currCount == (totalLength//2): firstAdd =
    #             r+=1
    #         else:
    #             l+=1
    # else:
    #     currCount = 0
    #     while r and l and currCount != (totalLength//2) +1:
    #         currCount +=1
    #         if nums1[l] > nums2[r]:
    #             if currCount == (totalLength//2): firstAdd =
    #             r+=1
    #         else:
    #             l+=1

    # for

    # def binary search(nums,target):
    #     midVal = nums[len(nums)//2]
    #     first = False
    #     l,r = 0, len(nums)-1
    #     while l <= r:
    #         midVal = l+r//2
    #         if target == nums[midVal]:
    #             first = True
    #             return midVal
    #         if target > nums[midVal]:
    #             l = midVal+1
    #         else:
    #             r = midVal -1
    #     return midVal if first  else -1

    # #
