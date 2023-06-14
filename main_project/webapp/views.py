from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from .filmModel import FilmModel


def index( request):

  films = FilmModel.GetAllFilms()

  users = FilmModel.GeAllUSers()

  #return JsonResponse( films, safe=False)

  return render(request, 'index.html', {
    'films': films,
    'users': users,
  })

