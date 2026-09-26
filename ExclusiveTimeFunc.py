class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        last = []

        for log in logs:
            func, act, time = log.split(':')
            func, time = int(func), int(time)

            if act == 'start':
                if last:
                    res[last[-1][0]] += time - last[-1][2]
                last.append([func, act, time])

            else:
                curr = last.pop()
                res[func] += time - curr[2] + 1

                if last:
                    last[-1][2] = time + 1

        return res
