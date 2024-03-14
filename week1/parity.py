

# if(x%2 == 0):
#   print('Even Number');
# else:
#   print('Odd Number');


# using functions

def main():
  x = int(input('Enter value of x: '));
  isEven = checkEven(x);
  return isEven;


def checkEven(num):
  if(num % 2 == 0):
    return 1;
  return 0;

isEven = main();
print('Even' if isEven else 'Odd'); # Ternary Operator