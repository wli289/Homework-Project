# want: all primes between 2-100
# primes have two factors (1 and itself)
# factor: number % factor == 0

def is_prime(num):
    # check all numbers between 1 and num
    for x in range(2,num):
        if num % x == 0:
            # x is a factor!
            return False
    return True

for x in range(2,100):
    if is_prime(x):
        print x,"prime!"
