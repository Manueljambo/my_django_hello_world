from django.views.generic import ListView
from .models import Something

class HomePageView(ListView):
    model = Something
    template_name = "home.html"

    context_object_name = 'all_posts_list'