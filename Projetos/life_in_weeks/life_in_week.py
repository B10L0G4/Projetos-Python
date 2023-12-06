# years = 365
# weeks = 52
# months = 12

age = int(input("What is your current age? "))

years = ((365 * age)-32850)*-1
weeks = ((age * 52)- 4680)*-1
months = ((age * 12)- 1080)*-1


print(years, weeks,months)
print(f"You have {age} years,to the 90 years left {years} days {months} months, and {weeks} weeks left.")