input_file = open("input.txt", encoding="utf-8")

choise = input('Что модифицировать?\n'
               '1 - Коды блоков\n'
               '2 - коды пачек\n'
               'Выбор: ')


# BUG Не отрабатывает запуск функции "bundle_code_modify"
def run_choise(choise):
    if choise == '1':
        bundle_code_modify(input_file)
    else:
        print('Неверный выбор')


def replace_quotes_sql(new_string):
    out_string = ""
    for symbol in new_string:
        if symbol == "'":
            symbol = "''"
            out_string += symbol
        else:
            out_string += symbol
    return out_string


def replace_quotes_json(new_string):
    out_string = ''
    for symbol in new_string:
        if symbol == '"':
            symbol = '\\"'
            out_string += symbol
        else:
            out_string += symbol
    return out_string


# BUG не отрабатыает запуск этой функции
def bundle_code_modify(input_file):
    for string in input_file:
        # Проверка на 52 и 53 символа идет потому что иногда при выгрузке кодов
        # не ставится сивол переноса строки
        if (len(string) >= 52 or len(string) <= 53) and string[0:5] == "01046":
            new_line = string[0:35]
            with open("output.txt", "a+", encoding="utf-8") as result:
                print(f"'{replace_quotes(new_line)}',", file=result)
    result.close()


input_file.close()
# result.close()

# FIXME реализовать удаление запятой в последней строке кода
