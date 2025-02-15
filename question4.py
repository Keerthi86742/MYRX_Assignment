def min_platforms(arr, dep):
    arr = sorted([int(time.replace(":", "")) for time in arr])
    dep = sorted([int(time.replace(":", "")) for time in dep])

    n = len(arr)
    platform_needed = 0
    max_platforms = 0
    i, j = 0, 0

    
    while i < n and j < n:
        if arr[i] < dep[j]:  
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:  
            platform_needed -= 1
            j += 1

    return max_platforms

# Example Usage:
arr1 = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep1 = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(min_platforms(arr1, dep1)) 

arr2 = ["9:00", "9:40"]
dep2 = ["9:10", "12:00"]
print(min_platforms(arr2, dep2))  
