from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    htmlTemplate = 'grace_bday/index.html'
    # Use UTC time
    expectedDate = datetime(2018, 1, 28, 0, 0)
    now = datetime.now()
    if now > expectedDate:
        htmlTemplate = 'grace_bday/index_new.html'
    return render(request, htmlTemplate)
