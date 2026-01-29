class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalid = []
        prevTransactions = {}
        #{name: "name,time,price,city"}

        for transaction in transactions:
            tr = transaction.split(',')
            name, time, price, city = tr[0], int(tr[1]), int(tr[2]), tr[3]

            if name not in prevTransactions:
                prevTransactions[name] = [transaction]
            else:
                prevTransactions[name].append(transaction)

            conflict = False
            for val in prevTransactions[name][:-1]:
                curr = val.split(',')
                namePrev, timePrev, pricePrev, cityPrev = curr[0], int(curr[1]), int(curr[2]), curr[3]
                if abs(time - timePrev) <= 60 and city != cityPrev:
                    if val not in invalid:
                        invalid.append(val)
                    conflict = True

            if price > 1000 or conflict:
                invalid.append(transaction)

        return list(set(invalid))
