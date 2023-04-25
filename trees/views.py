from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context, loader
from .models import Tree
from .forms import TreeRecordForm
from django.template.loader import get_template
from django.views import View
from django.http import HttpResponse
import qrcode
from io import BytesIO

# Create your views here.
class treeRecords(View):
    template = "treeRecords.html"
    def get(self, request):
        all_tree_records = Tree.objects.order_by('treeID').values('treeID').distinct()
        context = {
            "all_tree_records": all_tree_records
        }
        return render(request, "trees/treeRecords.html", context)
    
def newTreeRecord(request):
    if request.method == "POST":
        tree_record_form = TreeRecordForm(request.POST, request.FILES)
        if tree_record_form.is_valid():
            tree_record_form.save()
            return redirect("trees:newTreeRecord")
        else:
            tree_record_form = TreeRecordForm()
    return render(request, "trees/add.html", {"tree_record_form": TreeRecordForm})

def generate_qr(request, data):
    # Construct the URL to redirect to
    redirect_url = request.build_absolute_uri('/trees/treeRecords/')
    
    # Append the redirect URL to the data
    data_with_url = f"{data} {redirect_url}"
    
    # Generate the QR code image
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data_with_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    
    # Return the image as an HTTP response
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response

def tree_details(request, treeindex):
    trees = Tree.objects.filter(treeID=treeindex)
    context = {'trees': trees}
    return render(request, 'tree_details.html', context)