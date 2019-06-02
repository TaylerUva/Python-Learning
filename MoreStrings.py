import FileWrapper
FileWrapper.hello(__file__)

timesToPrint = 5
print("This will print %s times\n" % timesToPrint * timesToPrint)

s1 = "A"
s2 = "B"
s3 = "C"
s4 = "D"
s5 = "E"
s6 = "F"

print("Using + vs , for string prints:")
print(s1 + s2 + s3)
print(s4, s5, s6)

FileWrapper.goodbye(__file__)
