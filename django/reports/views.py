from django.shortcuts import render
from django.views import generic


# Create your views here.
from .models import County, Lake, Report

class IndexView(generic.ListView):
  template_name = "reports/index.html"
  context_object_name = "counties_list"
  
  def get_queryset(self):
    return County.objects.order_by('name')
  
class CountyView(generic.DetailView):
    model = County
    template_name = "reports/county.html"
    def get_object(self):
      return get_object_or_404(County, pk=request.session['county_name_slug'])

"""def homePage(request):
  counties = County.objects.order_by('name')
  return render(request, 'reports/index.html', {'counties': counties})

def countyPage(request):
  counties = County.objects.order_by('name')
  return render(request, 'reports/county.html', {'counties': counties})"""