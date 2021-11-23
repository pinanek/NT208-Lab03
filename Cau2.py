print('Cho người dùng nhập vào số nguyên dương n. Sử dụng hàm range() để sinh ra dãy số 0 ≤ x < n , thực hiện tính tổng dãy trên và xuất kết quả ra màn hình\n')

number = 0

while number <= 0:
    number = int(input('Enter your number range: '))

    if number <= 0:
        print('Number must be positive!\n')

print('Sum of your range:', sum(range(number)))
