print("You arrive in The Lost Woods, the first part of the triforce buried deep in the woods. To obtain this piece, you will need to light torches to find you way and find a key to enter throough the gates.")
print("First, you need to find the torch to light your way.")
looking = input("Where will you look, in the bushes, or  inside the great oak tree?:\n").strip().lower()
if looking == ("bushes"):
    print("You look in the bushes only to find a couple of berries, which you put in your bag, you then head over to look in the great oak tree finding the torch!")
elif looking == ("great oak tree"):
    print("you search inside the Great Oak Tree, finding the torch! congrats. Your next mission is to find the gates leading to the triforce")
else:
    print("Sorry that is not an option, Please type either, 'great oak tree' or 'bushes'")