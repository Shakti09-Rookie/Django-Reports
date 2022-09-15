import re
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.

def home_view(request):
    sales_df = None
    form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        # lte = less than equal to, gte = greater than equal to
        qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        # qs2 = Sale.objects.get(id=1)
        if len(qs) > 0:        
            print(qs)
            sales_df = pd.DataFrame(qs.values())
            sales_df = sales_df.to_html()
            
            # df2 = pd.DataFrame(qs1.values_list())
            print(sales_df)
        else:
            print("No data")

    context = {
        'form' : form,
        'sales_df' : sales_df,
    }
    return render(request, 'sales/home.html', context)

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'