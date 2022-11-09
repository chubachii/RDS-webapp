from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def index(request):
    return HttpResponse("hello world")
    

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "webapp/upload.html", context = {
        "files": documents
    })