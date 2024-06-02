Dictionary={}
while True:
    print("/nDictionary Menu")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")
    
    option = input("Enter an option of ur choice:")
    if option== '1':
        Word=input("Enter a Word: ")
        Meaning=input("Enter the meaning of the Word: ")
        Dictionary[Word]=Meaning
        print(f" Word '{Word}' & Meaning '{Meaning}' added sucessfully ")
    elif option== '2':
        Word=input("Enter a Word to search the meaning: ")
        Meaning=Dictionary.get(Word)
        if Word in Dictionary:
            print(f"Meaning of the '{Word}' is {Dictionary[Word]}")
        else:
            print(f"Entered '{Word}' Meaning is not found in the dictionary")
    elif option== '3':
        if Dictionary:
              for Word, Meaning in Dictionary.items():
                     print(f"All the words: '{Word}' : '{Meaning}'")
        else:
              print("The dictionary is empty")
    elif option=='4':
        Word=input("Enter a Word to Update :")
        if Word in Dictionary:
            New_meaning=input("Enter the new meaning:")
            Dictionary[Word]=New_meaning
            print(f"'{Word}' & '{New_meaning}' has been sucessfully updated in the dictionary")
        else:
            print(f"The Word '{Word}' is not sucessfully updated ")
    elif option=='5':
        Word=input("Enter a word to be deleted:")
        if Word in Dictionary:
            del Dictionary[Word]
            print(f"'{Word}' has been deleted fromm the dictionary")
        else:
            print(f"The '{Word}' is not there in the Dictionary")
    elif option== '6':
        print("Sucessfully Exited from the Dictionary")
        break
    else:
        print(f"Invalid Input '{option}'")
