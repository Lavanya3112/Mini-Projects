print("<<<<WELCOME TO OUR TIP CALCULATOR>>>>")
print("Tip Calculator")
bill = float(input("Enter Bill:\n₹"))
tip = int(input("Enter Tip you wish to give:(5%, 10%, 12%):\n"))
people = int(input("Enter no.of people to split the bill:\n"))
tip_decimal = tip/100
total_bill = bill*tip_decimal+bill
Final_Bill = total_bill/people
print(f"Your Final Bill to pay is ₹{(round(Final_Bill,2))}")