import math

def karatsuba(x, y):

    if x < 10 and y < 10:
        return x*y

    else:

        n = max(len(str(x)), len(str(y)))
        m = int(math.ceil(float(n)/2))

        x_H = int(math.floor(x/10**m))
        x_L = int(x % (10**m))

        y_H = int(math.floor(y / 10**m))
        y_L = int(y % (10**m))

        s1 = karatsuba(x_H, y_H)
        s2 = karatsuba(x_L, y_L)
        s3 = karatsuba(x_H + x_L, y_H + y_L)
        s4 = s3-s2-s1

        return int(s1*(10**(m*2)) + s4*(10**m) + s2)

        # print(n, m)


        # a = x/10**()
        # b = x%10**(nby2)
        # c = y/10**(nby2)
        # d = y%10**(nby2)
        #
        # ac = karatsuba(a, c)
        # bd = karatsuba(b, d)
        # ad_plus_bc = karatsuba(a+b, c+d) - ac - bd
        #
        # prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        #
        # return prod

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(x, y))
