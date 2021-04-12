from typing import NoReturn

import prompt


def welcome_user() -> NoReturn:
    """Метод для привествия пользователя"""
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


__all__ = ('welcome_user',)
