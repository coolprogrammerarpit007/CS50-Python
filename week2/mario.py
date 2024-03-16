# print('Hello Mario');

# def main():
#   print_columns(3);

# def print_columns(height):
#   for _ in range(height):
#     print('#');


# def main():
#   print_rows(4);

# def print_rows(length):
#     print('?'*length,end='');

# main();


def main():
  size = int(input('Enter Grid Size: '))
  print_square(size)

def print_square(size):
  # for each row in grid
  for row in range(size):
    # for each Brick in row
    for col in range(size):
      # print brick
      print("$",end="")
    print()

main()