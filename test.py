n = int(input("n+"))
a = n % 10
b = n % 100 // 10
c = n % 1000 // 100
d = n // 1000
print(a + b + c + d)
