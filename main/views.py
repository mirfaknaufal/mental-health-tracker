from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306244961',
        'name': 'Mirfak Naufal Pratama Putra',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)