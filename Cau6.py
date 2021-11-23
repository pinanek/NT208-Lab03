import random


print(
    'Cho phép người dùng nhập vào số nguyên dương n. Thực hiện sinh ra n số nguyên ngẫu nhiên và in ra màn hình những số nguyên tố trong dãy số vừa sinh ra theo thứ tự tăng dần\n')


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if (num % i == 0):
            return False
    return True


number = 0

while number <= 0:
    number = int(input('Enter your number range: '))

    if number <= 0:
        print('Number must be positive!\n')

arr = random.sample(range(10000), number)

primes = []

for num in arr:
    if (isPrime(num)):
        primes.append(num)

primes.sort()

print('Prime numbers from your range:', primes)
