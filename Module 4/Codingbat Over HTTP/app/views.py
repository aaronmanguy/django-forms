from django.shortcuts import render
from app.forms import *

# Create your views here.
def font_times(request):
    warmup = FontTime(request.GET)
    if warmup.is_valid():
        string = warmup.cleaned_data["string"]
        num = warmup.cleaned_data["num"]
        result = string[:3] * num
        return render(request, "warmup.html", {"warmup":warmup, "result":result})
    else:
        return render(request, "warmup.html", {"warmup":warmup})

def no_teen_sum(request):
    logic = TeenSum(request.GET)
    if logic.is_valid():
        a = logic.cleaned_data["a"]
        b = logic.cleaned_data["b"]
        c = logic.cleaned_data["c"]
        result = fix_teen(a) + fix_teen(b) + fix_teen(c)
        return render(request, "logic.html", {"logic":logic, "result": result})
    else:
        return render(request, "logic.html", {"logic": logic})

def fix_teen(n):
    if n == 13 or n == 14 or n == 17 or n == 19:
        return 0
    return n

def xyz_there(request):
    string = XYZThere(request.GET)
    if string.is_valid():
        u_input = string.cleaned_data["Input"]
        result = u_input.count ("xyz") > u_input.count (".xyz")
        return render(request, "string.html", {"string": string, "result": result})
    else:
        return render(request, "string.html", {"string": string})

def centered_average(request):
    list_ = CenteredAverage(request.GET)
    if list_.is_valid():
        a = list_.cleaned_data["a"]
        b = list_.cleaned_data["b"]
        c = list_.cleaned_data["c"]
        d = list_.cleaned_data["d"]
        e = list_.cleaned_data["e"]
        nums = [a, b, c, d, e]
        nums.sort()
        total = 0
        for i in range(1, len(nums) - 1):
            total += nums[i]
        result = total / (len(nums) - 2)
        return render(request, "list.html", {"list": list_, "result": result})
    else:
        return render(request, "list.html", {"list": list_})