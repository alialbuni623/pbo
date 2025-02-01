# forms.py
from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'steps', 'distance', 'calories_burned']

# views.py
from django.shortcuts import render, redirect
from .forms import ActivityForm

def record_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('activity_history')
    else:
        form = ActivityForm()
    return render(request, 'health/record_activity.html', {'form': form})
