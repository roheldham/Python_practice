from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file) 
indata = in_file.read()

print (f"The input file is {len(indata)} bytes long")

print (f"Does the file actually exist? {exists(to_file)}")
print ("Press Ctrl+C to exit and press Return to continue")

input ('>')

out_file = open (to_file, 'w')
out_file.write(indata)

print ("Alright, the operaton is done!")

out_file.close()
in_file.close()