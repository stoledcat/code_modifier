input_file = open("input.txt", encoding="utf-8")

# Очистка либо создание файла для сохранения результатов выборки
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
    out_line = ""
    for symbol in new_line:
        if symbol == '"':
            symbol = '\\"'
            out_line += symbol
        else:
            out_line += symbol
    return out_line


# Модифицирование кодов пачек для SQL
def pack_code_sql_modify(input_file):
    count = 0
    output_file = ''
    for string in input_file:
        # Проверка на 29 и 30 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 29 or len(string) == 30) and string[0:6] == "000000":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f"'{replace_quotes_sql(string[:25])}',\n"
            count += 1
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов пачек: {count}.\nРезультат находится в файле 'output.txt'.")
    print("Нажмите Enter.")
    exit = input()
    result.close()


# Модифицирование кодов пачек для JSON
def pack_code_json_modify(input_file):
    count = 0
    output_file = ''
    for string in input_file:
        # Проверка на 29 и 30 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 29 or len(string) == 30) and string[0:6] == "000000":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f'"{replace_quotes_json(string[:25])}",\n'
            count += 1
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов пачек: {count}.\nРезультат находится в файле 'output.txt'.")
    print("Нажмите Enter.")
    exit = input()
    result.close()


# Модифицирование кодов блоков для sql
def bundle_code_sql_modify(input_file):
    count = 0
    output_file = ''
    for string in input_file:
        # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 52 or len(string) == 53) and string[0:5] == "01046":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f"'{replace_quotes_sql(string[0:35])}',\n"
            count += 1
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов блоков: {count}.\nРезультат находится в файле 'output.txt'.")
    print("Нажмите Enter.")
    exit = input()
    result.close()


def bundle_code_json_modify(input_file):
    count = 0
    output_file = ''
    for string in input_file:
        # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) == 52 or len(string) == 53) and string[0:5] == "01046":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f'"{replace_quotes_json(string[0:35])}",\n'
            count += 1
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов блоков: {count}.\nРезультат находится в файле 'output.txt'.")
    print("Нажмите Enter.")
    exit = input()
    result.close()


def operation(choice):
    various = {
        "13": "пачек для SQL",
        "14": "пачек для JSON",
        "23": "блоков для SQL",
        "24": "блоков для JSON"
    }
    return various.get(choice)


# Точка входа, выбор типа модицикации
def main():
    choice = ""
    code_choice = input(
        "Что модифицировать?\n"
        "1 - Коды пачек\n"
        "2 - Коды блоков\n"
        "Выбор: "
    )
    format_choice = input(
        "3 - Для SQL\n"
        "4 - Для JSON\n"
        "Выбор: "
    )
    choice = code_choice + format_choice
    print(f'Выполняется обработка кодов {operation(choice)}.')

    #  проверка корректности ввода данных
    if choice not in ("13", "14", "23", "24"):
        print("Введено неверное значение, повторите ввод.")

    if choice == "13":
        pack_code_sql_modify(input_file)
    elif choice == "14":
        pack_code_json_modify(input_file)
    elif choice == "23":
        bundle_code_sql_modify(input_file)
    elif choice == "24":
        bundle_code_json_modify(input_file)


if __name__ == "__main__":
    main()

input_file.close()
