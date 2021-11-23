print('Cho file input.txt, mỗi dòng là các số nguyên từ 0 đến 10 000 000. Thực hiện đọc những số này và ghi kết quả vào file output.txt\n')


def ReadNumberCharacter(num) -> str:
    switcher = {
        '0': 'không',
        '1': 'một',
        '2': 'hai',
        '3': 'ba',
        '4': 'bốn',
        '5': 'năm',
        '6': 'sáu',
        '7': 'bảy',
        '8': 'tám',
        '9': 'chín'
    }

    return switcher.get(num, 'error')


def ReadTensNumber(num, isReadZero):
    stringNum = str(num)
    lenStringNum = len(stringNum)

    if num == 0:
        return ''

    if lenStringNum == 1:
        if isReadZero:
            return f'lẻ {ReadNumberCharacter(stringNum)}'
        else:
            return ReadNumberCharacter(stringNum)

    if lenStringNum == 2:
        if num == 10:
            return 'mười'

        if stringNum[1] == '0':
            return f'{ReadNumberCharacter(stringNum[0])} mươi'

        else:
            return f'{ReadNumberCharacter(stringNum[0])} mươi {ReadNumberCharacter(stringNum[1])}'


def ReadHundredNumber(num, isReadZero):
    stringNum = str(num)
    lenStringNum = len(stringNum)

    if num == 0:
        return ''

    if lenStringNum < 3:
        if isReadZero:
            return f'không trăm {ReadTensNumber(num, isReadZero)}'

        return ReadTensNumber(num, isReadZero)

    if stringNum[1] == '0' and stringNum[2] == '0':
        return f'{ReadNumberCharacter(stringNum[0])} trăm'

    if stringNum[1] == '0':
        return f'{ReadNumberCharacter(stringNum[0])} trăm lẻ {ReadNumberCharacter(stringNum[2])}'

    return f'{ReadNumberCharacter(stringNum[0])} trăm {ReadTensNumber(stringNum[1:], isReadZero)}'


def ReadNumber(num) -> str:
    stringNum = str(num)
    lenStringNum = len(stringNum)
    isReadZero = lenStringNum > 3

    returnStringNum = ''

    for i in range(0, lenStringNum, 3):
        charNum = num % 1000

        isReadZero = False if num < 1000 else isReadZero

        readHundredNumber = ReadHundredNumber(charNum, isReadZero)

        if readHundredNumber != '':
            if i == 3:
                returnStringNum = f'{readHundredNumber} nghìn {returnStringNum}'

            elif i == 6:
                returnStringNum = f'{readHundredNumber} triệu {returnStringNum}'

            else:
                returnStringNum = f'{readHundredNumber} {returnStringNum}'

        num //= 1000

    return returnStringNum


with open('input.txt', 'r') as file:
    line = file.readline()
    while line:
        lineString = line.strip()
        lenLineString = len(lineString)
        lineNum = int(lineString)

        print(f'Read number {lineNum} : {ReadNumber(lineNum)}')

        line = file.readline()
