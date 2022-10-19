from dataclasses import replace
from math import pi
# #task1
# d = int(input("Задайте точность для d: "))
# print(f"Число пи равно {round(pi, d)}")

# #task2
# def is_simple(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def dividers(n):
#     dividers = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             dividers.append(i)
#     return (list(filter(is_simple, dividers)))

# print(dividers(835329))

# #task3
# l = [1, 56, 45, 45, 89, 9045, 1, 543]
# def no_coincidence(l):
#     return list(set(l))
# print(no_coincidence(l))

#task4
import random
def create_polinomial():
    k = int(input("Задайте k: "))
    coefficients = []
    for i in range(k, -1, -1):
        memory_coef = ""
        coef = str(random.randint(0, 100))
        polinom = f" * x^{i}"
        if coef == "0":
            continue
        if i == 0:
            polinom = ""
        if i == 1:
            polinom = polinom[:4]
        if coef == "1":
            memory_coef = coef
            coef = ""
            polinom = polinom[3:]
        if memory_coef == "1" and i == 0:
            coef = "1"
        coefficients.append(coef + polinom)
    return (" + ".join(coefficients) + " = 0")

# def add_polinomial_to_file(s):
#     with open(s, "w") as f:
#         f.write(create_polinomial() + "\n")
# add_polinomial_to_file("polies.text")

def create_new_file_and_polynomial(s, s1, new_file):
    with open(s, "r") as f, open(s1, "r") as f1, open(new_file, "w") as new_file:
        poly1 = f.readlines()
        poly2 = f1.readlines()
        print(poly1)
        new_poly = poly1[0][:-4] + "+ " + poly2[0]
        new_file.write(new_poly)
create_new_file_and_polynomial("polies.text", "polies2", "sum_of_polies")