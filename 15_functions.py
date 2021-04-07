def Name(first_name , last_name):
    print (f"Your name is {first_name} {last_name}")

def Sum(x , y):
    print (f"The sum of the numnbers is: {x + y}")

def Sum2(x , y):
    ans = x + y
    return ans

first = input("Enter your firstname: ")
last = input("Enter your lastname: ")
print(Name(first, last))
Sum(2 , 3)
ans = Sum2 (3, 3)
print(ans)