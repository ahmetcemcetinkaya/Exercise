phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
while True:  
    asa = input("Ara : ")

# testing code
    for name, number in phonebook.items():
        if str(asa) == name:
            print(asa + "'s number is %s" % number)
        
        if str(asa) not in phonebook:
            print(asa + " is not listed in the phonebook.")
            break
        

#Lesson Dictionaries Example Program.
