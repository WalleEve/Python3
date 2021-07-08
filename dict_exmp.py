def arith_opp(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 // num2

    return add, sub, mult, div


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

rest = arith_opp(num1, num2)

print(rest)

result_set = {'Add: ':rest[0], 'Sub: ':rest[1], 'Mult: ':rest[2], 'Div: ':rest[3]}
print(result_set)
