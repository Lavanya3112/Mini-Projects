print("Welcome to our Rollercoaster Ride Ticket Counter!")

print('''
      
      .       .           ._._.    _                     .===.
      |`      |`        ..'\ /`.. |H|        .--.      .:'   `:.
     //\-...-/|\         |- o -|  |H|`.     /||||\     ||     ||
 ._.'//////,'|||`._.    '`./|\.'` |\\||:. .'||||||`.   `:.   .:'
 ||||||||||||[ ]||||      /_T_\   |:`:.--'||||||||||`--..`=:='...  jv 
      
''')

height = int(input("Enter your height in cm: "))

if height < 120:
    print("You cannot ride.")
else:
    print("You can ride!")

    age = int(input("Enter your age: "))

    # Ticket price based on age
    if age < 12:
        bill = 80

    elif 12 <= age <= 18:
        bill = 100

    elif 18 < age < 45:
        bill = 156

    elif 45 <= age <= 55:
        bill = 0
        print("🎉 FREE RIDE for Mid-Life Crisis Survivors! 😭😂")

    else:
        bill = 156   # Normal adult price for 55+

    # Extra photos (+20), but not for free riders
    want_photos = input("Do you want photos? Yes or No: ").lower()

    if want_photos == "yes":
        bill += 20

    print(f"Your final bill is: ₹{bill}")