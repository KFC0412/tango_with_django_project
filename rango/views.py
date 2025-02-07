from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {
                    'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                    }
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def faq(request):
    faq_list = [
        {"question": "What is Django?", "answer": "Django is a high-level Python web framework that helps in app development."},
    ]
    # Construct a dictionary for the context to pass to the template
    context_dict = {
        'faq_list': faq_list,
    }
    return render(request, 'rango/faq.html', context=context_dict)
# Create your views here.
