print("You arrive in The Lost Woods, the first part of the triforce buried deep in the woods. To obtain this piece, you will need to light torches to find you way and find a key to enter throough the gates.")
print("First, you need to find the torch to light your way.")
while True:
    looking = input("Where will you look, in the bushes, or  inside the great oak tree?:\n").strip().lower()
    if looking == "bushes":
        print("You look in the bushes only to find a couple of berries, which you put in your bag, you then head over to look in the great oak tree finding the torch!")
        break
    elif looking == "great oak tree":
        print("you search inside the Great Oak Tree, finding the torch! congrats. Your next mission is to find the gates leading to the triforce")
        
    else:
        print("Sorry that is not an option, Please type either, 'great oak tree' or 'bushes'")
    
        
    

print("You have the torch to light your path, you need to find the Gates of Secrets leading to the triforce.")
print("You light your torch, and see the fire flickering left but you also see a trail of rocks leading foward.")
while True:
    choice = input("Will you follow the rocks and go foward, or will you follow the torch and go left? (Type foward or type left):\n").strip().lower()
    if choice == "left":
        print("You  go left, following the torch... after 1 hour of long walking, you end up the gates but it is gaurded by an evil elf!")
        break
    elif choice == "foward":
        print("You walk the way the rocks are leading, after several hours you finally arrive at the gates..however it is gaurded by an evil elf.")
    else:
        print("Sorry, that is not an option given. please type 'foward' or 'left'")
      

print("You have found the gates, and ran into the evil elf. He asks you what you are doing here, you say you are here to achieve the first part of the triforce...the elf then says you have to give him berries in exchange for the gate to open")
while True:
    berries = input("Going back to your memories...did you grab the berries?:\n").strip().lower()
    if berries == "yes":
        print("You say yes then give the elf the berries, he then lets you enter the gates and you find the first piece of the triforce.")
        break
    elif berries == "no":
        print("You didn't get the berries and you have to go back..You do end up going back and finally finding the berries you take this journey and give it the elf. He lets you enter the gates and you find the first piece of the triforce.")
    else:
        print("Sorry that is not an option given, please type yes or no.")
    
print("Good job you found the first part of the triforce and now have to find the second. ")
print("Head to the next part of your adventure...which is to be continued...")