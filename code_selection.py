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


def bundle_code_modify(input_file, choise):
    for string in input_file:
        # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится сивол переноса строки
        if (len(string) >= 52 or len(string) <= 53) and string[0:5] == "01046":
            new_line = string[0:35]
            with open("output.txt", "a+", encoding="utf-8") as result:
                if choise == "1":
                    print(f"'{replace_quotes_sql(new_line)}',", file=result)
                elif choise == "2":
                    print(f"'{replace_quotes_json(new_line)}',", file=result)
    print('Операция модифицирования выполнена')
    result.close()


def main():
    choise = input(
        "Что модифицировать?\n"
        "1 - Коды пачек (для SQL)\n"
        "2 - Коды блоков (для JSON)\n"
        "Выбор: "
    )
    if choise == "1":
        bundle_code_modify(input_file, choise)
    else:
        bundle_code_modify(input_file, choise)
    return choise


if __name__ == "__main__":
    main()

input_file.close()

# FIXME реализовать удаление запятой в последней строке кода
