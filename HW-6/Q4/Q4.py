def delete_keys(keys, dictionary):
    for key in keys:
        del dictionary[key]
    
    return dictionary

my_dict = {"firstName": "Amy", "lastName": "K", "birthYear": 2000, "nationality": "Chinese"}
print(delete_keys(["lastName","birthYear"], my_dict))