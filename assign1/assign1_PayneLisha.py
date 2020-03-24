#Lisha Payne
#Web Dev and Programming Assign #1
#Due Friday, Feb 7


import random

#get random number of each gumball
yellow = random.randint(10,15)
blue = random.randint(1,10)
white = random.randint(6,15)
green = random.randint(10,25)
black = random.randint(1,12)
purple = random.randint(5,10)
silver = random.randint(4,6)
cyan = random.randint(5,12)
magenta = random.randint(0,10)
red = 1

#Create gumballs list
gumballs=["Yellow", "Blue", "White", "Green", "Purple", "Silver", "Cyan", "Magenta", "Red"]
#Create gumballs count
gumballs_count = [yellow, blue, white, green, purple, silver, cyan, magenta, red]

#Create array to keep track of gumballs purchased
total_gumballs_purchased = 0
purchased_gumballs=[0,0,0,0,0,0,0,0,0,0]

#print number of each Gumball
print("Welcome to the CIMS Gumball Machine Simulator")
print("You are starting with the following Gumballs:")
print(yellow, "Yellow")
print(blue, "Blue")
print(white, "White")
print(green, "Green")
print(black, "Black")
print(purple,"Purple")
print(silver, "silver")
print(cyan, "cyan")
print(magenta,"magenta")
print("and 1 Red")
print("Here are your random purchase")

#create while Loop to keep track of Gumballs purchased
while True:
    gumballs_choice=random.choice(gumballs_count)
    total_gumballs_purchased = total_gumballs_purchased + 1

    #purchased_gumballs[gumballs.index(gumballs_choice)] = purchased_gumballs[gumballs.index(gumballs_choice)] + 1
    
    print(gumballs_choice)
    #if red gumball found, end loop
    if gumballs_choice == "Red":
        break

#Calculate cost of gumballs
print("You purchased {0} gumballs for a total of {1}".format(total_gumballs_purchased, (0.25*total_gumballs_purchased)))
get_max = max(purchased_gumballs)
print("The color(s) purchased most: ", end="")

#Find max to calculate most purchased Gumball
for index in range(len(purchased_gumballs)):
    if purchased_gumballs[index]==get_max:
        print(gumballs[index],end=" ")


    





