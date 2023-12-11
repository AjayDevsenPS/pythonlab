def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def series_sum(n):
    result = 0
    for i in range(1, n + 1):
        term = (i ** 3) / factorial(i)
        result += term
    return result

n = int(input("Enter the number of terms in the series: "))

result = series_sum(n)
print("Sum of the series 1/1!+4/4!+21/3!+..to the",n,"th term is:", result)
