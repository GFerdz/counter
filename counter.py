import os


def line_counter(file_name):
    """Функция для подсчёта строк в файле.
    :param file_name: путь до текстового файла в типе str
    :return: подсчитанное количество строк в типе int
    """
    with open(file_name, encoding='utf8') as file:
        count_line = 0
        for _ in file:
            count_line += 1
    return count_line


def get_words(file_name):
    """Функция для преобразования в отсортированный и отчищенный от
    некоторых знаков препинания список. Удаляются некоторые знаки препинания

    :param file_name: путь до текстового файла в типе str
    :return: список строк, отфильтрованый от
    переноса строк и знаков препинания: , . ! ?
    Так же - убираются круглые скобки.
    """
    with open(file_name, encoding='utf8') as file:
        text = file.read()
    text = text.replace('\n', ' ').replace('(', ' ')\
        .replace(')', ' ')
    text = text.replace(',', '').replace('.', '')\
        .replace('!', '').replace('?', '')
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    """Функция для формирования словоря из списка.
       Считает количество повторяющихся слов.

    :param words: список из строк
    :return: словарь. ключ - слово,
    значение - количество повторений слова.
    """
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    """ Функция для работы с пользователем.
        Запрашивает путь к файлу и выводит
        в консоль информацию   """
    filename = input('путь к файлу: ')
    if not os.path.exists(filename):
        print('Файл не наден.')
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print('Количество строк: %d' % line_counter(filename))
        print('Количество слов: %d' % len(words))
        print('Количество уникальных слов: %d' % len(words_dict))
        print('Все использованные слова: ')
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == '__main__':
    main()
