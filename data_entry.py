from datetime import datetime


def get_date(prompt, allow_default=False):
    date_str = input(f"\n{prompt}")
    if allow_default and not date_str:
        print("Today's date has been entered")
        return datetime.today().strftime("%d-%m-%Y")

    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y")
        print("Date entered successfully!")
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid Date. Make sure the date is real and correctly formatted")
        return get_date(prompt)


def get_amount():
    try:
        amount = float(input("\nEnter the amount: ").strip())
        if amount <= 0:
            print("Amount must be greater than 0.")
            return get_amount()
        else:
            print("Amount Entered Successfully")
            return amount
    except ValueError:
        print("Invalid Input! Please enter a number.")
        return get_amount()


def get_category():
    while True:
        category = input(
            "\nEnter the category ('i' for income, 'e' for expense): ").strip().lower()

        if category != 'e' and category != 'i':
            print("Invalid input! Please enter 'e' for expense and 'i' for income")
        else:
            return category


def get_description():
    return input("\nEnter a description (optional): ")
