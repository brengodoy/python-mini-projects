def ask_for_number(prompt,must_be_integer=False):
    print(prompt)
    number = None
    while number is None:
        number = read_input()
        try:
            if float(number) > 0:
                if must_be_integer:
                    return int(number)
                else:
                    return float(number)
            else:
                print("Please enter a positive number.")
                number = None
        except ValueError:
            number = None
            print("Please enter a valid number")

def read_input():
    return input()
    
def calculate_tip(total_cost,tip_percentage,amount_of_people):
    tip = tip_percentage * total_cost / 100
    to_pay_per_person = (tip + total_cost) / amount_of_people
    return tip, to_pay_per_person
    
def ask_all_data():
    total_cost = ask_for_number("Please enter the total cost of the order: ")
    tip_percentage = ask_for_number("Please enter the tip percentage you want to pay: ")
    amount_of_people = ask_for_number("Please enter how many people are paying: ",True)
    return total_cost,tip_percentage,amount_of_people

def show_results(total_cost,tip_percentage,tip,to_pay_per_person):
    print("Total cost: $" + str(total_cost))
    print("Tip (" + str(tip_percentage) + "%): $" + str(tip))
    print("Total to pay: $" + str(total_cost + tip))
    print("Each person should pay: $" + str(to_pay_per_person))

def main():
    total_cost,tip_percentage,amount_of_people = ask_all_data()
    tip,to_pay_per_person = calculate_tip(total_cost,tip_percentage,amount_of_people)
    show_results(total_cost,tip_percentage,tip,to_pay_per_person)

if __name__ == "__main__":
    main()