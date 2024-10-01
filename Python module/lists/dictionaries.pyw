#dictionaries = A changeable, unordered collection of Unique key: value pairs.
#               Fast because they use hashing, allow access to a value quickly.

capitals  = {'Kenya': 'Nairobi', 
             'India': 'New Delhi', 
             'Australia':'Opera House',
             'USA': 'Washington DC'}
capitals.update({'Tanzania': 'Arusha', 
                 'Germany': 'Berlin'})# Yo can also update an already existing key to a new value for example:
capitals.update({'Kenya': 'Kakamega'})
capitals.pop('Australia')
#print(capitals['Australia'])
print(capitals.get('Kenya')) # - much safer way as it will return no error even if the key does not exist.
print(capitals.keys()) # - will print only the keys
print(capitals.values()) # - will print only the values.
print(capitals.items()) # - will print all the keys and it's values
capitals.clear() # - will print
#for key in capitals:
    #print(key)
#for x in capitals:
   # print(x)
#for key, value in capitals.items(): - will print all the values and keys.
    #print(key, value)
