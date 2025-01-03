from django.shortcuts import render
from django.views.generic import ListView, DetailView
from graph.models import Data

# Create your views here.
class DataLV(ListView):
    model = Data
    template_name = 'graph/data_all.html'
    context_object_name = 'datas'
    paginate_by = 1

from django.conf import settings     #댓글

class DataDV(DetailView):
    model = Data

    def get_context_data(self, **kwargs):    #댓글
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.id}"
        return context

