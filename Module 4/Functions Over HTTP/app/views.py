from django.shortcuts import render
from app.forms import Hello, Age, Order

# Create your views here.
def hello(request):
    form = Hello(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        return render(request, "hello.html", {"form": form, "name":name})
    else:
        return render(request, "hello.html", {"form": form})

def how_old(request):
    form = Age(request.GET)
    if form.is_valid():
        birth = form.cleaned_data['birth']
        end = form.cleaned_data['end']
        result = end - birth
        return render(request, "how-old.html", {"form":form, "result":result, "birth":birth, "end":end})
    else:
        return render(request, "how-old.html", {"form": form})

def order(request):
    form = Order(request.GET)
    if form.is_valid():
        x = form.cleaned_data['burgers']
        y = form.cleaned_data['fries']
        z = form.cleaned_data['drinks']
        burger = x * 4.5
        fries = y * 1.5
        drinks = z * 1
        total = burger + fries + drinks
        return render(request, "order.html", {"form": form, "burger": burger, "fries": fries, "drinks": drinks,"total": total})
    else:
        return render(request, "order.html", {"form": form})