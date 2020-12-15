from datetime import datetime, timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import  JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import models

from . import models
from . import forms

def logout_view(request):
    logout(request)
    return redirect("/login/")

# Create your views here.
def index(request):
    context = {
        "title":"Suggestions",
    }

    query = ""
    if request.GET:
        query = request.GET['q']
        context[query] = str(query)
    return render(request, "index.html", context=context)

def add_suggestion(request):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect("/")
    else:
        form = forms.SuggestionForm()
    context = {
        "title":"Suggestion",
        "form":form
    }
    return render(request, "suggestion.html", context=context)

def comment(request, sugg_id):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save(request, sugg_id)
            return redirect("/")
    else:
        form = forms.CommentForm()
    context = {
        "title":"Comment",
        "sugg_id":sugg_id,
        "form":form
    }
    return render(request, "comment.html", context=context)

def get_suggestions(request):
    suggestion_objects = models.SuggestionModel.objects.all().order_by('-published_on')
    # {"key":value,"key":["value","value"], "key3":{}}
    suggestion_list = {}
    suggestion_list["suggestions"]=[]
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg).order_by('published_on')
        temp_sugg = {}
        temp_sugg["suggestion"]=sugg.suggestion
        temp_sugg["author"]=sugg.author.username
        temp_sugg["id"]=sugg.id
        temp_sugg["date"]=sugg.published_on.strftime("%Y-%m-%d %H:%M:%S")
        if sugg.image:
            temp_sugg["image"]=sugg.image.url
            temp_sugg["image_desc"]=sugg.image_description
        else:
            temp_sugg["image"]=""
            temp_sugg["image_desc"]=""
        temp_sugg["comments"]=[]
        for comm in comment_objects:
            temp_comm={}
            temp_comm["comment"]=comm.comment
            temp_comm["id"]=comm.id
            temp_comm["author"]=comm.author.username
            time_diff = datetime.now(timezone.utc) - comm.published_on
            time_diff_s = time_diff.total_seconds()
            if time_diff_s < 60:
                temp_comm["date"] = "published " + str(int(time_diff_s)) + " seconds ago"
            else:
                time_diff_m = divmod(time_diff_s, 60)[0]
                if time_diff_m < 60:
                    temp_comm["date"] = "published " + str(int(time_diff_m)) + " minutes ago"
                else:
                    time_diff_h = divmod(time_diff_m, 60)[0]
                    if time_diff_h < 24:
                        temp_comm["date"] = "published " + str(int(time_diff_h)) + " hour ago"
                    else:
                        temp_comm["date"]  = "published on " + comm.published_on.strftime("%Y-%m-%d")
            # published {{ comm.date }} minutes ago
            # temp_comm["date"]=comm.published_on
            temp_sugg["comments"]+=[temp_comm]
        suggestion_list["suggestions"]+=[temp_sugg]
    return JsonResponse(suggestion_list)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)


def tetris(request):
    return render(request, 'tetris.html')