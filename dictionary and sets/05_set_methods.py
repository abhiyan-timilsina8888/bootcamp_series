#creating a empty set
b=set()
print(type(b))

# adding value to an empty set
b.add(7)
b.add(3)
b.add(3)
b.add(3) # having double value in the set doesnot affect the set
b.add(7)
b.add(9)
# b.add([1,2,3])  #cannot add any list or dictionary in the set 
# b.add({5:7})  #cannot add any list or dictionary in the set
b.add((1,2,3))  # can add tuple to the set cause it is not changable

print(len(b)) # gives the length of the set
b.remove(9)   # removes the 9 from the set
# b.remove(12)   # gives an error cause 12 is not present in the set
print(b)

# b.pop(9) # gives an error cause pop doesnot take any order it randomly removes the elemnets in a set
b.pop()
print(b)

# b.clear()  #it clears the set leaving no values left
# print(b)

# b.union({8,6,3})
b.intersection({7})
print(b)