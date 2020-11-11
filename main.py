import math
import sys


def diff():
    global interest
    global current_rep
    global diff_payment_total
    for x in range(1, int(interest + 1)):
        diff_payment = math.ceil((principal / months) + (i * (principal - ((principal * (current_rep - 1)) / months))))
        diff_payment_total += diff_payment
        overpayment = diff_payment_total - principal 
        print(f"Month {current_rep}: payment is {diff_payment}")
        current_rep += 1
       
    print()
    print(f"Overpayment = {overpayment}")

def annuity():
    global months
    global payment 
    global principal
    if args1[0] == "--principal" and args2[0] == "--periods":
        payment = math.ceil(principal * ((i * math.pow(1 + i, months)) / (math.pow(1 + i, months) - 1)))
        overpayment = payment * months - principal
        print(f"Your monthly payment = {payment}!")
        print()
        print(f"Overpayment = {overpayment}")
    elif  args1[0] == "--principal" and args2[0] == "--payment":
        months = math.ceil(math.log((payment / (payment - (i * principal))), (1 + i)))
        overpayment = payment * months - principal
        
        if months == 1:
            print(f"It will take {months} month to repay this loan!")
        elif months < 12:
            print(f"It will take {months} months to repay this loan!")
        elif months > 11:
            years = divmod(months, 12)
            if years[0] > 1 and years[1] > 0:
                print(f"It will take {years[0]} years and {years[1]} months to repay this loan!")
            elif years[0] == 1 and years[1] == 0:
                print(f"It will take {years[0]} year to repay this loan!")
            elif years[1] == 0:
                print(f"It will take {years[0]} years to repay this loan!")
        print()
        print(f"Overpayment = {overpayment}")
    else:
        principal = math.ceil(payment / ((i * math.pow(1 + i, months)) / (math.pow(1 + i, months) - 1)))
        overpayment = payment * months - principal
        print(f"Your loan principal = {principal}!")
        print()
        print(f"Overpayment = {overpayment}")

diff_payment_total = 0
current_rep = 1 
args = sys.argv
if len(args) == 5:
    args_type = str(args[1]).split("=")
    args1 = str(args[2]).split("=")
    args2 = str(args[3]).split("=")
    args3 = str(args[4]).split("=")
    if args1[0] == "--principal":
        if int(args1[1]) > 0:
            principal = int(args1[1])
        else:
            print("Incorrect parameters")
            exit()
    elif args1[0] == "--payment":
        if int(args1[1]) > 0:
            payment = int(args1[1])
        else:
            print("Incorrect parameters")
            exit()

    if args2[0] == "--periods":
        if int(args2[1]) > 0:
            months = int(args2[1])
        else:
            print("Incorrect parameters")
            exit()
    elif args2[0] == "--payment":
        if int(args2[1]) > 0:
            payment = int(args2[1])
        else:
            print("Incorrect parameters")
            exit()

    if args3[0] == "--interest":
        if float(args3[1]) > 0:
            global interest
            interest = float(args3[1])
            i = interest / (12 * 100)
            if int(interest) < 8:
                interest += 1
        else:
            print("Incorrect parameters")
            exit()    
        
    if args_type[1] == "diff":
        diff()
    elif args_type[1] == "annuity":
        annuity()
else:
    print("Incorrect parameters")
