from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'my_variable': mark_safe("<h1>Hello, world. You're at the <b>first_tutorial_project</b> index.</h1>")}
    
    # Combine both dictionaries
    context = {**date_dict, **my_dict}
    
    return render(request, 'first_app/index.html', context=context)