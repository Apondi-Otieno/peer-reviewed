from django.shortcuts import render,redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Follow, Post, Profile, Comment, Like
from .forms import ProfileUpdateForm, UserUpdateForm, NewPostForm, CommentForm
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    