class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        #make all permutations and check that 
        # count = 0
        # for a,b,c,d in list(itertools.permutations(nums,4)):
        #     if a*b == c*d: count +=1
        hash1 = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                hash1[nums[i] * nums[j]] = hash1.get(nums[i] * nums[j], 0) +1
        count = 0
        for i in hash1.values():
            count += math.comb(i,2) *8
        return count




# class Solution(object):
#     def tupleSameProduct(self, nums):
#         nums_length = len(nums)

#         # Initialize a dictionary to store the frequency of each product of pairs
#         pair_products_frequency = {}

#         total_number_of_tuples = 0

#         # Iterate through each pair of numbers in `nums`
#         for first_index in range(nums_length):
#             for second_index in range(first_index + 1, nums_length):
#                 # Increment the frequency of the product of the current pair
#                 product_value = nums[first_index] * nums[second_index]
#                 if product_value in pair_products_frequency:
#                     pair_products_frequency[product_value] += 1
#                 else:
#                     pair_products_frequency[product_value] = 1

#         # Iterate through each product value and its frequency in the dictionary
#         for product_frequency in pair_products_frequency.values():
#             # Calculate the number of ways to choose two pairs with the same product
#             pairs_of_equal_product = (
#                 (product_frequency - 1) * product_frequency // 2
#             )

#             # Add the number of tuples for this product to the total (each pair
#             # can form 8 tuples)
#             total_number_of_tuples += 8 * pairs_of_equal_product

#         return total_number_of_tuples
# # class Solution:
# #     def tupleSameProduct(self, nums: List[int]) -> int:
# #         nums_length = len(nums)
# #         nums.sort()

# #         total_number_of_tuples = 0

# #         # Iterate over all possible values for 'a'
# #         for a_index in range(nums_length):
# #             # Iterate over all possible values for 'b', starting from the end
# #             # of the list
# #             for b_index in range(nums_length - 1, a_index, -1):
# #                 product = nums[a_index] * nums[b_index]

# #                 # Use a set to store possible values of 'd'
# #                 possible_d_values = set()

# #                 # Iterate over all possible values for 'c' between 'a' and 'b'
# #                 for c_index in range(a_index + 1, b_index):
# #                     # Check if the product is divisible by nums[c_index]
# #                     if product % nums[c_index] == 0:
# #                         d_value = product // nums[c_index]

# #                         # If 'd_value' is in the set, increment the tuple count
# #                         # by 8
# #                         if d_value in possible_d_values:
# #                             total_number_of_tuples += 8

# #                         # Add nums[c_index] to the set for future checks
# #                         possible_d_values.add(nums[c_index])

        # return total_number_of_tuples

