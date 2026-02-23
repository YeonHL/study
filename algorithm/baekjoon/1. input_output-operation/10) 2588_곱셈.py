import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

num_hundreds = b // 100
num_tens = b // 10 % 10
num_ones = b % 10

result = [a * num_ones, a * num_tens, a * num_hundreds, a * b]

for value in result:
    sys.stdout.writelines(f"{value}\n")
