def sort_hashmap_by_value(d):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    return sorted_dict


hashmap = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
sorted_hashmap = sort_hashmap_by_value(hashmap)

print(sorted_hashmap)
