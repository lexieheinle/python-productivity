from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
  return render(request, 'index.html', {
      'new_item_text': request.POST.get('item_text', ''),
  })