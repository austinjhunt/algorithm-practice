"""Leetcode: Find the median of two sorted arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=problem-list-v2&envId=binary-search

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    def findMedianSortedArraysWithMerge(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # O(m+n) because of merge iteration over m + n elements
        full = self.merge(nums1, nums2)
        print(f"Merged: {full}")
        if len(full) % 2 == 0:
            middletwo = len(full) // 2
            middleone = middletwo - 1
            median = (full[middletwo] + full[middleone]) / 2
        else:
            middle = len(full) // 2
            median = full[middle]

        return median

    def get_median(self, a):
        if len(a) == 0:
            return None
        if len(a) % 2 == 0:
            m1, m2 = a[len(a) // 2 - 1], a[len(a) // 2]
            return (m1 + m2) / 2
        return a[len(a) // 2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return None
        elif len(nums1) == 0:
            return self.get_median(nums2)
        elif len(nums2) == 0:
            return self.get_median(nums1)
        # Do not need to merge sorted arrays. Arrays are sorted so min is either first
        # in nums1 or first in nums2.
        m, n = len(nums1), len(nums2)

        # Index pointers for nums1 and nums2 to help identify global min.
        p1, p2 = 0, 0

        # Get the smaller value between nums1[p1] and nums2[p2].
        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        # If m + n is even, repeat step 3 by (m + n) / 2 + 1 times
        # and return the average of the elements from the last two steps.
        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            # If m + n is odd, repeat step 3 by (m + n + 1) / 2 times and
            # return the element from the last step (global middle element)
            for _ in range((m + n) // 2):
                _ = get_min()
            return get_min()

    def merge(self, a, b):
        # implement merge sort's merge method
        out = []
        while len(a) > 0 and len(b) > 0:
            if a[0] <= b[0]:
                out.append(a.pop(0))
            else:
                out.append(b.pop(0))
        # either a or b is empty
        while len(a) > 0:
            out.append(a.pop(0))
        while len(b) > 0:
            out.append(b.pop(0))
        return out
