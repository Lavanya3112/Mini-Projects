print("Welcome to Python Pizza Deliveries!")

print(r'''
      
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\
         /' %%@=%o%%%o|   /(_)o%%% `\
        /  %o%%%%%=@%%|  /%%o%%@=%%  \
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--'
      
''')

size = input("What size pizza do you want? S, M or L: \n").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n").lower()
extra_cheese = input("Do you want extra cheese? Y or N: \n").lower()
delivery = input("Do you want delivery? Y or N: \n").lower()

bill = 0

# Base price
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
else:
    bill = 25

# Pepperoni cost
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

# Extra cheese cost
if extra_cheese == "y":
    bill += 1

# Delivery cost
if delivery == "y":
    bill += 2  # base delivery fee
    if size == "s":
        bill += 3
    elif size == "m":
        bill += 4
    else:
        bill += 5

print(f"\nThe total bill: ₹{bill}")

print("Thank you for choosing us! Hope to see you again!")
