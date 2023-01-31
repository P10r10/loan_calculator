import math
import argparse
import sys


def nb_of_months(monthly, i, loan):
    ni = i / 1200
    months = math.log(monthly / (monthly - ni * loan), 1 + ni)
    time_to_repay(math.ceil(months))
    print(f"Overpayment = {round(24 * monthly - loan)}")


def time_to_repay(months):
    print(f"It will take {months // 12} years and {months % 12} months to repay this loan!")


def monthly_payment(loan, i, nb_pay):
    ni = i / 1200
    monthly = math.ceil(loan * ni * pow(1 + ni, nb_pay) / (pow(1 + ni, nb_pay) - 1))
    print(f"Your annuity payment = {monthly}!")
    print(f"Overpayment = {round(monthly * nb_pay - loan)}")


def loan_principal(a, n, i):
    ni = i / 1200
    principal = a / ((ni * pow(1 + ni, n)) / (pow(1 + ni, n) - 1))
    print(f"Your loan principal = {math.floor(principal)}!")
    print(f"Overpayment = {math.ceil(a * n - principal)}")


def diff(p, n, i):
    total = 0
    i /= 1200
    for m in range(1, n + 1):
        pay = p / n + i * (p - ((p * (m - 1)) / n))
        monthly = math.ceil(pay)
        total += monthly
        print(f"Month {m}: payment is {monthly}")
    print(f"\nOverpayment = {round(total - p)}")


def exit_on_error():
    print("Incorrect parameters")
    exit(1)


parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
args = parser.parse_args()

if args.interest is None:
    exit_on_error()
if len(sys.argv) < 5:
    exit_on_error()
if args.type == "diff":
    diff(args.principal, args.periods, args.interest)
if args.type == "annuity":
    if args.payment is None:
        monthly_payment(args.principal, args.interest, args.periods)
    if args.principal is None:
        loan_principal(args.payment, args.periods, args.interest)
    if args.periods is None:
        nb_of_months(args.payment, args.interest, args.principal)
