# Personal Finance Tracker

A simple command-line Personal Finance Tracker built with Python. Track your income and expenses, view summaries, and visualize your transactions over time with graphs.

---

## Features

- Add new transactions with:
  - Date (optional, defaults to today)
  - Amount
  - Category (Income 'i' / Expense 'e')
  - Description (optional)
- View transactions in a specific date range
- View total income, total expenses, and net savings
- Plot daily income and expenses on a graph

---

## File Structure

- main.py – Main program with CSV handling, adding, viewing, and plotting transactions.

- data_entry.py – Handles input validation for date, amount, category, and description.

- finance_data.csv – CSV file where transactions are stored (created automatically if it doesn’t exist).
