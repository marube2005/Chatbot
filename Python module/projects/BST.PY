# A binary search is a searching algorithms that works by repitedly splitting a set of data into half,until the target value is found.
#Example in a list as shown [1,2,3,4,5,6,7,8,9,10] and the target value is two. It will repeatidly split the list into half,until the target value is found(which is Two)
# a function that takes a list and a target parameter
# a multiple variable: middle,start,end,steps.
# a recursion or while loop to repeatidly split the list into half,until the target value is found.
# increase steps each time a split is done.
# conditions to track target position.
# Binary search is quicker than linear search because bs Doesn't have to look for every single value unlike linear search data.

def binary_search(list,parameter):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Steps",steps, ":",str(list[start:end+1]))
        steps= steps + 1
        middle = (start + end)/2

        if parameter == list[middle]:
            return middle
        if parameter < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 5

binary_search(my_list,target)
