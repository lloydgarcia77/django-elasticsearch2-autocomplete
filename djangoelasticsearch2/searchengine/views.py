from django.shortcuts import render
from searchengine import models
from haystack.query import SearchQuerySet
from django.db.models import Count, Q
import simplejson as json
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    template_name = "index.html"
    results = ""

    if request.method == 'GET':
        keyword = request.GET.get('search')
        # https://django-haystack.readthedocs.io/en/latest/searchqueryset_api.html#SearchQuerySet.models
        if keyword:
            results = SearchQuerySet().filter(Q(email__contains=keyword) |
                                              Q(name__contains=keyword) |
                                              Q(postId__contains=keyword) |
                                              Q(body__contains=keyword) |
                                              Q(user_id__contains=keyword) |
                                              Q(tid__contains=keyword) |
                                              Q(title__contains=keyword) |
                                              Q(completed__contains=keyword)
                                              ).load_all().models(models.Comments, models.Todo)
            x = SearchQuerySet().autocomplete(email__endswith='Al')
            for b in x:
                print('------------', b.email)
    context = {
        'results': results,
    }

    return render(request, template_name, context)


def autocomplete_query(request):
    data = dict()
    if request.is_ajax():
        if request.method == 'GET':
            # b = [x.email for x in SearchQuerySet().autocomplete(email__endswith='Al')]
            b = [x.name for x in SearchQuerySet().models(
                models.Comments).load_all()]
            data['context'] = {
                'b': b,
            }

    return JsonResponse(data)


def autocomplete(request):
    template_name = "autocomplete.html"

    context = {

    }

    return render(request, template_name, context)


def autocomplete_jquery(request):
    template_name = "autocomplete_jquery.html"
    
    if request.method == 'GET':
        keyword = request.GET.get('q')
        if keyword:
            results = SearchQuerySet().filter(Q(name__contains=keyword)).models(models.Comments).load_all()  
        else:
            results = ""
    context = {
        'results': results,
    }

    return render(request, template_name, context)
