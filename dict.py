def change_dict(dict, key, change = 0):
    dict[key] += change
    return dict[key]

dict1 = {'current hp' : 10, 'limit hp' : 20}

print(dict1)

dict1["current hp"] = dict1['limit hp']
print(dict1)