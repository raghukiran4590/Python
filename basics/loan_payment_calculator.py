loan_amount = float(input("Enter the loan amount:"))
# print(loan_amount)
apr = float(input("Enter the annual percentage amount:"))
# print(apr)
loan_term = float(input("Enter the duration of the loan in months:"))
# print(loan_term)
monthly_payment = float(input("Enter the monthly payment:"))
# print(monthly_payment)
monthly_interest_rate = apr/100/12
print("Monthly interest rate is ",monthly_interest_rate)

total_amount_paid = 0

for i in range(int(loan_term)):
    amount_paid = float(monthly_payment+monthly_interest_rate)
    total_amount_paid = total_amount_paid + amount_paid
    loan_amount = loan_amount - amount_paid
    if(loan_amount < amount_paid):
        print(f"Amount paid for month - {i+1} : {amount_paid}")
        print(f"Loan Amount is paid off in {i+1} months")
        break
    print(f"Amount paid for month - {i+1} : {amount_paid}, Loan Amount : {loan_amount}")

print(f"Total amount paid is : ${total_amount_paid + amount_paid}") 