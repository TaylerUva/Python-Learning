import FileWrapper
FileWrapper.hello(__file__)

printType = "Printed with %s:\t"

string1 = "This is a string with numbers: %f and %i" % (5.2 + 3.2, 5.2 + 3.2)
string2 = "This is a string with numbers: %r and %r" % (5.2 + 3.2, 5.2 + 3.2)
string3 = "This is a string with numbers: %d and %d" % (5.2 + 3.2, 5.2 + 3.2)
string4 = "This is a string with numbers: %s and %s" % (5.2 + 3.2, 5.2 + 3.2)
print(printType % "%f and %i", string1)
print(printType % "%r", string2)
print(printType % "%d", string3)
print(printType % "%s", string4)

print()
question = "What does %s do?"
print(question % "this")

# Testing %r
conclusion = "%r puts quotes but only on strings it seems"
print(question % ("%r"))
print(question % ("%r" % string1))
print(question % ("%r" % 5))
print(question % string1)

# Printing without a space
print("\n%s" % conclusion)

print()
conclusion = "Using %s allows you to use a place holder in the future for the same string, makes less copy pasting! Cool!"
print(conclusion, "\nIt also allows you to insert without spaces",
      "even cool%s" % "er")
print("Like this:", conclusion % "PLACEHOLDER INSERTED")

finalConclusion = "%r is for raw messages and %s is for displaying"
print()
print(printType % "%r", "%r" % finalConclusion)
print(printType % "%s", "%s" % finalConclusion)

FileWrapper.goodbye(__file__)
