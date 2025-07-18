from django.shortcuts import render
import datetime

# Create your views here.
def wish_view(request):
    dt = datetime.datetime.now()
    msg = 'Hi Friend! Good '
    hr = int(dt.strftime('%H'))
    if hr < 12:
        msg+='Morning!'
    elif hr < 16:
        msg += 'Afternoon!'
    elif hr < 21:
        msg += 'Evening!'
    else :
        msg += 'Night!'

    return render(request, 'testapp/results.html', {'msg': msg})
