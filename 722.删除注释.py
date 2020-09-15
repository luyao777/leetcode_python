#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#

# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ret = []
        commented = False
        flag = -1
        for l in source:
            nl = ''
            i = 0
            while i < len(l):
                if not commented:
                    if l[i:i + 2] == '//':
                        break
                    elif l[i:i + 2] == '/*':
                        commented = True
                        flag = len(ret)
                        i += 2
                    else:
                        nl += l[i]
                        i += 1
                else:
                    if l[i:i + 2] == '*/':
                        commented = False
                        i += 2
                    else:
                        i += 1
            if flag != -1 and not commented:
                if len(ret) == flag:
                    if nl != '':
                        ret.append(nl)
                else:
                    ret[-1] += nl
                flag = -1
            elif nl != '':
                ret.append(nl)

        return ret


# @lc code=end
