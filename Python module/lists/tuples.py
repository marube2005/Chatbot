#tuples = collection which is ordered and unchangeable used to
#        group together related data. (Similar to lists.)
# the word student here is a tuple.
student = ("Elvis", 21 , "male")
print(student.count("male"))
print(student.index(21))

for i in student:
    print(i)
if "Lisa" in student:
    print("Lisa is here.")
elif "male" in student:
    print("Male is here. Lisa ain't here.")