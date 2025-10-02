#JS 6th silly sentances (mad lib)

noun_person = input("Give me a noun (person):\n").strip().lower()
noun_person2 = input("Tell me another noun (person):\n").strip().lower()
noun_thing = input("tell me a noun but a thing:\n").strip().lower()
noun_thing3 = input("Give me a noun (whichever):\n").strip().lower()
noun_thing4 = input("tell me another noun:\n").strip().lower()
noun_thing5 = input("Tell me one last noun:\n").strip().lower()
adjective = input("Lastly, tell me an adjective:\n").strip().lower()

print(noun_person, "Went to the beach with", noun_person2,".", "First, they swam in their", noun_thing, "Then they saw", noun_thing3, "and", noun_thing4,".", "lastly, they built a sandcastle out of", noun_thing5, "Their trip to the beach was very", adjective )