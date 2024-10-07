def difference(number):
    if number <= 17:
        return 17 - number
    else:
        return (number-17) * 2


if __name__ == '__main__':
    num = input("Enter number: ")

    print("difference:", difference(int(num)))
