# -*- coding: utf-8 -*-
# Домашнее задание по теме "Создание исключений".
# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте
# Комментарии к заданию:
# Важно понять разницу между обработкой исключений (блок try/except) и их генерацией (оператор raise).
# Дополнительно: попробуйте использовать блоки finally или else для дополнительных действий при обработке исключений.
# Обратите внимание на то, как исключения передаются по стеку вызовов и как это можно использовать для стратегии
# обработки ошибок в сложных программах.
# Важно!! Для передачи обработанных исключений в вызвавшую функцию, нужно вызывать raise

class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def auto_registration():
    print('---Запись на техобслуживание---')
    auto_data = str(input('Введите дату: '))
    try:
        if auto_data == '1 января':
            raise InvalidDataException("Извините у всех праздник и мы не работаем.")
    except InvalidDataException as exc1:
        print(f'Ошибка: {exc1}')
        raise
    else:
        print(f'{auto_data} - С нетерпением будем Вас ждать!')

    auto_process = str(input('Введите название модели авто: '))
    try:
        if auto_process <= 'Жигули':
            raise ProcessingException('К сожалению мы не можем Вас обслужить.')
    except ProcessingException as exc2:
        print(f'Ошибка: {exc2}')
        raise
    else:
        print('Добро пожаловать на обслуживание!')
    finally:
        print('Спасибо, уважаемый клиент! Ты ответил на все вопросы!')



auto_registration()