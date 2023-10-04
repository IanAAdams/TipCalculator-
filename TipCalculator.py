print("Welcome to the tip calculator.")
total = float(input("Please enter the bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 ,15 or other? "))
number_of_people = int(input("How many people will split the bill? "))
total_with_tip = total * (1 + percentage/100)

each_person_pays = (total_with_tip / number_of_people)
final_amount = "{:.2f}".format(each_person_pays)
print(f"Each person should pay {final_amount}")