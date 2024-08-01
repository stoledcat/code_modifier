def compare_files():
    infile1 = open("duplicates1.txt", "r", encoding="utf-8").readlines()
    infile2 = open("duplicates2.txt", "r", encoding="utf-8").readlines()
    if infile1 > infile2:
        delete_duplicates(infile1, infile2)
    else:
        delete_duplicates(infile2, infile1)


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
