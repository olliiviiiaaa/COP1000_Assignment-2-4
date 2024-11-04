# input statements
salary = 1250
numDependents = 2
stateTax = 0.065
federalTax = 0.28
dependentDeduction = 0.025
# input from user
salary = float(input("Please enter your salary amount: "))
numDependents = float(input("Please enter your number of dependents: "))
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * dependentDeduction * numDependents
takeHomePay = salary - (stateTax + federalTax + dependentDeduction)
# output statements
print("State tax: $" + str(stateTax))
print("Federal tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))