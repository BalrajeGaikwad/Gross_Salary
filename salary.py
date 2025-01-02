
"""Ramesh basic salary is input through the keyboard. 
His dearness allowance is 40% of basic salary and house rent allowance is 20% of basic salary. 
Write a program to find his gross salary"""


#The formula to calculate gross salary is: 
#Gross salary = Basic salary + HRA + Other allowances

salary=int(input("Enter the basic salry"))
dearness_allowance=0.4* salary
rent_allowance=0.2*salary

Gross_salary=salary+dearness_allowance+rent_allowance


print(Gross_salary)