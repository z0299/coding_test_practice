k, p, n = map(int, input().split())
"""
n = n*10
def f(p, n):
    if n == 1:
        return p 
    else:
        if (n % 2) == 0:
            return (f(p, n // 2) * f(p, n // 2)) % 1000000007
        else:
            return (f(p, (n-1) // 2) * f(p, (n-1) // 2) * p) % 1000000007

result = f(p, n)
print((k*result) % 1000000007)
"""
print((k*(pow(p, n*10, 1000000007)))%1000000007)
# print(k*((p**(n*10))%1000000007)%1000000007)