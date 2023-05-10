def josephusProblem(n, k) -> int:
    if n == 1:
        return 1
    else:
        return ((josephusProblem(n - 1, k) + k - 1) % n) + 1

n, k = input("Enter n and k separated by a space to calculate the safe spot for the josephus problem\n").split()
n, k = int(n), int(k)
x = josephusProblem(n, k)
print("Safe spot is ", x)
