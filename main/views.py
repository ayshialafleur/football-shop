from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Ayshia La Fleur Felizia',
        'class': 'KKI'
    }

    return render(request, "main.html", context)