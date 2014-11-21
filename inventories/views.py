# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, FormView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Inventory, Perfiles
from .forms import UserForm
from .forms import InventoryForm

import forms

#class CreateInventoryView(CreateView):

#    model = Inventory
#    template_name = 'edit_inventory.html'
#    form_class = forms.InventoryForm

#    def form_valid(self, form):
#        obj = form.save(commit=False)
#        obj.save()
#        return HttpResponseRedirect(reverse_lazy('index'))


class Registrarse(FormView):
	template_name = 'registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		user.save()
		return HttpResponseRedirect(reverse_lazy('login'))

class List(ListView):
	queryset = Inventory.objects.all().order_by('-created')
	model = Inventory
	template_name='list.html'
	form_class = InventoryForm
	#success_url = reverse_lazy('list')
	#paginate_by="5",
	queryset=Inventory.objects.all()
	context_object_name="inventories"

	#def list(request):
	#    inventories = Inventory.objects.all()
	#    data = {}
	#    data['object_list'] = inventories
	#    return render(request, template_name, data)


class Create(CreateView):
	template_name = 'create.html'
	model = Inventory
	form_class = InventoryForm
	success_url = reverse_lazy('login')

	def create(request):
	    form = InventoryForm(request.POST or None)
	    if form.is_valid():
	        form.save()
	        return redirect('list')
	    return render(request, template_name, {'form':form})

	#def form_valid(self, form):
	#	inv = form.save(commit=False)
	#	inv.save()
	#	return HttpResponseRedirect(reverse_lazy('login'))

class Delete(DeleteView):
	model = Inventory
	success_url = reverse_lazy('delete')

	def delete(request, pk, template_name='delete.html'):
	    inventories = get_object_or_404(Inventory, pk=pk)
	    if request.method=='POST':
	        inventories.delete()
	        return redirect('server_list')
	    return render(request, template_name, {'object':inventories})

	#def delete(self, request):
	#    self.object = self.get_object()
	#    self.object.delete()
	#    return HttpResponseRedirect(reverse_lazy('login'))

