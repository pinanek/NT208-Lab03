print('Cho phép người dùng nhập chuỗi ký tự từ bàn phím và số nguyên n. Hiển thị ra màn hình n ký tự cuối cùng trong chuỗi trên\n')

string = input('Input your string: ')
number = int(input('Input your number: '))

if number <= 0:
    exit(1)

printLength = len(string) - number if len(string) > number else 0

print(f'Your last {number} characters: {string[printLength:]}')
