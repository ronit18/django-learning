from django.shortcuts import render, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages


def receipe(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        Receipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect("recipe")

    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        print(request.GET.get("search"))
        queryset.queryset = queryset.filter(
            recipe_name__icontains=request.GET.get("search")
        )

    context = {"recipes": queryset}
    return render(request, "recipe.html", context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("recipe")


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect("recipe")

    context = {"recipe": queryset}

    return render(request, "update_receipe.html", context)


def login_page(request):
    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")

        usernameDB = User.objects.filter(username=username)
        if usernameDB.exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        messages.success(request, "Account created successfully")

        user.set_password(password)
        return redirect("register")

    return render(request, "register.html")
