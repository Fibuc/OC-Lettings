from django.shortcuts import render


def index(request):
    """View that displays the principal page of website.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTML page of the principal index.
    """
    return render(request, 'index.html')


def error_404(request, exception):
    """View that displays a test of 404 error.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTML page of the 404 error.
    """
    return render(request, '404.html', status=404)


def error_500(request):
    """View that displays a test of 500 error.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTML page of the 500 error.
    """
    return render(request, '500.html', status=500)
