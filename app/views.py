from django.shortcuts import render

# Create your views here.
def build_in_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'HAI HOw aRe YoU','dt':dt,'c':0}
    return render(request,'build_in_filter.html',d)