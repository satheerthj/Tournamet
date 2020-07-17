from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration 
import random
import datetime
import itertools
# Create your views here.
def home(request):
    return render(request,'register.html',{'name':'TOURNAMENT REGISTRATION'})
def display(request):
    if request.method == 'POST':
        register = Registration()
        count = Registration.objects.all().count()
        if count ==10:
            message = 'Registraion Full'
            return render(request , 'teams.html',{'message' : message})
        teamname = request.POST['teamname']
        teamnum = int(request.POST['teamnum'])
        manager = request.POST['manger']
        coach = request.POST['coach']
        
        register.team_name = teamname
        register.team_members = teamnum
        register.manager = manager
        register.coach = coach
        register.save()
        return redirect('/')
    else:
        return render(request , 'teams.html',{'dis' : teamname})
def match(request):
    venues = ['delhi','chennai','kolata','kerala','mumbai']
    teams = Registration.objects.all()
    ids= [data.id for data in teams]
    team_names = [data.team_name for data in teams]
    date = datetime.datetime(2020,12,1,12,3,5)
    dates = []
    li = []
    l = []
    for i in range(0,len(ids)):
        li.insert(i,i+1)  
    match_pair = list(itertools.combinations(li,2))
    c = 0
    l = []
    a = []
    b = False
    print('Starting')
    list_copy = match_pair.copy()
    x = len(match_pair)
    for i in range(0,x):      
        if len(a) > 0:
           
            for j in list_copy:
                b = False
                for k in a:
                    if k in j:
                        b= True
                        break
                if b == True:
                    
                    continue
                else:

                    print(j)
                    l.append(j)
                    a = j
                    list_copy.remove(a)
        else:
            print(list_copy[0])
            a = list_copy[0]
            l.append(a)
            list_copy.pop(0)
    print(l)
    v = []
    for i in range(1,x+1):
        date += datetime.timedelta(days =1)
        dates.insert(i,date)
        a = random.choice(venues)
        v.append(a)
    print(dates[0])
    print(len(dates))
    print(len(l))
    p1 = []
    p2 = []
    li = []
    for i in l:
        k1 = team_names[i[0]-1]
        k2 = team_names[i[1]-1] 
        p1.append(k1)
        p2.append(k2)
    li = [i for i in range(1,len(l)+1)]
    print(p1)
    print(p2)
    print(li)
    final_list= zip(dates,v,p1,p2,li)
    return render(request , 'matchmaking.html',{'final':final_list })
