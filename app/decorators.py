from functools import wraps

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from app.models import JobOffer


def user_not_authenticated(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return HttpResponseRedirect("/")

    return wrap


def user_can_modify(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        if not request.user.has_perm("app.change_joboffer"):
            try:
                JobOffer.objects.get(id=kwargs.get("pk"), author=request.user)
            except JobOffer.DoesNotExist:
                messages.warning(
                    request, "You do not have permission to modify this offer"
                )
                return redirect("offers")
            except ValueError:
                return redirect("offers")
        return func(request, *args, **kwargs)

    return wrap
