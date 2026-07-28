class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes, tables = set(), set()
        placed = {}
        for order in orders:
            table, dish = int(order[1]), order[2]
            if table in placed:
                placed[table].append(dish)
            else:
                placed[table] = [dish]
            dishes.add(dish)
            tables.add(table)

        display_table = [["0" for i in range(len(dishes) + 1)] for j in range(len(tables) + 1)]
        display_table[0][0] = "Table"

        dishes, tables = sorted(list(dishes)), sorted(list(tables))
        for i in range(len(dishes)):
            display_table[0][i + 1] = dishes[i]
        for j in range(len(tables)):
            display_table[j + 1][0] = tables[j]

        dish_idx = {}
        for idx in range(1, len(display_table[0])):
            dish_idx[display_table[0][idx]] = idx
        
        for tbl in range(1, len(display_table)):
            current_table = display_table[tbl][0]
            for d in placed[current_table]:
                display_table[tbl][dish_idx[d]] = str(placed[current_table].count(d))
                    
            display_table[tbl][0] = str(display_table[tbl][0])
        
        return display_table


