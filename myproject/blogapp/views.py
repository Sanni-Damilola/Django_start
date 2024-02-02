from django.shortcuts import render

# Create your views here.
def archive(req):
    return render(req, "blog/archive.html")

def details(req):
    return render(req, "blog/details.html")
git commit -m "feat: Create and integrate blog app"
