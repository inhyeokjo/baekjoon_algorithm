def f(n):
    print("hello")
    if n == 0:
        return 1
    return f(n // 2) + f(n // 2)+1



print(f(4))
