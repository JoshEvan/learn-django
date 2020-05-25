from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Item

# Create your views here.
class ItemView():
    model = Item
    lookup = "idItem"
    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model,id=id)
        return obj
        


class IndexView(View):
    template_name = "items/index.html"
    queryset = Item.objects.all()
    context = {
        "object_list":queryset
    }

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.context)

class DetailView(ItemView,View):
    template_name="items/detail.html"
    
    def get(self, request, idItem =None, *args, **kwargs ):
        context = {}
        if id is not None:
            obj = self.get_object()
            context["obj"] = obj

        return render(request, self.template_name,context)

