def fib(terms):
    a, b = 0, 1
    print(f"Here are {terms} terms of fibonacci sequence:")
    print(a, end=' ')
    for i in range(terms-1):
        c = a + b
        print(c, end=' ')
        a = b
        b = c


def main():
    while True:
        n = input("Enter number of terms: ")
        try:
            n = int(n)
            if n <= 0:
                print("Enter a positive integer.")
            else:
                fib(n)
                break
        except ValueError:
            print("Please enter an integer.")


if __name__ == '__main__':
    main()
