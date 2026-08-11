#Message Slicing Tool

string=input("Enter string:")
print(f"First 5 Character: {string[:5]}")
print(f"Last 5 Character: {string[-5:]}")
print(f"Character from Index 2 to 7: {string[2:7]}")
print(f"Every Second Character: {string[::2]}")
print(f"Message inReverse: {string[::-1]}")
print(f"Message Without First and Last Character: {string[1:-1]}")
