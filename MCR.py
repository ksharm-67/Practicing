class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        without_dupe = []
        for word in responses:
            x = {i for i in word}
            without_dupe.append(x)

        cnt = {}
        for resp in without_dupe:
            for i in resp:
                cnt[i] = cnt.get(i, 0) + 1
        
        common = ["", 0]
        for k, v in cnt.items():
            if v > common[1] or (v == common[1] and k < common[0]):
                common = [k, v]

        return common[0]
