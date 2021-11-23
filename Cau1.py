print('Cho người dùng nhập vào hai số nguyên và trả về tích của chúng. Nếu kết quả lớn hơn 1000 thì trả về tổng của chúng\n')

number1 = int(input('Enter your first number: '))
number2 = int(input('Enter your second number: '))

sum = number1 + number2

if sum > 1000:
    print('Sum of 2 number', sum)
