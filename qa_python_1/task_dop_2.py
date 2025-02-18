# Дополнительное задание. Цифровой корень числа.


def digit_root(num):
    temp_number = 0
    while True:
        while num // 10 > 0:
            temp_number += num % 10
            num //= 10
        temp_number += num
        if temp_number < 10:
            return temp_number
        num = temp_number
        temp_number = 0


print(digit_root(int(input())))
