"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError
    ctr = 2
    while (len(list) < number_of_primes):
        ctr2 = 2
        isPrime = True
        while (ctr2 < ctr):
            if ctr % ctr2 == 0:
                isPrime = False
            ctr2 += 1

        if isPrime:
            list.append(ctr)
        
        ctr+=1

    return list
