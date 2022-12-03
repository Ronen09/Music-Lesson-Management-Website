import locale

LESSON_PRICE_MULTIPLIER = 1.15


def get_lesson_price(lesson_duration):
    locale.setlocale(locale.LC_ALL, 'en_GB')
    return locale.currency(lesson_duration * LESSON_PRICE_MULTIPLIER, grouping=True)