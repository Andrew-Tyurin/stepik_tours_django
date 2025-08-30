from . import data


def global_data(request):
    """
    Context processor — это функция, которая автоматически
    добавляет данные во все шаблоны. Реализация в views.py
    можно, но это считается плохим стилем, т.к. view
    и процессоры — разные вещи. Эта функция нужна для вывода
    данных в навигационную панель которая не зависит от запроса.
    Не забываем в setting.py -> TEMPLATES дополнить:
    'tours.context_processors.global_data'
    """
    return {'departures': data.departures}
