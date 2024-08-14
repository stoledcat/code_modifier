def find_missing_code():
    missing_codes = ""
    file2 = open("duplicates2.txt", "r", encoding="utf-8").read()
    with open("duplicates1.txt", "r", encoding="utf-8") as file1:
        for string in file1:
            new_string = string.replace('\\"', '"')
            if new_string[35:42] not in file2:
                string = string.strip()
                missing_codes += f"{string.rstrip(',')}\n"
        if missing_codes != "":
            print(f"Отсутствующие блоки (результат сохранен в файл 'missing_codes.txt'): \n{missing_codes}")
        else:
            print("Все блоки на месте.")
    with open("missing_codes.txt", "w", encoding="utf-8") as outfile:
        outfile.write(missing_codes)
    input("Для завершения нажмите Enter ")


if __name__ == "__main__":
    find_missing_code()
