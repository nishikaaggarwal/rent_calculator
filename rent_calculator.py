# inputs
# food
# rent
# electricity bill
# extra expenses 

Rent = float(input("Monthly rent for the room/flat = "))
Food = float(input("Total food expenses on food = "))
electricity_spent = float(input("total units of electricity used in the room/flat = "))
charge_per_unit = float(input("charge per unit of electricity in your area = "))
electricity_bill = electricity_spent * charge_per_unit
extra_expenses = float(input("extra spending done = "))
persons = int(input("number of persons living in a room/flat = "))
output = float(Rent + Food + electricity_bill + extra_expenses) // persons
print("Each person will have to pay = ", output)
