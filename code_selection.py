# FIXME реализовать удаление запятой в последней строке кода


input_file = open("input.txt", encoding="utf-8")

#  Очистка либо создание файла для сохранения результатов выборки
with open("output.txt", "w", encoding="utf-8") as output:
    output.close()


# Экранирование кавычек для SQL
def replace_quotes_sql(new_line):
    out_line = ""
    for symbol in new_line:
        if symbol == "'":
            symbol = "''"
            out_line += symbol
        else:
            out_line += symbol
    return out_line


# Экранирование кавычек для json
def replace_quotes_json(new_line):
    out_line = ''
    for symbol in new_line:
        if symbol == '"':
            symbol = '\\"'
            out_line += symbol
        else:
            out_line += symbol
    return out_line


# CHECK # Модифицирование кодов пачек для SQL
def pack_code_sql_modify(input_file):
    count = 0
    for string in input_file:
        # Проверка на 29 и 30 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 29 or len(string) == 30) and string[0:6] == "000000":
            new_line = string[0:25]
            with open("output.txt", "a+", encoding="utf-8") as result:
                print(f"'{replace_quotes_sql(new_line)}',", file=result)
            count += 1
    print(f"Операция выполнена. Изменено кодов пачек: {count}.")
    result.close()


# CHECK # Модифицирование кодов пачек для JSON
def pack_code_json_modify(input_file):
    count = 0
    for string in input_file:
        # Проверка на 29 и 30 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 29 or len(string) == 30) and string[0:6] == "000000":
            new_line = string[0:25]
            with open("output.txt", "a+", encoding="utf-8") as result:
                print(f'"{replace_quotes_json(new_line)}",', file=result)
            count += 1
    print(f"Операция выполнена. Изменено кодов пачек: {count}.")
    result.close()


# CHECK Модифицирование кодов блоков для sql
def bundle_code_sql_modify(input_file):
    count = 0
    for string in input_file:
        # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 52 or len(string) == 53) and string[0:5] == "01046":
            new_line = string[0:35]
            with open("output.txt", "a+", encoding="utf-8") as result:
                print(f"'{replace_quotes_sql(new_line)}',", file=result)
            count += 1
    print(f"Операция выполнена. Изменено кодов блоков: {count}.")
    result.close()


# CHECK # Модифицирование кодов блоков для json
def bundle_code_json_modify(input_file):
    count = 0
    for string in input_file:
        # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 52 or len(string) == 53) and string[0:5] == "01046":
            new_line = string[0:35]
            with open("output.txt", "a+", encoding="utf-8") as result:
                print(f"'{replace_quotes_json(new_line)}',", file=result)
            count += 1
    print(f"Операция выполнена. Изменено кодов блоков: {count}.")
    result.close()


#  Точка входа, выбор типа модицикации
def main():
    choise = ""
    code_choise = input(
        "Что модифицировать?\n"
        "1 - Коды пачек\n"
        "2 - Коды блоков\n"
        "Выбор: "
    )
    if code_choise != "1" or code_choise != "2":
        print("Введено неверное значение, повторите ввод.")
    format_choise = input("3 - Для SQL\n"
                          "4 - Для JSON\n"
                          "Выбор: ")
    if format_choise != "3" or format_choise != "4":
        print("Введено неверное значение, повторите ввод.")

    choise = code_choise + format_choise
    if choise == "13":
        pack_code_sql_modify(input_file)
    elif choise == "14":
        pack_code_json_modify(input_file)
    elif choise == "23":
        bundle_code_sql_modify(input_file)
    elif choise == "24":
        bundle_code_json_modify(input_file)


if __name__ == "__main__":
    main()

input_file.close()
