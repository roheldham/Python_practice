ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait, that's not 10 things, hold on...")

stuff = ten_things.split()
print ("Enter atleast 4 more things with a space in between")

more_things = input('>')
list_more = more_things.split()

while len(stuff) != 10:
    next_one = list_more.pop()
    print ("Adding:",next_one)
    stuff.append(next_one)
    print (f"There are {len(stuff)} items now.")

print(stuff[1])
print(stuff[-1]) 
print(stuff.pop())
print(' '.join(stuff)) 
print('#'.join(stuff[3:5])) 

