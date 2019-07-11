import sys

'''
I have an idea.
	Joey's Theorum:			For all n in positive integers, all divisors of n <= n/2 and n
	Prime Factorization Theorum:	For all n in positive integers, all prime factors of n <
					square-root(n)
'''

def main(x):
    divisors = []
    for n in range(1,x+1):
        #Checks if n is inclusively a divisor of x
        if (x%n == 0):
            if n in divisors:
                 continue
            else:
                divisors.append(int(n))
                divisors.append(int(x/n))
    divisors.sort()
    return divisors


if (len(sys.argv) != 2):
    raise Exception("Program requires 1 arguement.")
number = int(sys.argv[1])
if (number < 1):
    raise Exception("Argument is less than one.")
print(main(number))
