from django.shortcuts import render, HttpResponse , redirect
from datetime import datetime
from home.models import Contact , Complaint , Bills , Appartment , Dependents , Visitor , Employee
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate, login , logout
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index (request):
    context={
        'variable1':'This is sent',
        'variable2':'This is sent'
    }
    #return HttpResponse("This is Home Page")
    return render(request, 'index.html',context)

 

def about (request):
    #return HttpResponse("This is About Page")
    mydata2=Appartment.objects.filter(vacancy="available")
    return render(request, 'about.html' , {"mycomp2":mydata2})

def services (request):
    #return HttpResponse("This is Services Page")
    if request.method == "POST":
        Name = request.POST.get('Name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        appartment = request.POST.get('appartment')
        password = request.POST.get('password')
        contact=Contact(Name=Name , email=email , phone=phone , appartment=appartment , 
        password=password , date=datetime.today() )
        contact.save()
        user = User.objects.create_user(Name, email, password)
        messages.success(request, 'You have been successfully signed up')
    
    
    return render(request, 'services.html')

def contact (request):
    #return HttpResponse("This is Contact Page")
    return render(request, 'contact.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered the correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in')
            return redirect('/mysoc')
        # A backend authenticated the credentials
                   
        else:
            return render(request , 'login.html')
        # No backend authenticated the credentials
    return render(request , 'login.html')

def mysoc (request):
    #return HttpResponse("This is About Page")
    return render(request, 'mysoc.html')

def complaint (request):
    #return HttpResponse("This is Complaint Page")
    if request.method == "POST":
        ownername = request.POST.get('ownername')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        appartment = request.POST.get('appartment')
        desc = request.POST.get('desc')
        comp = Complaint (ownername=ownername , email=email , phone=phone , appartment=appartment , 
        desc=desc , date=datetime.today() )
        comp.save()
        messages.success(request, 'Your Complaint has been successfully registered')
        return redirect ('/mysoc')
    return render(request, 'complaint.html' )

def complaintstatus (request):
    #return HttpResponse("This is About Page")
    myuser = request.user
    currentuser = myuser.username
    print(currentuser)
    mydata=Complaint.objects.filter(ownername=currentuser)
    return render(request, 'complaintstatus.html' , {"mycomp":mydata} )

def maintainancebill (request):
    #return HttpResponse("This is About Page")
    myuser1 = request.user
    currentuser1 = myuser1.username
    print(currentuser1)
    mydata1=Bills.objects.filter(username1=currentuser1 , Status="Pending")
    return render(request, 'Bills.html' , {"mycomp1":mydata1} )

def dependents (request):
    #return HttpResponse("This is Complaint Page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        ownerid = request.POST.get('ownerid')
        appartment = request.POST.get('appartment')
        comp1 = Dependents(name=name , email=email , phone=phone , appartment=appartment , ownerid=ownerid)
        comp1.save()
        messages.success(request, 'Details successfully registered')
        return redirect ('/mysoc')
    return render(request, 'dependents.html' )

def LogoutUser (request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('/')

def payment (request):
    #return HttpResponse("This is Contact Page")
    return render(request, 'payment.html')

def forgotpassword (request):
    if request.method == "POST":
        messages.success(request, 'Password reset link has been sent to your email id')
        return redirect('/')

    return render(request, 'forgotpassword.html')