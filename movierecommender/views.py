from django.shortcuts import render
from .models import Movie

# Create your views here.
#generate the context of the list of movies

def generate_movies_context():
    context = {}
    # Show only movies in recommendation list
    # Sorted by vote_average in desc
    # Get recommended movie counts
    recommended_count = Movie.objects.filter(
        recommended=True
    ).count()
    # If there are no recommended movies
    if recommended_count == 0:
        # Just return the top voted and unwatched movies as popular ones
        movies = Movie.objects.filter(
            watched=False
        ).order_by('-vote_count')[:1000]
    else:
        # Get the top voted, unwatched, and recommended movies
        movies = Movie.objects.filter(
            watched=False
        ).filter(
            recommended=True
        ).order_by('-vote_count')[:30]
    context['movie_list'] = movies
    return context



def movie_recommendation_view(request):
    if request.method == "GET":
      # The context/data to be presented in the HTML template
      context = generate_movies_context()
      # Render a HTML page with specified template and context
      return render(request, 'movierecommender/movie_list.html', context)
  
  
""" 

There are probably hundreds of good recommendation algorithms and can be roughly divided
into two categories:

Content filtering based: The content filtering based recommendation algorithms assume
you may like a new movie
if you have watched very similar movies before. Or based on your user profile (like age,
gender, interests), it will try
to find new movies matching your profile.

Collaborative filtering based: The collaborative filtering algorithms assume you may like
a new movie if other users similar to
you (similar profile or watched similar movies) have watched this movie.


In this project, we will use content filtering based algorithm, and we will try to 
recommend unwatched/new movies to you if they are similar to your watched movies.

Then how do we calculate such movie similarity? There are also many ways to do that, 
depends on your data and problem settings.
Some popular ones include Jaccard similarity, Euclidean Distance, Cosine Similarity, 
or even using various Neural Networks.

Here we will use Jaccard similarity which is probably the simplest but very effective 
method to calculate similarity between two sets.

Jaccard Similarity is defined as the size of intersection of two sets divided by the size 
of union of that two sets.
"""