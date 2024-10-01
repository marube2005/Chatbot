#slicing + create a substring by extracting elements from another string.
# Done in two ways either by indexing[] or slice{}
# indexing involves the [start: stop: step]
name = "Elvis MASTER"
first_name = name[0:5].upper()
last_name = name[5:].lower()
nick_name = name[12: 0:-3]
reversed_name = name[: :-1]
#By default, step is usually one as it accounts for each letter but you can increment by 2 or 3.
print(last_name)
print(first_name)
print(nick_name)
print(reversed_name)

website = "http://www.amazon.com"
ref = website[11:-4] #This is Indexing
print(ref)
slice = slice(11,-4,1)
print(website[slice]) #This is Slicing.