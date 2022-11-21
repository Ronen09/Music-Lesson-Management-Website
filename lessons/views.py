from django.shortcuts import render

from lessons.forms import SignUpForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", {"form": form})


def log_in(request):
    return render(request, "log_in.html")
