import os
import time
from datetime import datetime


enter = input("Убедитесь, что исходные коды находятся в файле 'input.txt', затем нажмите Enter\n")

input_file = open("input.txt", encoding="utf-8")

start_time = datetime.now()

# Очистка либо создание файла для сохранения результатов выборки
with open("output.txt", "w", encoding="utf-8") as output:
    output.close()


# Проверка наличия кодов в исходном файле
def check_input_file(count):
    if count == 0:
        print('В файле input.txt не найдено соответствующих кодов.')
        for j in reversed(range(0, 5)):
            time.sleep(1)
        exit()


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
        if (len(string) >= 26 and len(string) <= 30) and string[0:6] == "000000":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f"'{replace_quotes_sql(string[:25])}',\n"
            count += 1
    check_input_file(count)
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов пачек: {count}.\nРезультат находится в файле 'output.txt'.")
    result.close()
    time_spent()


# Модифицирование кодов пачек для JSON
def pack_code_json_modify(input_file):
    count = 0
    output_file = ''
    for string in input_file:
        # Проверка на 29 и 30 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки
        if (len(string) >= 26 and len(string) <= 30) and string[0:6] == "000000":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f'"{replace_quotes_json(string[:25])}",\n'
            count += 1
    check_input_file(count)
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов пачек: {count}.\nРезультат находится в файле 'output.txt'.")
    result.close()
    time_spent()


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
    check_input_file(count)
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов блоков: {count}.\nРезультат находится в файле 'output.txt'.")
    result.close()
    time_spent()


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
    check_input_file(count)
    result.write(output_file[:-2])
    print(f"Операция выполнена. Изменено кодов блоков: {count}.\nРезультат находится в файле 'output.txt'.")
    result.close()
    time_spent()


def operation(choice):
    various = {
        "11": "пачек для SQL",
        "12": "пачек для JSON",
        "21": "блоков для SQL",
        "22": "блоков для JSON"
    }
    return various.get(choice)


# Точка входа, выбор типа модицикации
def main():
    choice = ""
    code_choice = input(
        "Выберите вид кодов:\n"
        "1 - коды пачек\n"
        "2 - коды блоков\n"
        "Выбор: "
    )
    format_choice = input(
        "\nВыберите шаблон для форматирования:\n"
        "1 - для SQL\n"
        "2 - для JSON\n"
        "Выбор: "
    )
    choice = code_choice + format_choice
    #  проверка корректности ввода данных
    if choice not in ("11", "12", "21", "22"):
        print("Введено неверное значение, повторите ввод.")
        exit()
    print(f'Выполняется обработка кодов {operation(choice)}.')

    if choice == "11":
        pack_code_sql_modify(input_file)
    elif choice == "12":
        pack_code_json_modify(input_file)
    elif choice == "21":
        bundle_code_sql_modify(input_file)
    elif choice == "22":
        bundle_code_json_modify(input_file)
    open_this()


def time_spent():
    end_time = datetime.now()
    result_time = end_time - start_time
    print(f'Затраченное время: {str(result_time)[:7]}')


def open_this():
    question = input('Открыть сейчас? y/n: ')
    if question == 'y':
        os.system('output.txt')  # открытие файла в блокноте


if __name__ == "__main__":
    main()

input_file.close()