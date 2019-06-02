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
print("Using + :", s1 + s2 + s3)
print("Using , :", s4, s5, s6)
print()

tripleDoubleQuote = """
START
With tripple quote you can print alot.

It also stores the returns apprently
I wonder if it 		does indents


Yes it does
It also stores the returns
END
"""

print("Regular:", tripleDoubleQuote)
print("Raw: %r" % tripleDoubleQuote)

FileWrapper.goodbye(__file__)
