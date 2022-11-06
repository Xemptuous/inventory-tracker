from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Host, SubHost, ItemCategory, StructureCategory, Item, Structure, Transaction
from .forms import AddHost, AddSubHost

# Create your views here.

def base(request):
    return render(request, 'inventory_tracker/base.html')


def index(response):
    return render(response, "inventory_tracker/index.html", {})


def hosts(request):
    form = AddHost()
    if request.method == "POST":
        form = AddHost(request.POST)
        if form.is_valid:
            n = form.cleaned_data["name"]
            d = form.cleaned_data['description']
            sh = Host(name=n, description=d)
            sh.save()
        return HttpResponseRedirect("/")

    host_list = Host.objects.order_by('name')
    context = {
        'host_list': host_list,
        'form': form,
    }
    return render(request, "inventory_tracker/hosts.html", context)


def subHosts(request, host_id):
    form = AddSubHost()
    if request.method == "POST":
        form = AddSubHost(request.POST)
        if form.is_valid:
            n = form.cleaned_data["name"]
            d = form.cleaned_data['description']
            sh = SubHost(name=n, description=d, host=host_id)
            sh.save()
        return HttpResponseRedirect("/")
    host = get_object_or_404(Host, pk=host_id)
    subhost_list = SubHost.objects.filter(host__id=host_id).order_by('name')
    item_cat_list = ItemCategory.objects.filter(host__id=host_id).order_by('name')
    context = {
        'subhost_list': subhost_list,
        'item_cat_list': item_cat_list,
        'host': host,
        'form': form
    }
    return render(request, 'inventory_tracker/subhosts.html', context)


def transactionDashboard(request, host_id, subhost_id):
    host = get_object_or_404(Host, pk=host_id)
    subhost = get_object_or_404(SubHost, pk=subhost_id)
    transaction_list = Transaction.objects.filter(subhost__id=subhost_id)
    context = { 
        'transaction_list': transaction_list,
        'host': host,
        'subhost': subhost,
    }
    return render(request, 'inventory_tracker/transactions.html', context)


def transactionDetail(request, host_id, subhost_id, trans_id):
    host = get_object_or_404(Host, pk=host_id)
    subhost = get_object_or_404(SubHost, pk=subhost_id)
    transaction = get_object_or_404(Transaction, pk=trans_id)
    context = {
        "host": host,
        "subhost" : subhost,
        "transaction" : transaction,
    }
    return render(request, 'inventory_tracker/transaction_detail.html', context)


def categories(request, host_id):
    host = get_object_or_404(Host, pk=host_id)
    item_categories = ItemCategory.objects.filter(host__id=host_id).order_by('name')
    structure_categories = StructureCategory.objects.filter(host__id=host_id).order_by('name')
    context = { 
        'host': host,
        'item_categories': item_categories,
        'structure_categories': structure_categories
    }
    return render(request, 'inventory_tracker/category_overview.html', context)


def itemCategory(request, host_id, cat_id):
    host = get_object_or_404(Host, pk=host_id)
    category = get_object_or_404(ItemCategory, pk=cat_id)
    item_list = Item.objects.filter(host__id=host_id, category__id=cat_id).order_by('name')
    context = { 
        'host': host,
        'category': category,
        'item_list': item_list,
    }
    return render(request, 'inventory_tracker/category.html', context)


def itemDetails(request, host_id, cat_id, item_id):
    host = get_object_or_404(Host, pk=host_id)
    category = get_object_or_404(ItemCategory, pk=cat_id)
    subhost_list = SubHost.objects.filter(host__id=host_id).order_by('name')
    subhosts = [ s.id for s in subhost_list]
    transaction_list = Transaction.objects.filter(
        subhost__in=subhosts, 
        item_category__id=cat_id
    )

    context = { 
        'host': host,
        'category': category,
        'transaction_list': transaction_list
    }
    return render(request, 'inventory_tracker/item_transactions.html', context)
