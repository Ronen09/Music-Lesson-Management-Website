import locale

LESSON_PRICE_MULTIPLIER = 1.15

from lessons.models import Lesson, LessonRequest


def get_lesson_price(lesson_duration):
    locale.setlocale(locale.LC_ALL, 'en_GB')
    return locale.currency(lesson_duration * LESSON_PRICE_MULTIPLIER, grouping=True)


def has_lesson_request_been_fulfilled(lesson_request):
    """Check whether a lesson request has been fulfilled.

    Accomplished by searching for lessons

    :param lesson_request: _description_
    :type lesson_request: _type_
    """
    pass