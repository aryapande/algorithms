class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = []
        def create(arr):#initial array will be []
            
            if(len(arr)==len(nums)):
                m.append(arr)
                return
            for x in nums:
                if(x not in arr):
                    p = arr[:]
                    p.append(x)
                    create(p)
        create([])
        print(m)
        return m
