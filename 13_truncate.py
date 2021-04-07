from sys import argv

script, filename = argv

print (f"We are going to erase {filename}.")
print ("If you dont want to do this press Ctrl+C")
print ("If you want to do this press Enter")

input ("?")

print ("Opening the file...")
target = open (filename , 'w')

print ("Truncating the file, goodbye!")
target.truncate()

print ("Now I am going to ask you for three lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")
target.write(line1 + '\n' + line2 + '\n' + line3 +'\n')

print ("Finally we close the file")
target.close()