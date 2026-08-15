class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for idx, price in enumerate(words):
            if price.count('$') == 1 and price[0] == '$' and price[1:].isnumeric():
                amount = int(price[1:])
                after_disc = amount - (amount * discount / 100.00)
                words[idx] = '$' + f"{after_disc:.2f}"
        
        res = ""
        for i in range(len(words)):
            if i == len(words) - 1:
                res += words[i]
                return res
            res += words[i] + ' '
