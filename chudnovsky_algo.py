import decimal
import time
from colorama import Fore, Back


def binary_split(a, b):
    if b == a + 1:
        if a == 0:
            Pab, Qab = 1, 1
        else:
            Pab = -(6*a - 5)*(2*a - 1)*(6*a - 1)
            Qab = 10939058860032000 * a ** 3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)

        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky(n):
    P0n, Q0n, R0n = binary_split(0, n)
    return (426880 * decimal.Decimal(10005).sqrt() * Q0n) / R0n


with open(r"pipi.txt", "r") as dta: # Enter the Pi path here
    pi = str(dta.read())


n = int(input("> "))
decimal.getcontext().prec = 69 + 15*n
start = time.time()
PI = chudnovsky(n)
end = time.time()
PI = str(PI)

for i, j in enumerate(PI):
    if j == pi[i]:
        pass
    else:
        print(Fore.GREEN + str(pi[:i+1:]), end="")
        print(Fore.RED + str(PI[i+2::]))
        print(f"Correct Digits: {i+1},    Time Taken: {(end-start):.3f}")
        break
exit()
