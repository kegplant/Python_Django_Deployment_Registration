from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from models import Users
import bcrypt
from django.contrib.messages import error
   
# the index function is called when root is visited
def isLoggedIn(request):
    try:
        request.session['user_id']
        return True
    except:
        return False
def index(request):
    context={
        'status':isLoggedIn(request)
    }
    return render(request,'logIn_registration/index.html',context)

def register(request):
    errors=Users.objects.registration_validator(request.POST)
    if errors:
        for tag,message in errors.items():
            error(request,message,extra_tags=tag)
        return redirect('/')
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        hash1=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        bday= request.POST['birth_day']
        user=Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=hash1,birth_day=bday)
        request.session['user_id']=user.id      
        return redirect('/'+str(user.id)+'/success')
def logIn(request):
    errors=Users.objects.logIn_validator(request.POST)
    if errors:
        for tag,message in errors.items():
            error(request,message,extra_tags=tag)
        return redirect('/')
    else:
        user=Users.objects.filter(email=request.POST['email'])[0]
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
            request.session['user_id']=user.id
            return redirect('/'+str(user.id)+'/success')
def process(request):
    if request.method=='POST':
        if request.POST['type']=='register':            
            return register(request)
        if request.POST['type']=='log in':            
            return logIn(request)
    return redirect('/')

def success(request,id):
    if not isLoggedIn(request):
        return redirect('/')
    user=Users.objects.get(id=id)
    context={
        'user': user,
    }
    return render(request,'logIn_registration/success.html',context)

def clear(request):
    Users.objects.all().delete()
    return redirect('/')
def logOut(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def friends(request):
    if not isLoggedIn(request):
        return redirect('/')
    user=Users.objects.get(id=request.session['user_id'])
    context={
        'user':user,
        'users':Users.objects.all().exclude(friends=user).exclude(id=user.id)
    }
    return render(request,'logIn_registration/friends.html',context)
def friends_add(request):
    if request.method=='POST':
        user=Users.objects.get(id=request.session['user_id'])
        newFriend=Users.objects.all().exclude(friends=user).exclude(id=user.id).filter(id=request.POST['friend_id'])
        if not newFriend:
            error(request,'Your friend request does not make sense')
            return redirect('/friends')
        user.friends.add(newFriend[0])
    return redirect('/friends')
def friends_remove(request):
    if request.method=='POST':
        user=Users.objects.get(id=request.session['user_id'])
        oldFriend=user.friends.filter(id=request.POST['friend_id'])
        if not oldFriend:
            error(request,'You are not friends.')
            return redirect('/friends')
        user.friends.remove(oldFriend[0])
    return redirect('/friends')
def user_show(request,id):
    if not isLoggedIn(request):
        return redirect('/')
    user=Users.objects.filter(id=id)
    if not user:
        error(request,'User does not exist')
        return redirect('/friends')
    context={
        'user':user[0]
    }
    return render(request,'logIn_registration/user.html',context)

