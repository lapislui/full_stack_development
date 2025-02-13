from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage
from django.utils.safestring import mark_safe
from . import forms # Import the forms.py file from the same directory.

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'my_variable': mark_safe("<h1>Hello, world. You're at the <b>first_tutorial_project</b> index.</h1>")}
    
    # Combine both dictionaries
    context = {**date_dict, **my_dict}
    
    return render(request, 'first_app/index.html', context=context)
def form_name_view(request):
    form = forms.FormName()

    # Check to see if we get a POST back.
    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormName(request.POST)

        # Check to see form is valid
        if form.is_valid():
            # Do something.
            print("Form Validation Success. Prints in console.")
            # print("Name: " + form.cleaned_data['name'])
            # print("Email: " + form.cleaned_data['email'])
            # print("Text: " + form.cleaned_data['text'])
            print("Topic is: " + form.cleaned_data['Topic'])

    return render(request, 'first_app/form.html', {'form': form})
