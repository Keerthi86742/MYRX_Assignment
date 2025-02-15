li = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G'] 
dici = {}
for val in li:
    if val not in dici:
        dici[val] = 1
    else:
        dici[val] += 1


sorted_keys = sorted(dici.keys())  
sorted_list = [char for char in sorted_keys for _ in range(dici[char])]

print(sorted_list)