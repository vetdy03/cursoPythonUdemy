users = [["chanchito", 8],
         ["zelipe", 7],
         ["pulga", 4]
         ]



#print(users)
users.sort(key=lambda el:el[1], reverse= True) 
print(users)