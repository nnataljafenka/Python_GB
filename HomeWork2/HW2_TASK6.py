products = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
            (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
            (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
# value = [[], [], [], []]
value = [[] for i in range(len(products[0][1]))]
prod_analytics = dict()
j = 0
for key in products[1][1]:
    # print(key)
    for i in range(len(products)):
        value[j].append(products[i][1][key])
    prod_analytics[key] = value[j]
    j += 1
print(prod_analytics)
