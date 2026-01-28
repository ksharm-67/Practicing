class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rules = {"type" : 0, "color": 1, "name": 2}
        rk, matching = rules[ruleKey], 0

        for obj in items:
            if obj[rk] == ruleValue:
                matching += 1

        return matching
