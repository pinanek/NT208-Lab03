import random

print('Cho 1 list gồm n số nguyên được sinh ngẫu nhiên (n nhập từ bàn phím), hãy ghi các phần tử của list này ra file “f.txt” sao cho:')
print('- Mỗi phần tử nằm riêng lẻ trên 1 dòng')
print('- Dòng dưới sẽ thụt lùi vào trong so với dòng trên 1 dấu cách\n')

number = int(input('Enter your number range: '))

if number < 0:
    exit(-1)

arr = random.sample(range(10000), number)

with open('f.txt', 'w') as file:
    for i in range(number):
        file.write(' '*i + str(arr[i]) + '\n')
