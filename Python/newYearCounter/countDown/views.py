import datetime

from django.shortcuts import render

# render the html in the url
def index(request):
    now = datetime.datetime.now()
    return render(request, "countDown/index.html", {
        "newYear": now.day == 1 and now.month == 1,
        "remDays": (datetime.date(now.year + 1, 1, 1) - now.date()).days
    })
