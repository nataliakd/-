def my_cos(x):
    a = 0
    x_pow = x
    fact = 1
    n = 3
    minus = -1
    for i in range(1, n+1):
        fact *= 2*i*(2*i-1)
        a += minus/fact*x_pow
        #a += minus * 1/i
        minus *= -1
        x_pow*=x*x
    print ("a", a)

my_cos(10)
