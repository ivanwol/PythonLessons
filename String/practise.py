import os


def get_words(file_name):
    with open(file_name, encoding="utf8") as file:  # Открываем файл с изпользованием кодировки
        text = file.read()  # Открывает файл для чтения
    text = text.replace("\n", " ")  # Переводит все строки в одну через пробел
    text = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "")
    text = text.lower()  # Приведенье всех букв к маленьким
    words = text.split()  # Разбивает текст на отд. слова и добавляет их в лист
    words.sort()  # Сортирует слова в листе
    print(words)
    return words


def get_words_dict(words):
    words_dict = dict()  # Создание пустого словаря


    # Проверка на уникальность слова и каунт слов
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():  # Создание главной функции
    file_name = input("Укажите название файла: ")
    if not os.path.exists(file_name):  # Проверка на существование файла
        print("Такого файла не существует")
    else:
        words = get_words(file_name)
        words_dict = get_words_dict(words)
        print(f"Количество слов: {len(words)}")
        print(f"Количество уникальных слов: {len(words_dict)}")
        print("Все использованные слова: ")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":  # Создание блока запуска
    main()