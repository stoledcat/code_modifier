input_file = open("input.txt", encoding="utf-8")


def replace_quotes(new_string):
    out_string = ""
    for symbol in new_string:
        if symbol == "'":
            symbol = "''"
            out_string += symbol
        else:
            out_string += symbol
    return out_string


for string in input_file:
    # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
    # не ставится символ переноса строки
    if (len(string) >= 52 or len(string) <= 53) and string[0:5] == "01046":
        new_line = string[0:35]
        with open("output.txt", "a+", encoding="utf-8") as result:
            print(f"'{replace_quotes(new_line)}',", file=result)


input_file.close()
result.close()

# TODO реализовать удаление запятой в последней строке кода
