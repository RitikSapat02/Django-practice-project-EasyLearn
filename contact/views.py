from django.shortcuts import render
from .models  import Contact_content,Contact_Form

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        name = name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')

        contact_form_data = Contact_Form(name=name,email=email,subject=subject,message=message)

        contact_form_data.save()


    contact_items = Contact_content.objects.all()[0]

    return render(request,'contact.html',{
        'contact_items':contact_items,
    })
