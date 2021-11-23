print(' Hãy chèn thêm dòng chữ “Lập trình ứng dụng WEB” (viết Tiếng Việt, có dấu) vào cuối file “f.txt” mà không làm mất nội dung trước đó của file f. (khi mở file f lên phải đọc được Tiếng Việt có dấu)\n')

with open('f.txt', 'ab') as file:
    file.write('Lập trình ứng dụng WEB\n'.encode('utf8'))
