class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        k = []
        for i in key:
            if (i != ' ') and (i not in k):
                k.append(i)

        mp = {}
        curr = 'a'
        for i in k:
            mp[i] = curr
            curr = chr(ord(curr) + 1)

        res = ""
        for i in message:
            if i.isalpha():
                res += mp[i]
            else:
                res += ' '

        return res
        