def prime_numbers(end, start=2):
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, num)):
            print(num, end=" ")

prime_numbers(37, 13)