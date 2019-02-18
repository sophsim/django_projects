from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    hello_world = "hello world"

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'main.html', context=context)