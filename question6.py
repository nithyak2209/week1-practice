#Expense Tracker

expenses=[]
for i in range(7):
    expenses.append(int(input("Enter expense: ")))
print(f"Total expenses: ₹ {sum(expenses)}")
print(f"Average expenses: ₹ {(sum(expenses)//7)}")
print(f"Highest Expense: ₹ {max(expenses)}")
count=0
low=0
for i in expenses:
    if i>500:
        count+=1
    if i<=500:
        low+=1
print(f"Number of Expenses Above ₹500: {count}")
print(f"Number of Expenses Below ₹500: {low}")