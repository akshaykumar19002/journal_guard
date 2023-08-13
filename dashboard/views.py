from django.shortcuts import render
from django.utils.html import strip_tags
from django.utils import timezone
import pytz

from journal.models import Journal
from journal.utils import decrypt

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'dashboard/home.html')
    journal = Journal.objects.filter(user=request.user).order_by('-created_at')[:10]
    user_timezone = request.COOKIES.get('timezone')
    if user_timezone:
        timezone.activate(pytz.timezone(user_timezone))
    for entry in journal:
        entry.content = decrypt(request, entry.content)
        entry.content = strip_tags(entry.content)
        entry.content = entry.content[:100] + '...'
    return render(request, 'dashboard/home.html', {'journal': journal})
