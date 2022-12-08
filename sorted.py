with open('1.txt', encoding='utf-8') as fp1, open('2.txt', encoding='utf-8')\
        as fp2, open('3.txt', encoding='utf-8') as fp3:
    one_list = fp1.readlines()
    two_list = fp2.readlines()
    three_list = fp3.readlines()


new = [one_list, two_list, three_list]


while len(new) != 0:
    short_new = min(new, key=len)
    with open('10.txt', 'a', encoding='utf-8') as file:
        if short_new != two_list and short_new != three_list:
            file.write('1.txt' + '\n')
            file.write(str(f'Количество строк в файле {len( short_new)}' + '\n'))
        if short_new != one_list and short_new != three_list:
            file.write('2.txt' + '\n')
            file.write(str(f'Количество строк в файле {len( short_new)}' + '\n'))
        if short_new != one_list and short_new != two_list:
            file.write('\n' + '3.txt' + '\n')
            file.write(str(f'Количество строк в файле {len( short_new)}' + '\n'))
        file.writelines(short_new)
    new.remove(min(new, key=len))
