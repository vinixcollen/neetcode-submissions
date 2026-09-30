class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

        # for i in range(m):
        #     print(nums1[i])

        #     while nums1[m] < nums1[i] and m < m+n:
        #         nums1[m]

        # for i in range(len(nums1)):
        #     for j in range(n):
        #         if nums1[i] > nums2[j]:


        

            

