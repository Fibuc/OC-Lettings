from django.shortcuts import render
from django.http import Http404
from .models import Letting
import logging


logger = logging.getLogger(__name__)


def index(request):
    """View that displays the index of lettings application with a list of all lettings available.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTML page of the lettings index.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """View that displays the address of a chosen letting.

    Args:
        request (HttpRequest): The HTTP request.
        letting_id (int): ID of the chosen letting.

    Returns:
        HttpResponse: The HTML page of the letting address.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning(f'Erreur | Instance de Letting ID n°{letting_id} introuvable.')
        raise Http404()

    context = {'title': letting.title, 'address': letting.address}
    return render(request, 'lettings/letting.html', context)
