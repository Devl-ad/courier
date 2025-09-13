from django.shortcuts import render
from .models import Package


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


def track(request):
    context = {}
    track_id = request.GET.get("track-id", None)

    if track_id is not None:
        try:
            package = Package.objects.get(track_id__exact=track_id)

            context["package"] = package
        except Package.DoesNotExist:
            context["package"] = None

    else:
        context["package"] = None
    return render(request, "track.html", context)
