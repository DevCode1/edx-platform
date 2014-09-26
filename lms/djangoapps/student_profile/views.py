""" Views for a student's profile information. """

from django.conf import settings
from django.http import (
    QueryDict, HttpResponse,
    HttpResponseBadRequest, HttpResponseServerError
)
from django_future.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.translation import get_language

from edxmako.shortcuts import render_to_response
from dark_lang.models import DarkLangConfig
from lang_pref import LANGUAGE_KEY
from user_api.api import profile as profile_api
from third_party_auth import pipeline


@login_required
@require_http_methods(['GET'])
def index(request):
    """Render the profile info page.

    Args:
        request (HttpRequest)

    Returns:
        HttpResponse: 200 if successful
        HttpResponse: 302 if not logged in (redirect to login page)
        HttpResponse: 405 if using an unsupported HTTP method

    Example usage:

        GET /profile

    """
    user = request.user
    released_languages = DarkLangConfig.current().released_languages_list

    # If the default language is not in the list of released languages,
    # add it and re-alphabetize the list
    default_language = settings.LANGUAGE_CODE
    if default_language not in released_languages:
        released_languages.append(default_language)
        released_languages.sort()

    # Get the language used in the current thread
    language_code = get_language()
    preferred_language_code = profile_api.preference_info(user.username)[LANGUAGE_KEY]

    if preferred_language_code in settings.LANGUAGE_DICT:
        # If the user has a valid preferred language, use it 
        # as the active language
        language = settings.LANGUAGE_DICT[preferred_language_code]
    elif language_code in settings.LANGUAGE_DICT:
        # Otherwise, use the language used in the current thread
        language = settings.LANGUAGE_DICT[language_code]
    else:
        language = settings.LANGUAGE_DICT[default_language]

    return render_to_response(
        'student_profile/index.html', {
            'disable_courseware_js': True,
            'provider_user_states': pipeline.get_provider_user_states(user),
            'released_languages': released_languages,
            'language_code': language_code,
            'language': language,
        }
    )


@login_required
@require_http_methods(['PUT'])
@ensure_csrf_cookie
def name_change_handler(request):
    """Change the user's name.

    Args:
        request (HttpRequest)

    Returns:
        HttpResponse: 204 if successful
        HttpResponse: 302 if not logged in (redirect to login page)
        HttpResponse: 400 if the provided name is invalid
        HttpResponse: 405 if using an unsupported HTTP method
        HttpResponse: 500 if an unexpected error occurs.

    Example usage:

        PUT /profile/name_change

    """
    put = QueryDict(request.body)

    username = request.user.username
    new_name = put.get('new_name')

    if new_name is None:
        return HttpResponseBadRequest("Missing param 'new_name'")

    try:
        profile_api.update_profile(username, full_name=new_name)
    except profile_api.ProfileInvalidField:
        return HttpResponseBadRequest()
    except profile_api.ProfileUserNotFound:
        return HttpResponseServerError()

    # A 204 is intended to allow input for actions to take place
    # without causing a change to the user agent's active document view.
    return HttpResponse(status=204)

@login_required
@require_http_methods(['PUT'])
@ensure_csrf_cookie
def language_change_handler(request):
    """Change the user's language preference.

    Args:
        request (HttpRequest)

    Returns:
        HttpResponse: 204 if successful
        HttpResponse: 302 if not logged in (redirect to login page)
        HttpResponse: 400 if no language is provided
        HttpResponse: 405 if using an unsupported HTTP method
        HttpResponse: 500 if an unexpected error occurs.

    Example usage:

        PUT /profile/language_change

    """
    put = QueryDict(request.body)

    username = request.user.username
    new_language = put.get('new_language')

    if new_language is None:
        return HttpResponseBadRequest("Missing param 'new_language'")

    try:
        kwargs = {}
        kwargs[LANGUAGE_KEY] = new_language
        profile_api.update_preference(username, **kwargs)
    except profile_api.ProfileUserNotFound:
        return HttpResponseServerError()

    # A 204 is intended to allow input for actions to take place
    # without causing a change to the user agent's active document view.
    return HttpResponse(status=204)
