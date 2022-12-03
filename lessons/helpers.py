import locale

from lessons.models import Invoice, Lesson

LESSON_PRICE_MULTIPLIER = 1.15


def get_lesson_price(lesson):
    locale.setlocale(locale.LC_ALL, 'en_GB')
    return locale.currency(lesson.duration * LESSON_PRICE_MULTIPLIER, grouping=True)


def get_invoice_amount(invoice):
    # Find the lessons that match the lesson request of this invoice
    lessons = Lesson.objects.filter(lesson_request=invoice.lesson_request)

    total_amount = 0

    for lesson in lessons:
        total_amount = total_amount + float(get_lesson_price(lesson)[1:])

    locale.setlocale(locale.LC_ALL, 'en_GB')
    return locale.currency(total_amount, grouping=True)