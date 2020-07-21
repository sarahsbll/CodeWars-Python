# The Fibonacci numbers are the numbers in the following integer sequence (Fn):

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

# such as

# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

# F(n) * F(n+1) = prod.

# Your function productFib takes an integer (prod) and returns an array:

# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.

# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(m) being the smallest one such as F(m) * F(m+1) > prod.

# Some Examples of Return:
# (depend on the language)

# productFib(714) # should return (21, 34, true),
#                 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

# productFib(800) # should return (34, 55, false),
#                 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
# -----
# productFib(714) # should return [21, 34, true],
# productFib(800) # should return [34, 55, false],
# -----

#  F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
#  F(n) * F(n+1) = prod.
# product means multipliers and dividors
# a series means for the integer 'i' you enter, you get a series of 'i' values
#  def productFib(prod):

#     return

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

# this function returns the fib of the 'i'th value
# f(3)+f(2) = f(2)+f(1)= f(1)+


# print(s8)
# print(len(s8))


def productFib(prod):
    # Fibonnaci Functions
    def fib(i):
        if i == 0:
            return 0
        if i == 1:
            return 1
        else:
            return fib(i - 1) + fib(i - 2)

    # this function returns the first 'i' values of the fibonnaci series
    def fibSerie(j):
        s = []
        for i in range(j):
            s.append(fib(i))
        return s

    sTest = fibSerie(10)

    # Original Function
    for i in range(len(sTest) - 1):
        fibProd = sTest[i] * sTest[i + 1]
        if fibProd == prod:
            res = [sTest[i], sTest[i + 1], "True"]
            break
        if fibProd > prod:
            res = [sTest[i], sTest[i + 1], "False"]
            break
        if fibProd < prod:
            continue
    return res


print(productFib(40))