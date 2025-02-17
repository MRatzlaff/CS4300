# task 3: control structures

# determine if positive, negative, or 0
def what_is_it(num):
    if num > 0:
        result = "+"
    elif num < 0:
        result = "-"
    else: 
        result = "0"

    return result

# find first 10 prime nums using sieve of Eratosthenes
prime_nums = []
def is_prime():
    num = 2
    count = 0
    while count < 10:
        for c in range(2, num):
            if num % c == 0:
                break
        else:
            prime_nums.append(num)
            count += 1
        num += 1
    return prime_nums


# find sum of all nums from 1 to 100
def sum_nums():
    count = 1
    stop = 100
    sum = 0
    while count <= stop:
        sum = sum + count
        count += 1
    return sum
