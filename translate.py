# coding: utf-8

def translate():
    language = input('Выберите язык, с которого хотите перевести: ').lower()
    word = input('Введите слово: ').lower()
    previous_line = ''
    with open('ENRUS.TXT') as file:
        for line in file:
            line = line.rstrip('\n')
            string = line.split(', ')
            if len(string) > 1:
                if word in string:
                    if language == 'русский':
                        print(previous_line)
                        return 1
                    else:
                        print(file.readline())
                        return 1
            else:
                if line == word:
                    if language == 'русский':
                        print(previous_line)
                        return 1
                    else:
                        print(file.readline())
                        return 1
            previous_line = line
    return 'Слово не найдено'


translate()
