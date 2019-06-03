import FileWrapper
FileWrapper.hello(__file__)

print("""Please select a questioning style:
1. Question Style
2. Form Style
""")
style = int(input("Please type the number of the style you want: "))

if style == 1:
    print("What is your name?")
    name = input()
    print("What is your age?")
    age = int(input())

elif style == 2:
    print("Please complete the following:")
    name = input("Name: ")
    age = int(input("Age: "))

if age >= 21:
    status = "you are legally able to drink"
else:
    status = "you won't be able to drink for %i more years" % (21 - age)

print("\nHello %s, %s" % (name, status))

FileWrapper.goodbye(__file__)
