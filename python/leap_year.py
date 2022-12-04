leap_year = 2018

is_divisible_for_4 = True if leap_year % 4 == 0 else False

is_divisible_for_100 = True if leap_year % 100 == 0 else False

is_divisible_for_400 = True if leap_year % 400 == 0 else False

print(is_divisible_for_4, is_divisible_for_100, is_divisible_for_400)


if is_divisible_for_4 and is_divisible_for_100 and is_divisible_for_400:
    print('leap year 1')

elif is_divisible_for_4 and not is_divisible_for_100:
    print('leap year 2')

elif not is_divisible_for_4:
    print('not leap year 1')

elif is_divisible_for_4 and is_divisible_for_100 and not is_divisible_for_400:
    print('not leap year 2')




