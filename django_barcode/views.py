from .models import Barcode
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


class BarcodeListView(generic.ListView):
    queryset = Barcode.objects.all()
    template_name = "barcode_list.html"

class BarcodeCreateView(generic.CreateView):
    model = Barcode
    fields = '__all__'
    template_name = "barcode_create.html"
    success_url = reverse_lazy('list') 

class BarcodeDetailView(generic.DetailView):
    model = Barcode
    template_name = "barcode_detail.html"

class BarcodeUpdateView(generic.UpdateView):
    model = Barcode
    fields = '__all__'
    template_name = "barcode_update.html"
    success_url = reverse_lazy('list') 

class BarcodeDeleteView(generic.DeleteView):
    model = Barcode
    template_name = "barcode_delete.html"
    success_url = reverse_lazy('list') 
