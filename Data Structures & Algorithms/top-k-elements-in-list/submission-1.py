class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 0
            num_dict[num] += 1
        
        reverse_dict = {}
        freq_arr = []
        for num in num_dict.keys():
            freq = num_dict[num]
            freq_arr.append(freq)
            if freq not in reverse_dict.keys():
                reverse_dict[freq] = []
            reverse_dict[freq].append(num)
        
        freq_arr = list(set(freq_arr))
        freq_arr.sort(reverse=True)

        ans = []
        for k_ in range(k):
            topk = reverse_dict[freq_arr[k_]]
            for i in range(len(topk)):
                ans.append(topk[i])
                if len(ans) == k:
                    return ans
        return ans