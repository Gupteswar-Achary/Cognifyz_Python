str = input("Enter a string: ")
reverse = str[::-1]
print('Reversed String is : ', reverse)

if str == reverse:
    print('String is palindrom')
else:
    print('String is not palindrom')