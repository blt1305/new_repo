from datetime import datetime

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
        return render(request, "books.html", {"books": BOOKS})

    elif request.method == 'POST':
        book = dict(request.POST)
        for key in book:
            book[key] = book[key][0]

        book["created_at"] = datetime.now()
        book["id"] = int(book["id"]) if "id" in book else 10
        BOOKS.append(book)
        return render(request, "books.html", {"books": BOOKS})


def create_book(request):
    return render(request, "create_book.html")
