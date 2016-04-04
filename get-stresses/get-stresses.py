#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

def getExpectedTranscription(inp):
    '''Ця функція повертає очікувану транскрипцію
    @param input Вхідний рядок з наголосом, наприклад щаве!ль
    @returns Очікувану транскрипцію, наприклад шчаве!л'
    '''

    return inp

class TestExpectedTranscription(unittest.TestCase):

    def performTest(self, pairs):
        for i, o in pairs.items():
            self.assertEqual(o, getExpectedTranscription(i), 'Вхідне слово: "' + i + '"')

    def test_a_basic(self):
        pairs = {
            'ша!пка': 'ша!пка',
        }
        self.performTest(pairs)

    def test_o_basic(self):
        pairs = {
            'вода!': 'вода!',
            'моту!зка': 'моу^ту!зка',
        }
        self.performTest(pairs)

    def test_o_complex(self):
        # не виявляє оу^ однокурсник, бордюр, рвонути, красоту
        pairs = {
            'одноку!рсник': 'о*дноку!рсние^к',
            # Про слова іншомовного походжження словник 2001 не знає... 
            #'бордю!р': 'борд\'ур',
            # Про це також... 
            #'добу!ти': 'добу!ти',
        }
        self.performTest(pairs)

    def test_2001_o_before_stressed_i(self):
        # Увага! Це суперечить словнику Погрібного, проте так зроблено в словнику 2001
        pairs = {
            'порі!г': 'поу^ріг'
        }
        self.performTest(pairs)

    def test_u_basic(self):
        pairs = {
            'кугуа!р': 'кугуа!р',

            # у -> у~
            'аудито!рія': 'ау~дито!рійа',
        }
        self.performTest(pairs)

    def test_i_basic(self):
        pairs = {
            'дід': 'д\'ід',
            'істо!та': 'істо!та',
        }
        self.performTest(pairs)

    def test_i_to_y_1(self):
        pairs = {
            'і!ноді': 'і!и^ноді',
            'і!нколи': 'і!и^нколи',
            'і!нший': 'і!и^нший',
            'і!нде': 'і!и^нде',
        }
        self.performTest(pairs)

    # Немає у 2001
#    def test_i_to_y_2(self):
#        pairs = {
#            'си!ній': 'си!н\'іи^й',
#            'си!нім': 'си!н\'ім',
#            'мої!ми': 'мойі!и^ми',
#            'мої!м': 'мойі!м',
#            'краї!на': 'крайі!и^на'
#        }
#        self.performTest(pairs)

    def test_e_basic(self):
        pairs = {
            'сте!жка': 'сте!жка',
            'епо!ха': 'епо!ха',
            'по!ле': 'по!ле',
            'верба!a': 'веи^рба!',
            'прему!дрий': 'преи^му!дрий',
            'перли!на': 'пеи^рли!на',
            'неді!йсний': 'неи^ді!йсний',
        }
        self.performTest(pairs)

    def test_e_complex(self):
        pairs = {
            'теплоте!хніка': 'те*плоте!хні\'іка',
            'по!лем': 'поле!м',
            'болезаспокі!йливий': 'бо*лезаспок\'і!йлие^вий',
            # 2001 не знає:
            #'вечі!рка': 'вие^ч`і!рка',
        }
        self.performTest(pairs)

    def test_e_to_yi(self):
        pairs = {
            'за!єць': 'за!йі^ц\'',
        }
        self.performTest(pairs)

    def test_y_basic(self):
        pairs = {
            'ти!хо': 'ти!хо',
            'жва!вий': 'жва!вий',
            'прийти!': 'прийти!',
            'до!брих': 'до!брих',
            'роби!ти': 'роби!ти',
            'сидимо!': 'сие^дие^мо!',
            # 2001 не знає:
            #'виде!лка': 'веи^де!лка',
        }
        self.performTest(pairs)

    def test_y_complex(self):
        pairs = {
            'широкоря!дна': 'ши*рокор`а!дна',
            'пʼятиде!нний': 'пйатие^де!н:ий',
        }
        self.performTest(pairs)

    def test_h_to_kh(self):
        pairs = {
            'ле!гкість': 'ле!хкість',
            'сніг': 'сн\'іг',
        }
        self.performTest(pairs)

    def test_w(self):
        pairs = {
            'барв': 'барв',
            'вплив': 'у~плиу~',
            'вино!': 'вино!',
        }
        self.performTest(pairs)

    def test_z(self):
        pairs = {
            'зціли!ти': 'с\'ц\'іли!ти',
            'ка!зка': 'ка!зка',
            'розказа!ти': ('розказа!ти', 'росказа!ти'),
            'безпе!ка': ('беи^зпе!ка', 'беи^спе!ка'),
            # 2001!
            'розси!пати': 'рос:и!пати',
        }
        self.performTest(pairs)

    def test_odzvinchennia(self):
        pairs = {
            'боротьба!': 'бород\'ба!',
            'вокза!л': 'воґза!л',
        }
        self.performTest(pairs)

    def test_dz_dzh(self):
        pairs = {
            'джерело!': 'ДЖерело!',
            'дзеркало!': 'ДЗеркало!',
            # Не в 2001:
            #'віджима!ти': 'в`іДЖжима!ти',
            #'підзві!тний': 'піДЗзв`і!тний'
        }
        self.performTest(pairs)

    def test_mjakyj(self):
        pairs = {
            'лі!кар': 'л\'і!кар',
            'блок': 'блок',

            'ба!лка': 'ба!лка',
            'сип': 'сип',
            'верф': 'верф',
            'ма!ма': 'ма!ма',
            'біб': 'б`іб',
            'під': 'п`ід',
            'він': 'в`ін',
            'мій': 'м`ій',
            'фігура': 'ф`ігура',

            'ги!чка': 'ги!чка',
            'кит': 'кит',
            'хи!трий': 'хи!трий',
            'ґа!ва': 'ґа!ва',
            'гі!рко': 'г`і!рко',
            'хі!ба': 'х`і!ба',
            'ле!ґінь': 'ле!ґ`ін\'',

            'ча!ша': 'ча!ша',
            'джем': 'ДЖем',
            'шар': 'шар',
            'жах': 'жах',
            'о!чі': 'о!ч`і',
            'ло!джія': 'ло!ДЖ`ійа',
            'ші!сть': 'ш`іст\'',
            'жі!нка': 'ж`і!нка',

            'пала!ц': 'пала!ц',
            'ціпо!к': 'ц\'іпок',

            'ра!нок': 'ра!нок',
            'рі!чка': 'р`ічка',

            'дар': 'дар',
            'та!нок': 'та!нок',
            'нара!да': 'нара!да',
            'заграва': 'заграва',
            'сон': 'сон',
            'дзе!ркало': 'дзе!ркало',
            'дід': 'д\'ід',
            'тінь': 'т\'ін\'',
            'ніч': 'н\'іч',
            'зір': 'з\'ір',
            'сім': 'с\'ім',
            'дзьоб': 'дз\'об',
        }
        self.performTest(pairs)

    def test_tverdyj_pered_i(self):
        pairs = {
            'безіме!нний': 'беи^з(^\')^іме!н:й',
            'педінститу!т': 'пе*дінстие^ту!т',
        }
        self.performTest(pairs)

    def test_mjakist_podvijna(self):
        pairs = {
            # Згідно з орфоепічним словником Погрібного, приголосні з групи (з с ДЗ ц н л д т)
            # помʼякшуються перед приголосним з тієї ж групи ...

            'галу!ззя': 'галу!з\':а',
            'зале!жся': 'зале!з\'с\'а',
            'їздці!в': 'йіз\'ДЗ\'ц\'іу~',
            'ни!зці': 'ни!з\'ц\'і',
            'зліт': 'з\'л\'іт',
            'зді!бний': 'з\'д\'і!бний',
            'вро!зтіч': 'у~ро!з\'т\'іч',
            'коло!сся': 'коло!с\':а',
            'ка!сці': 'ка!с\'ц\'і',
            'весля!р': 'вес\'л\'яр',
            'ємні!сть': 'йеи^мні!с\'т\'',
            'наддзьо!бок': 'наДЗ\':о!бок',
            'пфа!льцський': 'пфа!л\'ц\'с\'кий',
            'ворі!тця': 'ворі!т\'ц\'а',
            'мі!цність': 'мі!ц\'н\'іс\'т\'',
            'ги!цля': 'ги!ц\'л\'а',
            'горте!нзія': 'горте!н\'з\'ійа',
            'ано!нсів': 'ано!н\'с\'іу~',
            'ланцю!г': 'ла!н\'ц\'у!г',
            'змага!ння': 'змага!н\':а',
            # нл' згідно 2001-2003
            'фінля!ндський': 'фінл\'а!н\'д\'с\'кий',
            'інді!йка': 'ін\'ді!йка',
            'підґру!нтя': 'підґру!н\'т\'а',
            # крім заволзький; майже всюди мʼякий знак
            'та!волзі': 'та!вол\'з\'і',
            # Знайшов лише кочержилні й рогачилні (решта з мʼяким знаком)
            'кочержи!лні': 'кочеи^ржи!л\'н\'і',
            'ллє!ться': 'л\':е!ц\':а',
            # крім мілдью
            'фа!лді': 'фа!л\'д\'і',
            # Надзвичайно дивний словник:
            # л помʼякшується в балтієць балтійський ґвалті ґвалтівник збольтіть кшталті шталті 
            # проте не помʼякшується в болті болтів ґвалтівни!й прибалті!йський
            # Ну як так можна?..
            'ба!лтієць': 'ба!л\'т\'ійец\'',
            'дні': 'д\'н\'і',
            # д перед л декілька опціонально: задля, підл* ще декілька;
            # Чомусь в "для" "д" твердий
            'відлік': 'відлік',
            #+дд правосуддя
            'су!ддя': 'су!д\':а',
            # опціонально в "підт"
            'звідтіля!': 'з\'в\'ід\'т\'іл\'а!',
            # Теоретично т'c' має переходити в ц':
            # Проте в словнику 2001-2013 для слова вʼяляться чомусь зроблено виняток...
            'вʼяля!ться': 'вйал\'а!т\'с\'а',
            'тлі!ти': 'т\'л\'!іти',
            'життя!': 'жит\':а!',
            
            # Також словник 2001-2003 у "зн", "сн" і "тн"
            # ставить опціональне помʼякшення ...

            'ку!зня': 'ку!з(^\')^н\'а',
            'сніг': 'с(^\')^н\'іг',
            'пу!тній': 'пу!т(^\')^н\'ій',

            # ... А в цт, лц, нДЗ не помʼякшує зовсім.

            'о!цті': 'о!цт\'і',
            'гі!лці': 'г`і!лц\'і',

            # немає в словнику: сз, сДЗ, сд, ДЗз, ДЗс,
            # ДЗн, ДЗл, ДЗд, ДЗт, цз, цДЗ, цд, лс (всюди мʼякий знак),
            # лДЗ (всюди мʼякий знак), дз, дс, дДЗ, дц, тз, тДЗ,
            # тц (обротьці), тд 
        }
        self.performTest(pairs)

    def test_mjakist_vidminky(self):
        # д т з с перед кінцевим мʼяким основи прикметників твердої...
        pairs = {
            'наро!дні': 'наро!д(^\')^н\'і',
            'па!мʼятні': 'па!мйат(^\')^н\'і',
            'о!бразні': 'о!браз(^\')^н\'і',
            # Словник 2001-2003 вважає, що тут помʼякшувати необхідно:
            'барви!сті': 'барви!с\'т\'і',
        }
        self.performTest(pairs)

    def test_double(self):
        pairs = {
            'щаве!ль': 'шчаве!л\'',

            'ярмо!': 'йармо!',
            'ю!шка': 'йу!шка',
            'єди!ний': 'йеи^ди!ний',
            'їжа!к': 'йіжа!к',

            'вʼя!з': 'вйа!з',
            'вʼюно!к': 'вйуно!к',
            'відʼє!мний': 'в`ідйе!мние^й',
            'підʼїзд': 'п\'ідйізд',

            'князь': 'кн\'аз\'',
            'люсте!рко': 'л\'усте!рко',
            'си!нє': 'си!н\'е',
        }
        self.performTest(pairs)

if __name__ == '__main__':
    unittest.main()
