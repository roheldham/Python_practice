from sys import argv 
script, filename = argv

txt_file = open(filename)

print (f"Here is the file that you wanted to read: {txt_file} ")
print (txt_file.read())

print ("Type the filename again:")
file_again = input('> ')

txt_file_again = open(file_again)

print ("Here is the file again")
print (txt_file_again.read())