from django.shortcuts import render
from django.views import View
from .models import Item

# Create your views here.
class IndexView(View):
    template_name = "items/index.html"
    queryset = Item.objects.all()
    context = {
        "object_list":queryset
    }

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.context)


