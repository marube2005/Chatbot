#set = collection which is unordered,unindexed. No duplicate values.
games = {"Handball" , "Netball" , "Volleyball" , "Football" }
dishes = {"bowl" , "plate" , "cup" , "Football"}
games.add("Basketball")
#games.clear()
#games.pop()
#games.copy()
#games.sort()
#games.update(dishes) # update all values from dishes and set them to games.
for z in games:
    print(z)
#lunch_games = games.union(dishes) 
#for x in lunch_games:
   # print(x)
print(dishes.difference(games)) # - set difference.
print(games.intersection(dishes))
#print(games)
