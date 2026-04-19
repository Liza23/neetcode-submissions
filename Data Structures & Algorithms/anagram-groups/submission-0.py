class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = []
        group_tag = [0 for i in range(len(strs))]
        group_list = []

        for i in range(len(strs)):
            s_dict = {}
            for char in strs[i]:
                if char not in s_dict.keys():
                    s_dict[char] = 0
                s_dict[char] += 1
            
            existing_group = False
            for j in range(len(dict_list)):
                if s_dict == dict_list[j]:
                    existing_group = True
                    group_tag[i] = j
                    group_list[j].append(strs[i])
            if not existing_group:
                dict_list.append(s_dict)
                group_tag[i] = len(dict_list)
                group_list.append([])
                group_list[len(dict_list) - 1].append(strs[i])
        return group_list
