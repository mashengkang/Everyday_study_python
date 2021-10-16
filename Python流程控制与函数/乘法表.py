# coding:utf-8

work = {}
# 1
one_value = (1,)
one_key = 1
work[str(one_key)] = one_value
print(work)
# 2
two_key = 2
two_value = []
two_value.append(1)
two_value.append(2)
work[str(two_key)] = two_value
# 3
three_key = 3
three_value = []
three_value.append(1)
three_value.append(2)
three_value.append(3)
work[str(three_key)] = three_value
print(work)
# 4
four_key = 4
four_value = []
four_value.append(1)
four_value.append(2)
four_value.append(3)
four_value.append(4)
work[str(four_key)] = four_value
# 5
temp_five = (1, 2, 3, 4, 5)
five_key = 5
five_value = []
five_value.extend(temp_five)
work[str(five_key)] = five_value
# 6
temp_six = (1, 2, 3, 4, 5, 6)
six_key = 6
six_value = []
six_value.extend(temp_six)
work[str(six_key)] = six_value
# 7
temp_seven = (1, 2, 3, 4, 5, 6, 7)
seven_key = 7
seven_value = []
seven_value.extend(temp_seven)
work[str(seven_key)] = seven_value
# 8
temp_eight = [1, 2, 3, 4, 5, 6, 7, 8]
eight_key = '8'
eight_value = []
eight_value.extend(temp_eight)
work[eight_key] = eight_value
# 9
temp_nine = (1, 2, 3, 4, 5, 6, 7, 8, 9)
nine_key = '9'
nine_value = list(temp_nine)
work[nine_key] = nine_value
print(work)

_keys = work.keys()
keys = list(_keys)
print(keys)

one = keys[0]
one_value = work.pop(one)
one_key = int(one)
print(one_value)  # (1,)
print(f'{one_key} * {one_value[0]} = {one_key*one_value[0]}')

two = keys[1]
two_value = work.pop(two)
two_key = int(two)
print(f'{two_key} * {two_value[0]} = {two_key*two_value[0]}', end=' ')
print(f'{two_key} * {two_value[1]} = {two_key*two_value[1]}')


# 2.
for x in range(1,10):
    for y in range(1, x+1):
        print(f'{x}*{y}={x*y}', end=' ')
    print()