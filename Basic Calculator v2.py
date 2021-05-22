print('=====CALCULATOR=====')

print(
"""
Select calculator:
  1. Addition
  2. Multiplication
  3. Subtraction
  4. Division
  5. Exponentiation
"""
)

calc = int(input('Select your calculator: '))
print('\n')

if calc == 1:
  print('=====ADDITION CALCULATOR=====\n')
  num1 = int(input('Input your first number: '))
  num2 = int(input('Input your second number: '))
  add = num1 + num2
  print('\n')
  print(num1, '+',  num2, '=',  add)

if calc == 2:
  print('=====MULTIPLICATION CALCULATOR=====\n')
  num1 = int(input('Input your first number: '))
  num2 = int(input('Input your second number: '))
  mul = num1 * num2
  print('\n')
  print(num1, '×', num2, '=', mul)

if calc == 3:
  print('=====SUBSTRACTION CALCULATOR=====\n')
  num1 = int(input('Input your first number: '))
  num2 = int(input('Input your second number: '))
  sub = num1 - num2
  print('\n')
  print(num1, '-', num2, '=', sub)

if calc == 4:
  print('=====DIVISION CALCULATOR=====\n')
  num1 = int(input('Input your first number: '))
  num2 = int(input('Input your second number: '))
  print('\n')
  div = num1 / num2
  print(num1, ':', num2, '=', div)

if calc == 5:
  print('=====EXPONENTIATION CALCULATOR=====\n')
  num1 = int(input('Input your first number: '))
  num2 = int(input('Input your second number: '))
  exp = num1 ** num2
  print('\n')
  print(num1, '^',  num2, '=',  exp)
