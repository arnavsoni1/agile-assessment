def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":
    number = 10
    result = factorial(number)
    print(result)