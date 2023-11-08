from aiogram.utils import markdown
from string import Template

from ...constants import DATA_DIR


welcome = "Добро пожаловать, в таро бот созданный Анной Пьерс.\n\nАнна - эксперт в сфере таро и основатель онлайн-школы. Более 16 тыс личных раскладов\n\nЕсли Вы здесь - это не случайность. Значит Вас что-то тревожит и карты помогут в этом разобраться.\n\nНу что, давайте начнём.\n\n👇Для продолжения, нажмите кнопоку снизу"

choose_taro_card = "🔮Ваша задача внимательно посмотреть на карты и выбрать одну из 6 закрытых карт таро"

# Вывод при выборе карт:
CARDS_DIR = DATA_DIR / "cards_photos"
_cards_end_of_all = f'Для расшифровки значения и вашего общего состояния напишите {markdown.hbold("Анне в личные сообщения — https://t.me/taro_anna_pie название карты, чтобы получить расшифровку карты и полезные")} рекомендации🙌\n\n{markdown.hbold("❗️Количество бесплатных мест ограничено")}'
taro_cards = [
        {'photo': CARDS_DIR / "taro_card_0.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Жрица")}'},
        {'photo': CARDS_DIR / "taro_card_1.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Башня")}'},
        {'photo': CARDS_DIR / "taro_card_2.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Солнце")}'},
        {'photo': CARDS_DIR / "taro_card_3.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Сила")}'},
        {'photo': CARDS_DIR / "taro_card_4.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Луна")}'},
        {'photo': CARDS_DIR / "taro_card_5.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Колесо Фортуны")}'}
    ]
byte_message = Template(f"{markdown.hbold('🔆Только сегодня')} дипломированный таролог Анна {markdown.hbold('подготовит для Вас бесплатный')} персональный расклад.\n\n📎Ваш кодовый номер заявки: {markdown.hcode('$code')}\n\nПожалуйста пришлите тарологу Анне название карты или её фото на личный аккаунт — @taro_anna_pie👈\n\n{markdown.hbold('❗️Количество бесплатных мест ограничено')}")
