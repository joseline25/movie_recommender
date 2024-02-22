from django.urls import path
from . import views


urlpatterns = [
    # route is a string contains a URL pattern
    
    # list of movies in the database
    path(route='movies/', view=views.movie_recommendation_view, name='recommendations'),
    path(route='', view=views.movie_recommendation_view, name='recommendations'),
]
