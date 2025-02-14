# task 3: control structures

def what_is_it(num):
    if num > 0:
        result = "+"
    elif num < 0:
        result = "-"
    else: 
        result = "0"

    return result

def prime_nums():
    primes_list = []
    count = 0
    sieve = 2
    count_max = 10

    # start at 2 because there are no prime numbers lower than 2
    while count < count_max:
        for i in range(2, count_max):
            if(i%sieve != 0):
                primes_list.append(i)
                sieve += 1
                
            count_max += 1

    print(primes_list)

prime_nums()