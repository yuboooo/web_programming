from django.shortcuts import redirect, render
from . import util
from markdown2 import markdown
from . import forms
from django.urls import reverse
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        content = "# The Page Does Not Exist!"
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown(content)
    })

def search(request):
    q = request.GET.get('q').lower()
    if q in list(map(str.lower, util.list_entries())):
        return redirect("entry", args=[q])
    return render(request, "encyclopedia/search.html", {
        "q": q, 
        "pages": [page for page in util.list_entries() if q in page.lower()]
    })

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html", {
          "form": forms.NewPageForm()
        })
    elif request.method == "POST":
        form = forms.NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
        if util.get_entry(title):
            message = 'This page title already exists! Please go to that title page and edit it instead!'
            return render(request, "encyclopedia/newpage.html", {
              "form": form,
              "message": message,
              "title": title
            })
        else:
            util.save_entry(title, content)
            return redirect(reverse('entry', args=[title]))

def edit(request, title):

    title = title
    if request.method == "GET":
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "form": forms.EditPageForm(initial={'content': content}),
            "title": title
        })

    elif request.method == "POST":
        form = forms.EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return redirect(reverse('entry', args=[title]))

def random_page(request):
    titles = util.list_entries()
    title = random.choice(titles)

    # Redirect to selected page:
    return redirect(reverse('entry', args=[title]))
