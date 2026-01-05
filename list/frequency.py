arr = [100,200,300,110,210,200,110,110,100]

freq_list = []

for i in arr:

    occ = arr.count(i)

    if occ>1 and i not in freq_list:

        freq_list.append(i)
print(freq_list) 