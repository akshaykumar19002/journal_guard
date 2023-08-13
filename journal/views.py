from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import JsonResponse
from .utils import *

import uuid

from .forms import *
from .models import *

@login_required
def add_journal(request):
    form = JournalForm()
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.id = uuid.uuid4()
            journal.content = encrypt(request, journal.content)
            journal.save()
            return redirect('dashboard:home')
    return render(request, 'journal/add-journal.html', {'form': form})

@login_required
def edit_journal(request, id):
    journal = get_object_or_404(Journal, id=id)
    journal.content = decrypt(request, journal.content)
    form = JournalForm(instance=journal)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.content = encrypt(request, journal.content)
            journal.save()
            return redirect('dashboard:home')
    return render(request, 'journal/edit-journal.html', {'form': form})

@login_required
def delete_journal(request, id):
    journal = get_object_or_404(Journal, id=id)
    journal.delete()
    return redirect('dashboard:home')

@login_required
def view_journal(request, id):
    journal = get_object_or_404(Journal, id=id)
    journal.content = decrypt(request, journal.content)
    return render(request, 'journal/view-journal.html', {'journal': journal})

@login_required
def view_all_journals(request):
    journals = Journal.objects.filter(user=request.user)
    for journal in journals:
        journal.content = decrypt(request, journal.content)
    return render(request, 'journal/view-all-journals.html', {'journals': journals})

@login_required
def calendar_view(request, year=None, month=None):
    today = datetime.today()
    
    if not year or not month:
        year, month = today.year, today.month

    entries = Journal.objects.filter(created_at__year=year, created_at__month=month, user=request.user)
    events = [{
        'title': entry.title,
        'start': entry.created_at.strftime('%Y-%m-%d'),
        'url': reverse('journal:view-journal', args=[entry.id])
    } for entry in entries]
    
    return render(request, 'journal/calendar.html', {'events': events})

@login_required
def default_calendar_view(request):
    today = datetime.today()
    return redirect('journal:calendar_view', year=today.year, month=today.month)

