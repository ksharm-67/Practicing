class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        res = []

        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]

            temp = []
            for j in range(len(products)):
                if products[j][:i] == prefix:
                    temp.append(products[j])

            temp.sort()
            res.append(temp[:3])   
            temp = []

        return res
