def search(sn):
    res_list = []
    with open ("data.txt", "r", encoding = "utf-8") as file:
        while True:
            book = file.readline()
            if not book:
                if not file.readline():
                    break
            if book.rstrip() == sn:
                res_list.append(sn)
                for i in range(1, 4):
                    res_list.append(file.readline().rstrip())
                res_list.append("")
    if len(res_list) > 0:
        return res_list
    return ("Не найдено!")

def export (res):
    with open ("data.txt", 'a', encoding='utf-8') as file:
        for ind in range(4):
            file.write(res[ind] + '\n')
        file.write(res[4])
