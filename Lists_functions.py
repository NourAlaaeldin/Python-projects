numbers = [0,1,2,3,4,5]
friends = ["Asmaa","Bassant","Maha","Aya","Noor","Kholoud"]

friends.sort()
print(friends)

print("*********************************")

friends.reverse()
print(friends)

print("*********************************")

friends.extend(numbers) #concatenate numbers list to friends list
print(friends)

print("*********************************")

friends.append("Great") #append an item to the end of the list
print(friends)

print("*********************************")

friends.insert(1,15) #append 15 at position 1
print(friends)

print("*********************************")

friends.remove(15)
print(friends)

print("*********************************")

friends.pop() #pops the last element in the list
print(friends)

print("*********************************")

print(friends.index("Maha"))
print(friends.count("Maha"))

friends2 = friends.copy()

print("*********************************")

friends.clear()
print(friends)

print("*********************************")

print(friends2)