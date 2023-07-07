from django.shortcuts import render


def home(request):
    peoples = [
        {"name": "John", "age": 20},
        {"name": "Jane", "age": 21},
        {"name": "Joe", "age": 22},
        {"name": "Jill", "age": 23},
        {"name": "Jack", "age": 24},
    ]
    return render(request, "index.html", context={"peoples": peoples})
