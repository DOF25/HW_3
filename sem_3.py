#Task1
l = [2, 3, 5, 6]
def odd_sum(l):
    sum = 0
    for i in range(len(l)):
        if i % 2 != 0:
            sum += l[i]
    return sum

print(odd_sum(l))

#task2
import math
def couple(l):
    result = []
    half = int(len(l) / 2)
    if len(l) % 2 != 0: 
        half = math.ceil(len(l) / 2)       
    for _ in range(half):
        multiplication = l[0] * l[-1]
        result.append(multiplication)
        l = l[1:-1]
    return result
print(couple(l))

#task3
d = [1.1, 1.2, 3.1, 5, 10.01]
def fractional_part_difference(l):
    fractional_parts = []
    for i in l:
        str_number = str(i)
        if "." in str_number:
            str_number = "0" + str_number[str_number.find("."):]
            fractional_parts.append(float(str_number))
    return(max(fractional_parts) - min(fractional_parts))
print(fractional_part_difference(d))

#task4
def to_binary(n):
    result = ""
    while n != 0:
        remainder = n % 2
        result += str(remainder)
        n //= 2
    return result[::-1]
print(to_binary(2))

#task4
def list_fibo(n):
    fibo = [0, 1]
    for i in range(2, n + 1):
        elem = fibo[i-1] + fibo[i - 2]
        fibo.append(elem)
    negative_fibo = []
    for i in range(len(fibo)):
        elem = (-1) ** (i + 1) * fibo[i]
        negative_fibo.append(elem)
    negative_fibo.reverse()
    return (negative_fibo[:-1] + fibo)
print(list_fibo(8))