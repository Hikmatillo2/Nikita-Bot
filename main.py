# coding: utf-8
import time
import telebot
import httplib2
from tyan import Chans


class Data:
    def __init__(self):
        self.TOKEN = ''
        self.APP_URL = f'https://yandexbot.herokuapp.com/{self.TOKEN}'
        self.bot = telebot.TeleBot(self.TOKEN)


class Keyboard(telebot.types.ReplyKeyboardMarkup):
    def __init__(self, resize: bool = True, text: list = None):
        super().__init__()
        self.resize_keyboard = resize
        self.text = text
        self.make_keyboard()

    def make_keyboard(self):
        for i in self.text:
            self.add(telebot.types.KeyboardButton(i))


ADMIN_ID = 476893348, 1001606699
bot = Data().bot
co = 0
flag = True
GIRLS_MODE = False

di = {'"Монумент": Ватутина – Блюхера -Титова - Станиславского - Котовского': 'data/4.jpg',
      '"Покрышкина"–Сиб гвардейцев-Вертковская-Станиславского-Титова-Покрышкина.': 'data/5.jpg',
      '"Холодильная" (Д.Ковальчук от Плановой до Ельцовской( мясо-комбината) включая улВладимировская': 'data/43.jpg',
      '"Чистая Слобода" Стартовая': 'data/14.jpg',
      '10/1 Затулинка2. участок:.улицы Зорге,Петухова от Громова до Сиб.Гвардейцев ,плюс ул Паласса,'
      ' ж.м ул Виктора Уса': 'data/11.jpg',
      'Академ-городок Венрхняя зона"Морской проспект"': 'data/48.jpg',
      'Академ-городок Нижняя зона (Демакова,Российская,Иванова,Полевая,Арбузова,Гер.Труда)': 'data/49.jpg',
      'Б. Богаткова (от Кошурникова(Зол.нива) до Лежена включительно)': 'data/32.jpg',
      'Б. Богаткова (отГаранина до Кошурникова Золотой Нивы)': 'data/33.jpg',
      'Богдана Хмельницкого(Народная – Невского (от Калиниского универмага до пересечения с'
      ' Учительской)': 'data/22.jpg',
      'Васхнил Краснообск Стоимость расклейки 2200руб(650шт).независимо от формата': 'data/51.jpg',
      'Волочаевский ж/м (Доватора – Толбухина – ГБШ)': 'data/35.jpg',
      'Гоголя четная сторона(квадрат Гоголя-Кошурникова-Фрунзе-Советская)': 'data/30.jpg',
      'Горский ж/м': 'data/3.jpg',
      'Дуси Ковальчук + Жуковский ж/м (до ул. Северная)(Включая ул.Дачная,Донского,Тимирязева,Плановая,Перевозчикова '
      'Северная)': 'data/21.jpg',
      'Железнодорожный район. (Железнодорожная,1905 года,Челюскинцев,Сибирская,Вокзальная магистраль,Ленина,'
      'Шамшурина)граница справа-пр Димитрова': 'data/18.jpg',
      'Западный ж/м(Забалуева,Невельского,фасадная, КолхидскаяХалтурина,Филатова)': 'data/13.jpg',
      'Затулинка 1часток:улицы .Зорге.Петухова от ул Громова (с не четной стороны в сторону Советского шоссе)до '
      'остановок Полевая, конечная Затулинский жм ,Петухова': 'data/10.jpg',
      'Квадрат Станиславского- Титова-Троллейная- Вертковского': 'data/7.jpg',
      'КвадратСтаниславского-Титова-Троллейная-Широкая': 'data/6.jpg',
      'Кирова- не четная(верхняя)сторона(Шевченковский ж.м.Кирова-Лескова,Никитина-Автогенная)': 'data/38.jpg',
      'Кирова-четная (нижняя)сторона(от Сако и В до Автогенной,Кирова-Зыряновская)': 'data/37.jpg',
      'Ключ-кам плато': 'data/42.jpg',
      'Колывань': 'data/55.jpg',
      'КольцовоСтоимость расклейки 2200руб(600шт) независимо от формата': 'data/50.jpg',
      'Красный проспект - Галущака (квадрат Кр.просп-Писарева-Нарымская) От ст метро Заельцовская'
      ' до Нарымской': 'data/19.jpg',
      'Кубовая (Мочище)400шт. Стоимость расклейки,независимо от формата': 'data/54.jpg',
      'МЖК, (Лазурная,Высоцкого,Татьяны Снежиной)': 'data/36.jpg',
      'Матрешкин двор. Тулинский матр.двор.Просторный Ю-чемской.Шмонина.Сотникова': 'data/17.jpg',
      'Менделеева)': 'data/27.jpg',
      'Мира, Бурденко(включая Беловежскую': 'data/8.jpg',
      'Обь-Гэс': 'data/53.jpg',
      'Первомайский район': 'data/47.jpg',
      'Пл.Калинина - Гор. больница(ул.Медкадры,включая ул.Танковую)': 'data/44.jpg',
      'Проспект Дзержинского (включая Гоголя и Промышленную) плюс треугольник Красина -Кошурникова-пр.Дзерж. ( м '
      '"Березовая роща")': 'data/28.jpg',
      'Пятый м.рСнегири Курчатова,Кр зорь Рассветная': 'data/24.jpg',
      'Станиславский ж/м(350шт)(Немировича Данченко,Ударная)': 'data/16.jpg',
      'Треугольник пр. Маркса – Ватутина - Котовског': 'data/0.jpg',
      'Треугольник. Маркса – Сибиряков Гвардейцев – Немировича-Данченко (плюс улица Тульская)': 'data/1.jpg',
      'Троллейный ж/м (Квадрат Троллейная-Пархоменко Связистов-Широкая(внутри Новосибирская,Киевская)': 'data/15.jpg',
      'Улица Выборная': 'data/41.jpg',
      'Улица Гоголя не четная сторона.(квадрат гоголя - ипподромская-писарева-советская) К этому участку '
      'относятся:1) уч. 1905г-советская-писарева 2) уч. ул. Ипподромская за дк. Строитель.': 'data/29.jpg',
      'Улица Есенина (включая Куприна) (от Никитина до Волочаевской)': 'data/34.jpg',
      'Улица Кропоткина + Плехановский ж/м (от Красного проспекта до ул Светлая)': 'data/20.jpg',
      'Улицы Большевистская - Обская( от бывшей гостинницы Обь до Инструментального завода)': 'data/40.jpg',
      'Улицы Путевая и Планировочная между ул Котовского и ж.дорогой)': 'data/2.jpg',
      'Учительска-Авиастроителей четная.(Республиканская,Нов заря)': 'data/26.jpg',
      'Центр. Границы: Фрунзе-Димитрова-Свердлова-Окт.магистраль-Шамшиных.(центр от Фрунзе до'
      ' авто-вокзала)': 'data/31.jpg',
      'Чемской ж/м,(улицы Комсомольская, Герцена, Кожевникова, Чигорина) Сев.Чемской'
      ' (Аникина-Оловозаводская)': 'data/9.jpg',
      'Четвертый м.р Объединения - Макаренко - Столетова': 'data/23.jpg',
      'Чик,Прокудское 500шт.3500 руб': 'data/56.jpg',
      'Шестой м.рРодники ,Тюленина Кочубуя,Краузе,Земнухова,Родники,Свечникова,Гребенщикова.900ш': 'data/25.jpg',
      'Шлюз': 'data/52.jpg',
      'Юго-Западный ж/м (9гв.дивизии, Связистов, Полтавская, Курганская,Трол-я)': 'data/12.jpg'}


@bot.message_handler(commands=['start'])
def start_message(message):
    id_ = message.chat.id
    global flag, ADMIN_ID

    bot.send_sticker(id_, 'CAACAgIAAxkBAAEEI_diLd85gwqQDLPkqUa9Hc5gei1v6wACaQsAApe62UniP9hNazdftiME')
    bot.send_message(id_, 'Привет, <i>{}</i>, сейчас проверю <b>твою</b> учетку в базе'
                          '.'.format(message.from_user.first_name), parse_mode='html')

    if id_ in ADMIN_ID:
        bot.send_message(id_, 'Добро пожаловать, <i>{}</i>'.format(message.from_user.first_name), parse_mode='html')
        bot.send_message(id_, 'Сейчас появятся <b>кнопки</b> с районами города. Нажми на <b>кнопку</b> -'
                              ' отправлю фотку, все просто',
                         parse_mode='html')
        bot.send_message(message.chat.id, 'Районы города:', reply_markup=Keyboard(True, [i for i in di.keys()]))
    else:
        bot.send_message(id_, 'Добро пожаловать, <i>{}</i>'.format(message.from_user.first_name), parse_mode='html')
        bot.send_message(id_, 'Сейчас появятся <b>кнопки</b> с районами города. Нажми на <b>кнопку</b> -'
                              ' отправлю фотку, все просто',
                         parse_mode='html')
        bot.send_message(message.chat.id, 'Районы города:', reply_markup=Keyboard(True, [i for i in di.keys()]))
        '''bot.send_message(id_, 'К сожалению, тебя нет в базе, выключаюсь...')
        flag = False'''


@bot.message_handler(commands=['chans'])
def announce(message):
    global ADMIN_ID, GIRLS_MODE
    id_ = message.chat.id
    if id_ in ADMIN_ID:
        bot.send_message(id_, 'Привет, какую тянку скинуть?', reply_markup=Keyboard(True, ['Zero Two',
                                                                                           'Albedo', 'Esdeath']))
        GIRLS_MODE = True
    else:
        bot.send_message(id_, 'К сожалению у вас нет прав Администратора для доступа к данному разделу')


@bot.message_handler(content_types=['text'])
def send_text(message):
    global GIRLS_MODE
    if flag:
        if message.text in di.keys():
            bot.send_photo(message.chat.id, photo=open(di[message.text], 'rb'), caption=message.text)
        elif GIRLS_MODE:
            link = ''
            if message.text == 'Albedo':
                link = Chans.get_albedo()
            elif message.text == 'Zero Two':
                link = Chans.get_zerotwo()
            elif message.text == 'Esdeath':
                link = Chans.get_esdeath()
            cache = httplib2.Http(disable_ssl_certificate_validation=True)
            response, content = cache.request(link)
            bot.send_photo(message.chat.id, photo=content, reply_markup=telebot.types.ReplyKeyboardRemove())
            GIRLS_MODE = False
            bot.send_message(message.chat.id, 'Районы города:', reply_markup=Keyboard(True, [i for i in di.keys()]))
        else:
            bot.send_message(message.chat.id, 'Районы города:', reply_markup=Keyboard(True, [i for i in di.keys()]))
        print(message.text, message.from_user.first_name)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(15)
