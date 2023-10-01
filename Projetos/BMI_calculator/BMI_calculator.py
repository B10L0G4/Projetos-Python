# 'Day 2'
# calculadora de massa corporal

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))


bmc =round(peso / altura ** 2, 2)

if bmc <= 18.5:
    print(f'Your BMI is {bmc}, you are underweight.')
elif bmc <= 25:
    print(f'Your BMI is {bmc}, you are a normal weight.')
elif bmc <= 30:
    print(f'Your BMI is {bmc}, you are a slightly overweight.')
elif bmc <= 35:
    print(f'Your BMI is {bmc}, you are a obese.')
else:
    print(f'Your BMI is {bmc}, you are a clinically obese.')


