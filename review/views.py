from django.shortcuts import render,redirect, get_object_or_404
from .forms import NewUserForm
import datetime as dt
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Follow, Post, Profile, Comment, Like
from .forms import ProfileUpdateForm, UserUpdateForm, NewPostForm, CommentForm
from django.http import HttpResponseRedirect


import random
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Post,Profile
from .serializer import Postserializer,ProfileSerializer
from rest_framework import 
# Create your views here.


def home(request):
    