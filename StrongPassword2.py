class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False

        low, up, dig, spe = False, False, False, False
        special = list("!@#$%^&*()-+")

        for i in range(len(password)):
            if i > 0 and password[i] == password[i - 1]:
                return False

            if not low and password[i].isalpha() and password[i].islower():
                low = True

            elif not up and password[i].isalpha() and password[i].isupper():
                up = True

            elif not dig and password[i].isdigit():
                dig = True

            elif not spe and password[i] in special:
                spe = True

        return low and up and dig and spe
        

            
