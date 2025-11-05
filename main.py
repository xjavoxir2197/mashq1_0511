# 1 - misol
sonlar = [4, 9, 16, 25, 36]
res = [son ** 0.5 for son in sonlar]
print(res)

# 2 - misol
sonlar = range(0, 51)
res = [son for son in sonlar if son % 5 == 0]
print(res)

# 3 - misol
words = ["hello", "world", "python"]
words = [word.upper() for word in words]
print(words)

# 4 - misol
words = ["car", "bike", "bus"]
res = [word[::-1] for word in words]
print(res)

# 5 - misol
sonlar = [1, 2, 3, 4]
res = [son * 2 for son in sonlar]
print(res)
