# Open File in Read Mode
file_1 = open(r'D:\Labs\python\lab12\file1.txt', 'r')
file_2 = open(r'D:\Labs\python\lab12\file2.txt', 'r')
 
print("Сравнение файлов ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n')
 
file_1_line = file_1.readline()
file_2_line = file_2.readline()
 
# использовать счетчика
line_no = 1
 
print()
 
with open(r'D:\Labs\python\lab12\file1.txt') as file1:
    with open(r'D:\Labs\python\lab12\file2.txt') as file2:
        same = set(file1).intersection(file2)
 
print("Общие строки в обоих файлах")
 
for line in same:
    print(line, end='')
 
print('\n')
print("Разные строки в обоих файлах")
while file_1_line != '' or file_2_line != '':
 
    # Удаление пробелов
    file_1_line = file_1_line.rstrip()
    file_2_line = file_2_line.rstrip()
 
    # Сравните строки из обоих файлов
    if file_1_line != file_2_line:
       
        if file_1_line == '':
            print("@", "Линия-%d" % line_no, file_1_line)
        else:
            print("@-", "Линия-%d" % line_no, file_1_line)
             
        if file_2_line == '':
            print("#", "Линия-%d" % line_no, file_2_line)
        else:
            print("#+", "Линия-%d" % line_no, file_2_line)
 
        # Печатать пустую строку
        print()
 
    # Читать следующую строку из файла
    file_1_line = file_1.readline()
    file_2_line = file_2.readline()
 
    line_no += 1
 
file_1.close()
file_2.close()