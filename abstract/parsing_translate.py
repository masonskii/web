import json
from pathlib import Path


class ParsingTranslate:
    @staticmethod
    def open_file(type_language=0):
        """
        Парсинг json файла для выбора языка кодировки страницы
        :param type_language: Номерной код языка. Для английского 0, для русского 1
        :return:
            список данных с выбранным языком
        :Example:
            data = ParsingTranslate.open_file(1)

            return render (request, ..., { 'translate': data}
        """
        """if type_language >= 2 or type_language <= -1:
            raise ValueError('Type Language is not corrected. Input successfully number code language')"""
        BASE_DIR = Path(__file__).resolve().parent.parent
        STANDART_PATH = '{0}/assets/translate/'.format(BASE_DIR)

        if type_language == 0:
            STANDART_PATH = STANDART_PATH + '{0}'.format('eng.json')
        if type_language == 1:
            STANDART_PATH = STANDART_PATH + '{0}'.format('rus.json')

        with open(STANDART_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not data:
                raise ValueError("File is empty")
            else:
                json.dumps(data, ensure_ascii=False, sort_keys=False, indent=4)
                return data
