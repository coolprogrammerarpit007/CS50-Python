# Error Catching in Python

# try:
#   x = int(input('Enter Number: ')) 
# except ValueError:
#   print('x is not a number!!')
# else:
#   print(f'Number: {x}')

# while True:
#   try:
#     x = int(input('Enter Value: '))
#   except ValueError:
#     print(f'Invalid Value Error! ')
#   else:
#     break

# print(f'Number is {x}')

def main():
  number = get_int("What's X ?")
  print(f'Number: {number}')


# def get_int():
#   while True:
#     try:
#       x = int(input('Enter value of x: '))
#     except ValueError:
#       print('Value Error, try something new!')
#     else:
#       break
#   return x


def get_int(prompt):
  while True:
    try:
      x = int(input(prompt))
    except ValueError:
      pass
    else:
      break
  return x


main()