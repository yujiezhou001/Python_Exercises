# This is If/Else practice

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":

    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")

# This is Loop practice

print("""This is the second practice which is loop practice. 
Do you want to continue? Yes or No""")

yes_or_no = input("> ")

if yes_or_no == "Yes":
    the_count = [1, 2, 3, 4, 5]
    fruits = ['apples', 'oranges', 'pears', 'apricots']
    change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

    # this first kind of for-loop goes through a list
    for number in the_count:
        print(f"This is count {number}")

    # same as above
    for fruit in fruits:
        print(f"A fruit of type: {fruit}")

    # also we can go through mixed lists too
    # notice we have to use {} since we don't know what's in it
    for i in change:
        print(f"I got {i}")

    # we can also build lists, first start with an empty one
    elements = []

    # then use the range function to do 0 to 5 counts
    for i in range(0, 6):
        print(f"Adding {i} to the list.")
    # append is a function that lists understand
        elements.append(i)

    # now we can print them out too
    for i in elements:
        print(f"Element was: {i}")
else:
    print ("Fine. There will be no more exercises!")