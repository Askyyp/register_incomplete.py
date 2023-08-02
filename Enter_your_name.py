name = input('Enter your name: ')
Age = input('Enter your age: ')

if name and Age:
    print(f'His name is {name}')
    print(f'Its inverted name is {name[::-1]}')

    if ' ' in name:
        print('Your name contains spaces')
    else:
        print('Your name does NOT contain spaces')

    print(f'Your name has {len(name)} lyrics')
    print(f'The first letter of his name is {name[0]}')
    print(f'The last letter of his name is {name[-1]}')
else:
    print("Sorry, you left empty fields.")
