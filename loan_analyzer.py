# coding: utf-8


"""Part 1: Automate the Calculations.
"""
loan_costs = [500, 600, 200, 1000, 450]

# 1. How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
Number_of_loans = len(loan_costs)
# Print the number of loans from the list
print(f'The Number of Loans is {Number_of_loans}')

# 2. What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
Total_loans = sum(loan_costs)
# Print the total value of the loans
print(f'The Total Cost of all Loans is $ {Total_loans}')

# 3. What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
Average_loan_amount = sum(loan_costs) / len(loan_costs)
# Print the average loan amount
print(f'The Average Loan Amount is ${Average_loan_amount: .0f}')



"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
FV = loan.get("future_value")
Remain = loan.get("remaining_months")
# Print each variable.
print(f'The Future Value is ${FV}, and the remaining month is {Remain}')

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
fair_value = loan["future_value"]/(1+.2/12)**loan["remaining_months"]
print(f'The Fai Value is ${fair_value:.2f}')

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
if fair_value >= loan["loan_price"]:
    print("The Loan is Worth at Least the Cost to Buy it")
else:
    print("The loan is too Expensive and not Worth the price")

"""Part 3: Perform Financial Calculations.
"""

# # Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# # @TODO: Define a new function that will be used to calculate present value.
# #    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# #    The function should return the `present_value` for the loan.
def Calculate_PV(future_value,remaining_months,annul_discount_rate):
    present_value = future_value/(1+annul_discount_rate/12)**remaining_months
    print(f'The Present Value is ${present_value:.2f}')
    return()

# # @TODO: Use the function to calculate the present value of the new loan given below.
# #    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# print(f"The present value of the loan is: {present_value}")
Calculate_PV(new_loan["future_value"],0.2,new_loan["remaining_months"])


# """Part 4: Conditionally filter lists of loans.

# In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.
# """

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# # @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# # @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# for loan_price in loans: 

for dict in loans:
    if dict.get("loan_price") <= 500:
        inexpensive_loans.append(dict)


# # # @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)


# # """Part 5: Save the results.

# Output this list of inexpensive loans to a csv file
#     1. Use `with open` to open a new CSV file.
#         a. Create a `csvwriter` using the `csv` library.
#         b. Use the new csvwriter to write the header variable as the first row.
#         c. Use a for loop to iterate through each loan in `inexpensive_loans`.
#             i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

#     Hint: Refer to the official documentation for the csv library.
#     https://docs.python.org/3/library/csv.html#writer-objects

# """

# # Set the output header

# # Set the output file path

# # @TODO: Use the csv library and `csv.writer` to write the header row
# # and each row of `loan.values()` from the `inexpensive_loans` list.
# # YOUR CODE HERE!
import csv
from pathlib import Path

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

csvpath = Path("inexpensive_loans.csv")

with open(csvpath,"w") as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())