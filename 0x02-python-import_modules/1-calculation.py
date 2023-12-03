#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 10
b = 5

result_add = add(a, b)
result_subtract = sub(a, b)
result_multiply = mul(a, b)
result_divide = div(a, b)

print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_subtract}")
print(f"{a} * {b} = {result_multiply}")
print(f"{a} / {b} = {result_divide}")
