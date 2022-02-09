import sys

input = sys.stdin.readline

mul = lambda x, y: x * y
div = lambda x, y: x / y
sum = lambda x, y: x + y
sub = lambda x, y: x - y
operators = [mul, div, sum, sub]

operators_mix = []
for first_operator in operators:
    for second_operator in operators:
        for third_operator in operators:
            operators_mix.append([first_operator, second_operator, third_operator])

    operation_oder_mix = [[j, i, 0] for j in range(3) for i in range(2)]

def make_numbers_combination(numbers):
    numbers_combinations = []
    for i in range(4):
        for j in range(3):
            for k in range(2):
                numbers_copy = numbers.copy()
                numbers_combinations.append(
                    [numbers_copy.pop(i), numbers_copy.pop(j), numbers_copy.pop(k), numbers_copy.pop()]
                )
    return list(map(list, set(map(tuple, numbers_combinations))))


def can_make_24(numbers_combination):
    for operators in operators_mix:
        for operation_orders in operation_oder_mix:
            numbers_combination_copy = numbers_combination.copy()
            operators_copy = operators.copy()
            error = False
            for operation_order in operation_orders:
                try:
                    operate_result = operators_copy.pop(operation_order)(
                        numbers_combination_copy.pop(operation_order),
                        numbers_combination_copy.pop(operation_order)
                    )
                except ZeroDivisionError:
                    error = True
                    break
                numbers_combination_copy.insert(operation_order, operate_result)
            if not error and numbers_combination_copy[0] == 24:
                return True
    return False


for _ in range(int(input())):
    yes = False
    numbers = list(map(int, input().strip().split()))
    numbers_combinations = make_numbers_combination(numbers)
    for numbers_combination in numbers_combinations:
        if can_make_24(numbers_combination):
            print("YES")
            yes = True
            break
    if not yes:
        print("NO")
