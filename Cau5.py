print('Cho danh sách các số nguyên được nhập từ bàn phím. Trả về True nếu số đầu tiên và số cuối cùng của danh sách giống nhau. Ngược lại, trả về False\n')

string = input('Input your string: ')

if len(string) == 0:
    exit(1)

if string[0] == string[-1]:
    print(True)
else:
    print(False)
