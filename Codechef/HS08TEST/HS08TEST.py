Assumed_withdrawal_money, initial_acco_balance = map(float, input().split())
if(Assumed_withdrawal_money % 5 == 0):
    if(Assumed_withdrawal_money + 0.5) <= initial_acco_balance:
        initial_acco_balance -= (Assumed_withdrawal_money + 0.5)
print(initial_acco_balance)
    