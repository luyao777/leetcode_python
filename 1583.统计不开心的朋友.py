#
# @lc app=leetcode.cn id=1583 lang=python3
#
# [1583] 统计不开心的朋友
#

# @lc code=start
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pair_dict = {}
        for pair in pairs:
            pair_dict[pair[0]] = pair[1]
            pair_dict[pair[1]] = pair[0]
        
        unhappy_num = 0
        unhappy_set = set()

        for pair in pairs:
            a, b = pair
            b_pos_in_a = preferences[a].index(b)
            for c in preferences[a][:b_pos_in_a]:
                a_pos_in_c = preferences[c].index(a)
                d_pos_in_c = preferences[c].index(pair_dict[c])
                if a_pos_in_c < d_pos_in_c:
                    if a not in unhappy_set:
                        unhappy_set.add(a)
                        unhappy_num += 1
            
            a_pos_in_b = preferences[b].index(a)
            for c in preferences[b][:a_pos_in_b]:
                b_pos_in_c = preferences[c].index(b)
                d_pos_in_c = preferences[c].index(pair_dict[c])
                if b_pos_in_c < d_pos_in_c:
                    if b not in unhappy_set:
                        unhappy_set.add(b)
                        unhappy_num += 1
        
        return unhappy_num

# @lc code=end

