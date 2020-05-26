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
        

class IndexView(ItemView,View):
    template_name = "items/index.html"
    
    def get(self,request,*args,**kwargs):
        queryset = Item.objects.all()
        context = {
            "object_list":queryset,
            "create_url": reverse_lazy('items:create')
        }
        return render(request,self.template_name,context)

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

class UpdateView(ItemView,View):
    template_name = "items/update.html"
    def get(self, request, idItem =None, *args, **kwargs):
        context = {}
        object = self.get_object()
        if(object is not None):
            form = ItemForm(instance=object)
            context['form'] = form
            context['object'] = object
            context['cancelUrl'] = reverse_lazy('items:index')
        return render(request, self.template_name, context)
    
    def post(self, request, idItem=None, *args, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = ItemForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect(reverse_lazy('items:index'))
            context['form'] = form
            context['object'] = obj
        return render(request,self.template_name,context)
