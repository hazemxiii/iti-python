original_list = [1,2,2,2,3,3,4,1,5,6,6,7]
new_list = []
last_added = None
for n in original_list:
    if n != last_added:
        new_list.append(n)
        last_added = n

print("Original list: ",original_list)
print("New list: ",new_list)