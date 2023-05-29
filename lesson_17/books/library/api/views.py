from datetime import datetime

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


BOOKS = [
    {
        "id": 1,
        "name": "Всадник без головы",
        "created_at": datetime.now()
    },
    {
        "id": 2,
        "name": "Не рычите на собаку",
        "created_at": datetime.now()
    },
    {
        "id": 3,
        "name": "Финансист",
        "created_at": datetime.now()
    }
]


def books(request):
    if request.method == 'GET':
        from .utils.todos import Todos
        Todos()
        print(settings.URL)
        return JsonResponse({'books': BOOKS})

    elif request.method == 'POST':
        book = dict(request.POST)
        for key in book:
            book[key] = book[key][0]

        book["created_at"] = datetime.now()
        book["id"] = int(book["id"])
        BOOKS.append(book)
        return HttpResponse(status=201)


def get_book(request, book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    if book:
        if request.method == 'GET':
            return JsonResponse(book)
        elif request.method == 'DELETE':
            BOOKS.pop(book_id)
            return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)
