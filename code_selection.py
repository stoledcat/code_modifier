# FIXME реализовать удаление запятой в последней строке кода


input_file = open("input.txt", encoding="utf-8")

#  Очистка либо создание файла для сохранения результатов выборки
with open("output.txt", "w", encoding="utf-8") as output:
    output.close()


# Экранирование кавычек в кодах пачек для SQL-запросов
def replace_quotes_sql(new_line):
    out_line = ""
    for symbol in new_line:
        if symbol == "'":
            symbol = "''"
            out_line += symbol
        else:
            out_line += symbol
    return out_line


# Экранирование кавычек в кодах блоков для json-отчетов
def replace_quotes_json(new_line):
    out_line = ""
    for symbol in new_line:
        if symbol == '"':
            symbol = '\\"'
            out_line += symbol
        else:
            out_line += symbol
    return out_line


# Модифицирование кодов пачек
def pack_code_modify(input_file):
    count = 0
    for string in input_file:
        # Проверка на 29 и 30 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 29 or len(string) == 30) and string[0:6] == "000000":
            new_line = string[0:25]
            with open("output.txt", "a+", encoding="utf-8") as result:
                print(f"'{replace_quotes_sql(new_line)}',", file=result)
            count += 1
    print(f'Операция выполнена. Изменено кодов пачек: {count}.')
    result.close()


# Модифицирование кодов блоков
def bundle_code_modify(input_file):
    count = 0
    for string in input_file:
        # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 52 or len(string) == 53) and string[0:5] == "01046":
            new_line = string[0:35]
            with open("output.txt", "a+", encoding="utf-8") as result:
                print(f"'{replace_quotes_json(new_line)}',", file=result)
            count += 1
    print(f'Операция выполнена. Изменено кодов блоков: {count}.')
    result.close()


#  Точка входа, выбор типа модицикации файлов
def main():
    choise = input(
        "Что модифицировать?\n"
        "1 - Коды пачек (для SQL)\n"
        "2 - Коды блоков (для JSON)\n"
        "Выбор: "
        )
    if choise == "1":
        pack_code_modify(input_file)
    elif choise == "2":
        bundle_code_modify(input_file)
    else:
        print("Введено неверное значение, повторите ввод.")


if __name__ == "__main__":
    main()

input_file.close()
