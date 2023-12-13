from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import people
from .form import Editform_info

# Create your views here.

def home(request):
    
     peoples = people.objects.all()
     context = {'people': peoples}
     return render(request, 'home.html', context)
    

    #return HttpResponse("homepage")
def person_details(request,id):
 
    # querying a particular book by its id
    person = people.objects.get(pk=id)
    print(person)
    context = {'person': person}
    return render(request, 'person_details.html', context)
  
def add_person(request):
    if request.method=="POST":
        data=request.POST
        person=people.objects.create(name=data["firstname"],place_of_birth=data["place_of_birth"],company=data["company"])
        return redirect('home')
      
    
                                     
                                     
                                     
  
    return render(request, 'add_person.html')
def remove_person(request,id):
    person=people.objects.get(pk=id)
    if request.method=="POST":
        person.delete()
        return redirect('home')
    context = {'person': person}
    
    #return HttpResponse("removing ")
    return render(request, 'delete_person.html', context)

def edit_info(request,id):


    person=people.objects.get(pk=id)
    form=Editform_info(instance=person)
    if request.method=="POST":
        form=Editform_info(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={"form":form}

    return render(request,'update_info.html',context)

