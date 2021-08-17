import random
import string


def passgenerator():
    k = string.ascii_letters + string.digits + '!' + "# " + "&" + "*" + "(" + ")" + "_" + "+" + "?" + ">" + "<"
    size = 8
    return ''.join(random.choice(k) for _ in range(size, 27))


n = 0

while n < 5:
    print(passgenerator())
    n += 1
