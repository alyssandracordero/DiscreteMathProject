import sys
import GCD

def dialog_helper():
    return(main(input("Numerator:\n"), input("Denominator:\n")))

def main(numerator, denominator):
    gcd = int(GCD.main(int(numerator), int(denominator)))
    return (str(numerator/gcd) + "/" + str(denominator/gcd))

if (len(sys.argv) == 3):
    print(main(int(sys.argv[1]), int(sys.argv[2])))
if (len(sys.argv) == 1):
    print(dialog_helper())
