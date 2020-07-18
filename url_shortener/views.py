import random
import string
from django.shortcuts import render, redirect
from .models import Link


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def home(request):
    return render(request, "url_shortener/view.html", {"short_url": None})


def shorten(request):
    url = request.POST["url"]
    try:
        entry = Link.objects.get(original_url=url)
    except Exception as e:  # noqa:F841
        entry = None
    if entry is None:
        short_url = get_random_alphanumeric_string(5)
        new_entry = Link(original_url=url, new_url=short_url)
        new_entry.save()
        return render(request, "url_shortener/view.html", {"short_url": new_entry.new_url})
    else:
        return render(request, "url_shortener/view.html", {"short_url": entry.new_url})


def view(request):
    objects = Link.objects.all()
    print(objects)
    return render(request, "url_shortener/viewlinks.html", {"links": objects})


def redirToShort(request, slug):
    entry = Link.objects.get(new_url=slug)
    if entry is None:
        return redirect("/")
    else:
        return redirect(entry.original_url)
