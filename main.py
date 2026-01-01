# Give the following options:
# 1. Add a new transaction
# 2. View transactions and summary within a data range
# 3. Exit

# Allow the user to enter the choice
# For adding a transaction --> ask for: date, amount, income or expense, description(optional)

# FOr summary --> ask for a range , then display the transactions, SUMMARY : total income, total expense, net profit/loss
# Option to view this as a lot


import pandas as pd
import csv
from datetime import datetime
import matplotlib.pyplot as plt

from data_entry import get_amount, get_category, get_date, get_description


class CSV:

    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("\nTransaction Entered Successfully! \n")

    @classmethod
    def view_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)

        df['date'] = pd.to_datetime(df['date'], format=CSV.DATE_FORMAT)

        start_date = datetime.strptime(start_date, CSV.DATE_FORMAT)
        end_date = datetime.strptime(end_date, CSV.DATE_FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        # filtered_df = df[df[start_date <= df['date'] <= end_date]]

        if filtered_df.empty:
            print("\nNo data found in the given range")
        else:
            print(
                f"\nTransactions from {start_date.strftime(CSV.DATE_FORMAT)} to {end_date.strftime(CSV.DATE_FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={
                  "date": lambda x: x.strftime(CSV.DATE_FORMAT)}))

        total_income = filtered_df[filtered_df["category"]
                                   == "i"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"]
                                    == 'e']["amount"].sum()

        print("\nSummary: ")

        print(f"Your total income is ${total_income:.2f}")
        print(f"Your total expense is ${total_expense:.2f}")

        if total_income > total_expense:
            print(f"\nNet saving is ${total_income - total_expense}")
        elif total_expense > total_income:
            print(f"\nNet expense is ${total_expense - total_income}")
        else:
            print("\nIncome and Expenses are equal")

        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date(
        prompt="Enter the date of transaction (dd-mm-yyyy) or press enter for today's date: ", allow_default=True)
    amount = get_amount()
    catgegory = get_category()
    description = get_description()

    CSV.add_entry(date, amount, catgegory, description)


def View():
    start_date = get_date(
        prompt="Enter the start date in the format (dd-mm-yyyy): ")
    end_date = get_date(
        prompt="Enter the end-date in the format (dd-mm-yy) or press enter to proceed with today's date: ", allow_default=True)
    df = CSV.view_transactions(start_date, end_date)

    ask_to_plot = input(
        "\nEnter 'x' to plot this on a graph: ").strip().lower()

    if ask_to_plot == 'x':
        plot_transactions(df)


def plot_transactions(df):
    df.set_index('date', inplace=True)

    income_df = df[df["category"] == 'i'].resample(
        "D").sum().reindex(df.index, fill_value=0)

    expense_df = df[df["category"] == 'e'].resample(
        "D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color='g')
    plt.plot(expense_df.index,
             expense_df["amount"], label="Expense", color='r')
    plt.xlabel('date')
    plt.ylabel('amount')
    plt.title('Income and Expense over time')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. ADD NEW TRANSACTIONS")
        print("2. VIEW TRANSACTIONS AND SUMMARY")
        print("3. EXIT")

        user_choice = input("\nEnter your choice (1/2/3): ").strip()

        if user_choice == '1':
            add()
        elif user_choice == '2':
            View()
        elif user_choice == '3':
            print("\nThank You. See you later!")
            break
        else:
            print("\nInvalid Choice! Please try again")


if __name__ == "__main__":
    main()
