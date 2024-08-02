import os
import time
from datetime import datetime
import pyperclip
from search_duplicates import bundle_duplicates_check, pack_duplicates_check


input_file = open("input.txt", encoding="utf-8")
duplicate_check = open("input.txt", encoding="utf-8")

start_time = datetime.now()

# очистить либо создать файл для сохранения результатов выборки
with open("output.txt", "w", encoding="utf-8") as output:
    output.close()


# проверить наличие кодов в исходном файле
def check_input_file(count):
    if count == 0:
        print("В файле input.txt не найдено соответствующих кодов.")
        for t in reversed(range(0, 5)):
            time.sleep(1)
        exit()


# экранировать кавычки для SQL
def replace_quotes_sql(new_line):
    out_line = ""
    for symbol in new_line:
        if symbol == "'":
            symbol = "''"
            out_line += symbol
        else:
            out_line += symbol
    return out_line


# экранировать кавычки для json
def replace_quotes_json(new_line):
    out_line = ""
    for symbol in new_line:
        if symbol == '"':
            symbol = '\\"'
            out_line += symbol
        else:
            out_line += symbol
    return out_line


# модифицировать коды пачек для SQL
def pack_code_sql_modify(input_file):
    count = 0
    output_file = ""
    for string in input_file:
        string = string.strip()
        # Проверка идет до 30 символов, потому что иногда при выгрузке кодов
        # не ставится символ переноса строки, либо ставятся пробелы
        if (len(string) >= 21 and len(string) <= 30) and string[0:6] == "000000":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f"'{replace_quotes_sql(string[:25])}',\n"
            count += 1
    check_input_file(count)
    result.write(output_file[:-2])
    print(
        f"Операция выполнена. Изменено кодов пачек: {count}. \n\
Результат находится в файле 'output.txt'."
    )
    result.close()
    time_spent()


# модифицировать коды пачек для JSON
def pack_code_json_modify(input_file):
    count = 0
    output_file = ""
    for string in input_file:
        string = string.strip()
        # Проверка идет до 30 символов, потому что иногда при выгрузке кодов
        # не ставится символ переноса строки, либо ставятся пробелы
        if (len(string) >= 21 and len(string) <= 30) and string[0:6] == "000000":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f'"{replace_quotes_json(string[:25])}",\n'
            count += 1
    check_input_file(count)
    result.write(output_file[:-2])
    print(
        f"Операция выполнена. Изменено кодов пачек: {count}. \n\
Результат находится в файле 'output.txt'."
    )
    result.close()
    time_spent()


# модифицировать коды блоков для sql
def bundle_code_sql_modify(input_file):
    count = 0
    output_file = ""
    for string in input_file:
        string = string.strip()
        # Проверка на 35 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки, либо ставятся пробелы
        if (len(string) >= 35 or len(string) == 53) and string[0:5] == "01046":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f"'{replace_quotes_sql(string[0:35])}',\n"
            count += 1
    check_input_file(count)
    result.write(output_file[:-2])
    print(
        f"Операция выполнена. Изменено кодов блоков: {count}. \n\
Результат находится в файле 'output.txt'."
    )
    result.close()
    time_spent()


def bundle_code_json_modify(input_file):
    count = 0
    output_file = ""
    for string in input_file:
        string = string.strip()
        # Проверка на 35 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится символ переноса строки, либо ставятся пробелы
        if (len(string) >= 35 or len(string) == 53) and string[0:5] == "01046":
            result = open("output.txt", "a+", encoding="utf-8")
            output_file += f'"{replace_quotes_json(string[0:35])}",\n'
            count += 1
    check_input_file(count)
    result.write(output_file[:-2])
    print(
        f"Операция выполнена. Изменено кодов блоков: {count}. \n\
Результат находится в файле 'output.txt'."
    )
    result.close()
    time_spent()


def operation(choice):
    various = {
        "11": "пачек для SQL",
        "12": "пачек для JSON",
        "21": "блоков для SQL",
        "22": "блоков для JSON",
    }
    return various.get(choice)


# точка входа, выбор типа модицикации
def main():
    if select_operation() == "1":
        compare_files()
    else:
        modify_code(input_file)


def modify_code(input_file):
    choice = ""
    code_choice = input(
        "Выберите вид кодов:\n" "1 - коды пачек\n" "2 - коды блоков\n" "Выбор: "
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
    print(f"Выполняется обработка кодов {operation(choice)}.")

    if choice == "11":
        pack_duplicates_check(duplicate_check)
        pack_code_sql_modify(input_file)
    elif choice == "12":
        pack_duplicates_check(duplicate_check)
        pack_code_json_modify(input_file)
    elif choice == "21":
        bundle_duplicates_check(duplicate_check)
        bundle_code_sql_modify(input_file)
    elif choice == "22":
        bundle_duplicates_check(duplicate_check)
        bundle_code_json_modify(input_file)
    open_this()


def time_spent():
    end_time = datetime.now()
    result_time = end_time - start_time
    print(f"Затраченное время: {str(result_time)[:7]}")


# выбрать действие с результатом обработки файла
def open_this():
    question = input(
        "\n1 - открыть файл\n" "2 - скопировать результат в буфер обмена\n" "Выбор: "
    )
    if question == "1":
        os.system("output.txt")
    elif question == "2":
        with open("output.txt", "r", encoding="utf-8") as result:
            clipboard = result.read()
            pyperclip.copy(clipboard)
    else:
        print("Неверный выбор")


# выбрать действия при запуске программы
def select_operation():
    choice = input(
        "Выберите операцию:\n\
1 - удалить дубликаты\n\
2 - модифицировать коды\n\
Выбор: "
    )
    return choice


# сравнить два файла с кодами
# выбрать больший из них, из которого будут удалены коды другого файла
def compare_files():
    infile1 = open("duplicates1.txt", "r", encoding="utf-8").readlines()
    infile2 = open("duplicates2.txt", "r", encoding="utf-8").readlines()
    if infile1 > infile2:
        delete_duplicates(infile1, infile2)
    else:
        delete_duplicates(infile2, infile1)


# удалить дубликаты
# по факту дубликаты не будут добавлены в новую переменную с корректными кодами
# новые коды в итоге записываются в выходной файл
def delete_duplicates(file1, file2):
    result = ""
    tempfile = ""
    for line in file2:
        if line != "\n":
            tempfile += line.strip() + "\n"
    for line in file1:
        line = line.strip()
        if line not in tempfile:
            if line not in result:
                result += str(line) + "\n"
    outfile = set_outfile()
    outfile.write(result)
    if outfile.name == "input.txt":
        modify_code(input_file)


# запросить, в какой файл будет сохранен результат обработки
def set_outfile():
    print("В какой файл сохранить коды?")
    set_file = input(
        '1 - "input.txt" (для дальнейшей обработки)\n2 - "result.txt"\n\
Выбор: '
    )
    if set_file == "1":
        outfile = open("input.txt", "w", encoding="utf-8")
    else:
        outfile = open("result.txt", "w", encoding="utf-8")
    return outfile


if __name__ == "__main__":
    main()

input_file.close()
