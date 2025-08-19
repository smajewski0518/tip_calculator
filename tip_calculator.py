# ===========================================
# A tip calculator
# ===========================================

print("Hi! Let's get started!")

def self_pay():
    print("Then let's work out your total!")
    # Calculating the left over
    your_portion = float(input("How much are you paying? $"))
    your_portion_rounded = round(your_portion, 2)
    left_over_total = total_bill - your_portion_rounded
    left_over_total_rounded = round(left_over_total, 2)
    print(f"\nIf you're paying ${your_portion_rounded}, that leaves ${left_over_total_rounded} for your friends to cover.")
    # Calculate amount the user owes
    user_tip_amount = your_portion * (tip_percentage / 100)
    user_tip_amount_rounded = round(user_tip_amount, 2)
    user_total = your_portion + user_tip_amount
    user_total_rounded = round(user_total, 2)
    # Display user total
    print(f"{tip_percentage}% of your bill is ${user_tip_amount_rounded}.")
    print(f"This means ${your_portion} + ${user_tip_amount_rounded} comes to ${user_total_rounded}!")
    print(f"${user_total_rounded} is how much you owe.")


def even_split():
    # Get user input
    number_of_people = int(input("How many people are paying today?  "))
    everyone_pays = total_bill / number_of_people
    everyone_tip = (total_bill * (tip_percentage / 100)) / number_of_people
    everyone_total = everyone_pays + everyone_tip
    everyone_total_rounded = round(everyone_total, 2)
    print(f"Excellent! Everyone owes {everyone_total_rounded} each.")


while True:
    total_bill = float(input("How much is the total bill? $"))
    # Calculate the tip
    tip_percentage_str = (input("Most people tip at least 20%. What percentage do you want to leave? "))
    # Remove % if entered
    tip_percentage_str = tip_percentage_str.replace('%', '')
    tip_percentage = int(tip_percentage_str)
    splitting_even = input("Are you splitting the bill evenly? Yes or No?  ")
    if splitting_even.lower() == 'yes':
        even_split()
    else:
        self_pay()

    another_calculation = (input("Do you need another calculation? Yes or No?  "))
    if another_calculation.lower() == 'no':
        print("\nCome back to calculate anytime!")
        break



