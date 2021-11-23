print('Cho danh sách (list) gồm 10 số nguyên được nhập từ bàn phím (có thể trùng nhau). Hãy tạo một danh sách y lấy các phần tử từ x không trùng nhau. Ghi thêm y vào file f.txt sao cho không làm mất nội dung trước đó của file f.txt')

arr = []

for i in range(10):
    number = int(input(f'Input number {i + 1}: '))
    arr.append(number)

arr = list(set(arr))

with open('f.txt', 'a') as file:
    for num in arr:
        file.write(str(num) + ' ')
