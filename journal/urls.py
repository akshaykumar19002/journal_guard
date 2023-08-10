from django.urls import path
from .views import *

app_name = 'journal'

urlpatterns = [
    path('add', add_journal, name='add-journal'),
    path('edit/<str:id>', edit_journal, name='edit-journal'),
    path('delete/<str:id>', delete_journal, name='delete-journal'),
    path('view/<str:id>', view_journal, name='view-journal'),
    path('view-all', view_all_journals, name='view-all-journals'),
    path('calendar/', default_calendar_view, name='default_calendar_view'),
    path('calendar/<int:year>/<int:month>/', calendar_view, name='calendar_view'),
    
]