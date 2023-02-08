
def inp_mod():
    mod = input("Введите режим работы (импорт/экспорт): ")
    return mod

def inp_import():
    surename = input("Введите фамилию: ")
    return surename

def view_import(result):
    print(*result, sep="\n")

def inp_export():
    surename = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    type = input("Введите описание: ")
    return "\n", surename, name, phone, type


def view_import_no():
    print(f"По вашему запросу данные не найдены!")


def view_export():
    print("Данные успешно сохранены!")