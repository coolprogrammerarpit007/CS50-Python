name = input('What is your name: ').capitalize();

# match name:
#   case 'Harry':
#     print('Griffindorr');
#   case 'Hermione':
#     print('Griffindorr');
#   case 'Ron':
#     print('Griffindorr');
#   case 'Draco':
#     print('Slythrin');
#   case _:
#     print('Who');



match name:
  case 'Harry' | 'Hermione' | 'Ron':
    print('Griffindorr');
  case 'Draco':
    print('Slythrin');
  case _:
    print('Who');