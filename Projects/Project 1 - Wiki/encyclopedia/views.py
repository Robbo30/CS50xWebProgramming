from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import choice
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == 'POST':
        if util.get_entry(request.POST['q']):
            entry = request.POST['q']
            return HttpResponseRedirect(f"/wiki/{entry}")
        else:
            entries = util.list_entries()
            search_result = []
            for entry in entries:
                if request.POST['q'].lower() in entry.lower():
                    search_result.append(entry)
            return render(request, "encyclopedia/search.html", {
                "results": search_result
            })

def new_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        entries = util.list_entries()
        for entry in entries:
            if title.lower() == entry.lower():
                return render(request, 'encyclopedia/entry.html', {
                    'entry': "Entry already exist."
                })
        with open(f"entries/{title}.md", mode='w', newline='', encoding='utf-8') as file:
            file.write(request.POST['entry'])
        return HttpResponseRedirect(f"/wiki/{title}")
    else:
        return render(request, "encyclopedia/new_page.html")

def edit_page(request, title):
    if request.method == 'POST':
        with open(f"entries/{title}.md", mode='w', newline='', encoding='utf-8') as file:
            file.write(request.POST['entry'])
        return HttpResponseRedirect(f"/wiki/{title}")
    else:
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            'title': title,
            'entry': entry
        })

def entry(request, title):
    if util.get_entry(title):
        entry = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": "Entry does not exist"
        })

def random(request):
    title = choice(util.list_entries())
    return HttpResponseRedirect(f"/wiki/{title}")