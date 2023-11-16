from django.shortcuts import render
from home.models import Phone


def example(request):
    phone = Phone.objects.all()
    context = {
        'phone':phone,
    }

    return render(request, 'index.html', context)


