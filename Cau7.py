print('Cho một chuỗi bất kỳ nhập từ bàn phím, đảo ngược chuỗi trên và xuất ra màn hình. Với các ký tự in thường, chuyển thành in hoa; và ngược lại, chuyển các ký tự in hoa sang in thường\n')

string = input('Input your string: ')

outputString = ''

for c in string:
    numC = ord(c)
    if numC >= 65 and numC <= 90:
        outputString += chr(numC + 32)
    elif numC >= 97 and numC <= 122:
        outputString += chr(numC - 32)
    else:
        outputString += c

print('Reverse string:', outputString[::-1])
