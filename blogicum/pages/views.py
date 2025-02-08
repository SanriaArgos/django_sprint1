from django.shortcuts import render


def about(request):
    context = {
        'title': 'О проекте',
    }
    return render(request, 'pages/about.html', context)


def rules(request):
    context = {
        'title': 'Наши правила',
    }
    return render(request, 'pages/rules.html', context)
