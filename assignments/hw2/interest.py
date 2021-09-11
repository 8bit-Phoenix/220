"""
Name: <Christopher Hamilton, II>
<interest>.py

Problem: This program

Certification of Authenticity:
I certify that this is entirely my own work
"""


def main():
    interest_rate = eval(input("Enter annual interest rate: "))
    billing_cycle = eval(input("Enter the number of days in the billing cycle: "))
    net_balance = eval(input("Enter previous net balance: "))
    payment_amount = eval(input("Enter the payment amount: "))
    payment_day = eval(input("Enter the day of the billing cycle that the payment was made: "))
    net_billing = net_balance * billing_cycle
    days_before_end = billing_cycle - payment_day
    end_payment = payment_amount * days_before_end
    net_payment = net_billing - end_payment
    daily_balance = net_payment / billing_cycle
    monthly_interest_rate = (interest_rate / 12) / 100
    monthly_interest_charge = daily_balance * monthly_interest_rate
    print(round(monthly_interest_charge, 2))


if __name__ == "__main__":
    main()
