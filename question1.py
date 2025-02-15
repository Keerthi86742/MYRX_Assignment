def sorted_array(arr):
    ans = []
    for val in arr:
        ans.append(abs(val) ** 2)
    ans.sort()
    return ans


li =[-12, -8 , -7, -5, 2, 4, 5, 11, 15]
s = sorted_array(li)
print(s)