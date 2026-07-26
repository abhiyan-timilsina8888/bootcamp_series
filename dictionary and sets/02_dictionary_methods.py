diction ={
    "abhiyan":"smart",
    "intilligent": "people with smart brain",
    "numbers" :[1,3,4],
    "anotherdiction":{"mummy":"who gives birth "},
    }           
    
# print(diction.keys())   #prints the key of the given dictionary
# print(diction.values())  #prints the values of the given dictionary
# print(diction.items())  #prints the (keys,values) in the tuple form of the given dictionary
# print(diction)



#dictionary methods
newone = {
"calculator":"app",
"pubg":"game",
"numbers":[12,13]
}
diction.update(newone)
# print(diction)

print(diction.get("abhiyan")) #prints the value of key abhiyan given in the dictionary
# print(diction["abhiyan"])  #prints the value of key abhiyan given in the dictionary

# # the difference betweeen using the get and [] syntax in the dictionary

print(diction.get("abhiyan2")) #gives none as the key is not given in the dictionary
print(diction["abhiyan2"])  #gives error as the key is not given in the dictionary