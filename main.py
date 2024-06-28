def main():
    numbers = []

    old = int(input('Enter '))
    numbers.append(old)
    
    while True:
        current = int(input('Enter '))
        if current < old:
            numbers.append(current)
            old = current
        else:
            break

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
