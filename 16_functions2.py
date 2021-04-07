def bats_and_balls (bats, balls):
    print (f"You have {bats} bats and {balls} balls")
    if bats > 10:
        print ("That is a lot of bats!")
    elif bats < 2:
        print ("You should buy more bats")
    else:
        print ("That's an adequate number of bats")    

    if balls > 10:
        print ("That is a lot of bats!")
    elif balls < 2:
        print ("You should buy more bats")
    else:
        print ("That's an adequate number of balls")

#Using normal input 
#num_bats , num_balls  = input("Enter number of bats and balls respectively:").split())
#bats_and_balls (int(num_bats), int(num_balls))

#Using list comprehension : 
num_bats , num_balls = [int(i) for i in input("Enter number of bats and balls respectively:").split()]
bats_and_balls(num_bats, num_balls)

