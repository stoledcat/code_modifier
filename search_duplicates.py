"""
pack_duplicates_check - поиск дубликатов среди кодов пачек
bundle_duplicates_check - поиск дубликатов среди кодов пачек

В каждой из функций создается словарь,
куда добавляются проверяемые коды при условии,
что ключ в этом словаре отсутствует. Если же таковой имеется,
возвращается сам код, номер строки с ним,
а также код пачки, либо блока + SKU (в случае с проверкой кодов блоков)
"""

# TODO реализовать запрос на повторную проверку кодов, если будут дубликаты


def pack_duplicates_check(duplicate_check):
    dict_for_duplicates = {}
    line_number = 0
    duplicates_counter = 0
    for code in duplicate_check:
        line_number += 1
        code = code[:21]
        if code not in dict_for_duplicates:
            if code != '':
               if code != '\n':
                   dict_for_duplicates[code] = 1
        else:
            print(f"\nВ списке кодов присутствует дубликат\nКод пачки: {code[14:21]} ")
            print(
                f"Номер строки с дубликатом: {line_number}\n"
            )
            duplicates_counter += 1

    if duplicates_counter != 0:
        input("\nПроверьте список кодов по указанным строкам \
и нажмите Enter для выхода ")
        exit()


def bundle_duplicates_check(duplicate_check):
    dict_for_duplicates = {}
    line_number = 0
    duplicates_counter = 0
    for j in duplicate_check:
        line_number += 1
        j = j[:52]
        if j not in dict_for_duplicates:
            if j != '\n':
               dict_for_duplicates[j] = 1
        else:
            print(f"\nВ списке кодов присутствует дубликат: {j} ")
            if len(j) >= 52:
                print(
                    f"Номер строки с дубликатом: {line_number}\nКод блока: {j[18:25]}\nSKU: {j[44:]}"
                )
                duplicates_counter += 1

    if duplicates_counter != 0:
        input("\nПроверьте список кодов по указанным строкам \
и нажмите Enter для выхода ")
        exit()
