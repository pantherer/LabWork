data = ["sunil","roshan",29]
data.append(43)
print(data)
data.insert(1,"amul")
print(data)
data2 = ["a","b",12]
print(data+data2)
data3 = []
data3 = data.copy()
print(data3)








data = ["sunil","roshan",29]
data2 = ["a","b",12]
data2.extend(data)
print(data2)
data.extend(data2)
print(data)
data2.clear()
print(data2)
datas = tuple(data)


