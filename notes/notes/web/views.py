from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from notes.web.forms import CreateProfileForm, AddNoteForm
from notes.web.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    notes = Note.objects.all()
    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = AddNoteForm()
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request):
    return HttpResponse('ok')


def delete_note(request):
    pass


def note_details(request):
    pass


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    return render(request, 'profile.html')


