expenses = open('input.txt').read().split()
expenses = [int(i) for i in expenses]

for index, expense in enumerate(expenses):
    for other_index, other_expense in enumerate(expenses[index+1:]):
        for third_expense in (expenses[index+other_index+2:]):
            if expense+other_expense+third_expense == 2020:
                print(f'''Expenses {expense} and {other_expense} and {third_expense} add up to
                    {expense+other_expense+third_expense} and the product is {expense*other_expense*third_expense}''')
