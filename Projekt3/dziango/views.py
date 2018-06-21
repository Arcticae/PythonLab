from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from dziango.models import Thread, Reply
from django.utils import timezone
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.models import User

from .forms import *


# Create your views here.

def threads(request):
    threads_sorted = Thread.objects.order_by('-last_post')
    return render(request, 'dziango/threadlist.html', {'threads': threads_sorted})


def thread_view(request, pk):
    heading = get_object_or_404(Thread, pk=pk)
    replies = Reply.objects.filter(thread=heading).order_by('date_posted')
    return render(request, 'dziango/thread_view.html', {'thread_number': pk, 'replies': replies, 'heading': heading})


def new_thread(request):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.poster = request.user
            thread.last_post = timezone.now()
            thread.save()
            return redirect('threads')
    else:
        form = ThreadForm()
        return render(request, 'dziango/new_thread.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'dziango/register.html', {'form': form})


def new_post(request, pk):
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.thread = Thread.objects.get(pk=pk)
            post.thread.last_modified = timezone.now()
            post.created_date = timezone.now()
            post.thread.save()
            thread= Thread.objects.get(pk=pk)
            thread.last_post=timezone.now()
            thread.save()
            post.save()
            return redirect('thread_view', pk=pk)
    else:
        form = ReplyForm()
    return render(request, 'dziango/new_post.html', {'form': form})


def delete_post(request, pk, th_pk):
    Reply.objects.get(pk=pk).delete()
    return redirect('thread_view', pk=th_pk)


def delete_thread(request, pk):
    Thread.objects.get(pk=pk).delete()
    return redirect('/')


def user(request, pk):
    user1 = User.objects.get(pk=pk)
    return render(request, 'dziango/user_profile.html', {'user1': user1})


def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/', pk=pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'dziango/user_edit.html', {'form': form})
