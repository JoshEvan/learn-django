from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm

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
        "object_list":queryset,
        "create_url": reverse_lazy('items:create')
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

class CreateView(View):
    template_name = "items/create.html"
    
    def get(self, request, *args, **kwargs):
        form = ItemForm()
        context = {
            'form': form
        }
        return render(request,self.template_name, context)
    
    def post(self,request, *args, **kwargs):
        form = ItemForm(request.POST)
        context = {}

        if form.is_valid():
            form.save()
            form = ItemForm()
            return redirect(reverse_lazy('items:index'))
        
        context['form'] = form

        return render(request, self.template_name, context)

