file = open("input.txt", encoding="utf-8")
line = file.readline
new_list = []
for string in file:
    length_line = len(string)
    # проверка длины строки указана в 53 символа из 52 потому что
    # в строке присутствует символ переноса \n, который считается за +1
    if len(string) == 53 and string[0:5] == "01046":
        new_line = string[0:35]
        with open('output.txt', 'a+', encoding="utf-8") as result:
            print(f'{new_line},', file=result)
