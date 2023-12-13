from django.shortcuts import render,redirect
from Home.models import project,client_feedback,client_logo,contact,subscribe,about_count

# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']

        cm = contact.objects.create(name=name,subject=subject,email=email,message=msg)
        cm.save()

        return redirect('home')

    else:
        clients = project.objects.all()
        cls = client_logo.objects.all()
        cfs = client_feedback.objects.all()
        counts = about_count.objects.all()
        return render(request,'index.html',{'clients':clients, 'cls':cls, 'cfs':cfs, 'counts':counts})
    
def subscribes(request):
    if request.method == "POST":
        email = request.POST['email']
        user = subscribe.objects.create(email=email)
        user.save()
        return redirect('home')

    else:
        return redirect('home')