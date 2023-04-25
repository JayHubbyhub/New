from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context, loader
from .models import Tree
from .forms import TreeRecordForm
from django.template.loader import get_template
from django.views import View
from django.http import HttpResponse
import qrcode
from io import BytesIO
from django.views.generic import ListView

# Create your views here.
class TreeListView(ListView):
    model = Tree
    template_name = 'trees/tree_list.html'

class treeRecords(View):
    template = "treeRecords.html"
    def get(self, request):
        all_tree_records = Tree.objects.order_by('treeID').values('treeID').distinct()
        context = {
            "all_tree_records": all_tree_records
        }
        return render(request, "trees/treeRecords.html", context)
    
def newTreeRecord(request):
    treeindex = request.GET.get('treeindex')
    if request.method == "POST":
        tree_record_form = TreeRecordForm(treeindex, request.POST, request.FILES)
        if tree_record_form.is_valid():
            tree_record_form.save()
            return redirect("trees:treeRecords")
    else:
        tree_record_form = TreeRecordForm(treeindex)
    return render(request, "trees/add.html", {"tree_record_form": tree_record_form})

def tree_details(request, treeindex):
    trees = Tree.objects.filter(treeID=treeindex).order_by('harvestDate')
    context = {
        'trees': trees,
        'treeindex': treeindex,
        }
    return render(request, 'tree_details.html', context)