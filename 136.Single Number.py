class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_dict = {}
        for i in nums:
            try: 
                cnt_dict[i] += 1
            except:
                cnt_dict[i] = 1
        for k, v in cnt_dict.items():
            if v == 1:
                return k