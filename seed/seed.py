import json

from mongoengine.errors import NotUniqueError, DoesNotExist
from models.models1 import Author, Quote

from connection.connect import get_connection


get_connection()


def main():
    with open('../json/authors.json', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            try:
                author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()
                print(f"Автор додано: {el.get('fullname')}")
            except NotUniqueError:
                print(f"Автор вже існує: {el.get('fullname')}")

    with open('../json/quotes.json', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            try:
                author, *_ = Author.objects(fullname=el.get('author'))
                quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
                quote.save()
                print(f"Цитату додано: {el.get('quote')}")
            except DoesNotExist:
                print(f"Автор не знайдено: {el.get('author')}")
            except NotUniqueError:
                print(f"Цитата вже існує: {el.get('quote')}")
            except ValueError:
                print(f"stop")


if __name__ == '__main__':
    main()