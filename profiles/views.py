from django.http import Http404
from django.shortcuts import render
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """View that displays the index of profiles application with a list of all profiles available.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTML page of the profiles index.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """View that displays the details of a chosen profile.

    Args:
        request (HttpRequest): The HTTP request.
        username (str): username of the chosen profile.

    Returns:
        HttpResponse: The HTML page of the profile details.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning(f'Erreur | Instance de Profile "{username}" introuvable.')
        raise Http404()

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
