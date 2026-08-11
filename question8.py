#Employee Record Analyzer

employee=("Arjun","Developer",45000,3)
name,pos,salary,exp=employee
if exp<2:
    bonus=5
elif exp<=5:
    bonus=10
else:
    bonus=15
msalary=salary*12
ab=bonus/100*msalary
print(f"Employee Name: {name}")
print(f"Designation: {pos}")
print(f"Experience: {exp} years")
print(f"Monthly Salary: {salary}")
print(f"Annual Salary: {msalary}")
print(f"Annual Bonus: {ab}")