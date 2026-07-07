class Solution:
    def numSteps(self, s: str) -> int:
        if s == '1': return 0
        if s == '0': return 0

        num = [int(i) for i in s]
        steps = 0
        
        while num != [1]:
            if num[-1] == 0:
                # divide i.e. right shift
                num.pop()

            else:
                # add 1
                carry = 0
                for i in range(len(num) - 1, -1, -1):
                    if num[i] == 0:
                        num[i] = 1
                        carry = 0
                        break
                    
                    else:
                        num[i] = 0
                        carry = 1

                if carry == 1:
                    num.insert(0, 1)

            steps += 1
        
        return steps
