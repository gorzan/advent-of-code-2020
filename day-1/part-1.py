expenses = open('input.txt').read().split()
expenses = [int(i) for i in expenses]

for index, expense in enumerate(expenses):
    for other_expense in expenses[index+1:]:
        if expense+other_expense == 2020:
            print(f'Expenses {expense} and {other_expense} add up to {expense+other_expense} and the product is {expense*other_expense}')
