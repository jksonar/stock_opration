from django.shortcuts import redirect, render
from .forms import StockForm
from .models import Stocks

# Create your views here.
def StocksFormView(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def showView(request):
    obj = Stocks.objects.all()
    template_name = 'crudapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateView(request, f_id):
    obj = Stocks.objects.get(id=f_id)
    form = StockForm(instance=obj)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, f_id):
    obj = Stocks.objects.get(id=f_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)
