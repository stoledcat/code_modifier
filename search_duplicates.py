# input_file = [
#     '01046200657008042132mhd;U800519700093N/UE24016142738',
#     '010462006570080421ooB/sE+800519700093/7fB24016142738',
#     '0104620065700804216gvYc/z800519700093Bbgn24016142738',
#     '010462006570080421ooB/sE+800519700093/7fB24016142738',
#     '0104620065700804216gvYc/z800519700093Bbgn24016142738'
#     ]

# TODO завершить объединение двух файлов программы


def search_duplicates(input_file):
    dict_for_duplicates = {}
    line_number = 0
    duplicates_counter = 0
    for j in input_file:
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
        input("\nПроверьте список кодов и нажмите Enter для выхода ")
        exit()

    # for j in reversed(range(0, 5)):
    #     time.sleep(1)
    # exit()


# search_duplicates(input_file)

