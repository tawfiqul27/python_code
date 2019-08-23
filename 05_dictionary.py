### this will cover dictionary, list, set, tuple


###### This program is fro list and tuple
# def main():
#     friends = [ 'naiem', 'nafi', 'najmul', 'mir', 'sakib' ]     # if you use parenthesis i,e tuple this program will do the same. But you cannot append or remove any item from the list
#     # print(', '.join(friends))         this will print the list without comma
#     print(len(friends))
#     print(friends[2])
#     print(friends[1:5:2])           # this will print every second item and the range is from 1 to 5. For list you have to use semi-colon but for tuple you have to use comma
#     a = friends.index('mir')        # you can use index to print an item
#     print(a)
#     friends.append('amin')          # this will append an item at the end of the list
#     friends.insert(0,'sharif')      # this will inset an item at specific place 
#     friends.remove('sakib')         # this will remove sakib from the list
#     friends.pop()                   # this will delete the last item from the list. pop(4) will delete the 4th item from the list. del friend[3] will do the same
#     friends.reverse()               # this will reverse the list

#     friend_list(friends)            


# def friend_list(o):
#     for i in o:
#         print(i, end=' ', flush=True)        # you can put \n for newline, \t for tab

# if __name__ == '__main__':
#     main()
    


##### This program is for dictionary

def main():
    # both of the dictionary representation is the same
    #animals = { 'puppy':'jenny', 'lion':'grrr', 'hen':'munro', 'dog':'justin' }
    animals = dict(puppy='jenny', lion='grrr', hen='munro', dog='justin') 
    print(animals['lion'])  # this will print the lion
    animals['lion']= 'I am a Lion now'  # this will change a value
    animals['monkey']='Haha'    # this will add new item at the end
    

    for k, v in animals.items():
        print(f'{k}: {v}')
    print("This is after the animal_dict function.")
    animal_dict(animals)

    print('THis will print the key.')
    for k in animals.keys():
        print(k)
    
    print('This will print the value.')
    for v in animals.values():
        print(v)

def animal_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')
# you can use both type of for loop. one is with key value pair and the other is without


if __name__ == '__main__':
    main()
    












