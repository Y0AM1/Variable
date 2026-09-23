kw_hours_used = int(input("Enter the KW Hours Used: "))
under = .07633
over = .09259
if kw_hours_used <= 1000 :
    amount_owed = kw_hours_used * under
else:
    if kw_hours_used >= 1000 :
       amount_owed = ((kw_hours_used - 1000) * over) +76.33

print("Amount owed is $", amount_owed)