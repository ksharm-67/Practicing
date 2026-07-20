class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits, mp = 0, {}

        for domain in cpdomains:
            v, d = "", ""
            for x in domain:
                if x.isnumeric():
                    v += x
                elif x == " ":
                    continue
                else:
                    d += x
            
            if d in mp:
                mp[d] += int(v)
            else:
                mp[d] = int(v)
            inner = d.split('.')
            ext = inner[-1]

            if len(inner) == 3:
                sub = inner[1] + '.' + inner[2]
                if sub in mp:
                    mp[sub] += int(v)
                else:
                    mp[sub] = int(v)

            if ext in mp:
                mp[ext] += int(v)
            else:
                mp[ext] = int(v)
            
        res = []
        for k, v in mp.items():
            res.append(str(v) + ' ' + k)

        return res
