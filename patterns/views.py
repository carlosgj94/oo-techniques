from django.shortcuts import render
from django.views.generic import View
from models import *


# Create your views here.
class IndexView(View):
    def get(self, request):
        patterns = Pattern.objects.all()
        tags = Tag.objects.all()
        context = {
            "title": "Patterns list",
            "patterns": patterns,
            "tags": tags
        }
        return render(request, "patterns/index.html", context)


class PatternView(View):
    def get(self, request, id):
        patterns = Pattern.objects.all()
        tags = Tag.objects.all()
        pattern = Pattern.objects.get(id=id)
        context = {
            "title": pattern.name,
            "pattern": pattern,
            "patterns": patterns,
            "tags": tags
        }
        return render(request, "patterns/pattern.html", context)


class TagView(View):
    def get(self, request, id):
        patterns = Pattern.objects.all()
        tags = Tag.objects.all()
        patterns_tag = Pattern.objects.filter(tags__id=id)
        context = {
            "title": "Tag",
            "patterns_tag": patterns_tag,
            "patterns": patterns,
            "tags": tags
        }
        return render(request, "patterns/tag.html", context)
