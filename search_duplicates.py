# BUG разделить проверки пачек и блоков

def pack_duplicates_check(duplicate_check):
    dict_for_duplicates = {}
    line_number = 0
    duplicates_counter = 0
    for j in duplicate_check:
        line_number += 1
        j = j[:29]
        if j not in dict_for_duplicates:
            dict_for_duplicates[j] = 1
        else:
            print(f"\nВ списке кодов присутствует дубликат: {j} ")
            if len(j) >= 29 and len(j) < 35:
                print(
                    f"Номер строки с дубликатом: {line_number}\nКод пачки: {j[15:20]}"
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
