print('Hãy đọc file “f.txt” trong bài trên và xuất ra màn hình biểu thức phép tính cộng và tổng của chúng của các số có trong file\n')

fileSum = 0

with open('f.txt', 'r') as file:
    line = file.readline()
    while line:
        numString = line.strip()
        fileSum += int(numString)
        line = file.readline()

print('Sum of f.txt file:', fileSum)
