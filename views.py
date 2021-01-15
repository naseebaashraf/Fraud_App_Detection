from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, './myapp/index.html')

from .models import user_login
def admin_login(request):
      if request.method == 'POST':
        uname=request.POST.get('uname')
        password = request.POST.get('password')
        # select query
        user_list = user_login.objects.filter(uname=uname, passwd=password, utype='admin')

        if len(user_list) == 1:
            #setting session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            context = {'uname': user_list[0].uname.upper()}
            return render(request,'./myapp/admin_home.html')
        else:
            context = {'msg':'Invalid Credentials'}
            return render(request,'./myapp/admin_login.html',context)
      else:
        return render(request,'./myapp/admin_login.html')

def admin_home(request):
    context = {'uname': 'admin'}
    return render(request,'./myapp/admin_home.html')

def admin_change_password(request):
    if request.method == 'POST':
        opasswd=request.POST.get('opswd')
        npasswd=request.POST.get('npswd')
        try:
            uname=request.session['user_name'] #reading session
        except:
            return render(request,'./myapp/admin_login.html')
        try:
            user1=user_login.objects.get(uname=uname,passwd=opasswd,utype='admin')
            #update query
            user1.passwd=npasswd
            user1.save()
            context = {'msg':'password changed'}
            return render(request, './myapp/admin_change_password.html',context)
        except user_login.DoesNotExist:
            context={'msg':'invalid old password'}
            return render(request,'./myapp/admin_change_password.html',context)
    else:
         return render(request,'./myapp/admin_change_password.html')

def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
        return admin_login(request)
    #except works if no session is setted
    except:
        return admin_login(request)


from .models import category_master

def admin_add_category(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')

        cat_list = category_master(category_name=category_name)
        cat_list.save()
        context={'msg':'Category Added Successfully'}
        return render(request,'./myapp/admin_add_category.html',context)
    else:
        return render(request,'./myapp/admin_add_category.html')


def admin_view_category(request):
        cat_list = category_master.objects.all()
        msg = ''
        context = {'msg': msg, 'cat_list': cat_list}
        return render(request, './myapp/admin_view_category.html', context)


def admin_delete_category(request):
    id = request.GET.get('id')
    cd = category_master.objects.get(id=int(id))
    cd.delete()

    msg = 'deleted'
    cat_list = category_master.objects.all()
    context = {'msg': msg, 'cat_list': cat_list}
    return render(request, './myapp/admin_view_category.html', context)

from .models import data_set

def admin_add_dataset(request):
    if request.method == "POST":
        sentiment_type = request.POST.get('sentiment_type')
        data_keys = request.POST.get('data_keys')

        data_list = data_set(sentiment_type=sentiment_type, data_keys=data_keys)
        data_list.save()
        context={'msg':'Data Set Added Successfully'}
        return render(request,'./myapp/admin_add_dataset.html',context)
    else:
        return render(request,'./myapp/admin_add_dataset.html')

#########################################################

from .models import user_login
def company_login(request):
      if request.method == 'POST':
        uname=request.POST.get('uname')
        password = request.POST.get('password')
        # select query
        user_list = user_login.objects.filter(uname=uname, passwd=password, utype='company')

        if len(user_list) == 1:
            #setting session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            context = {'uname': user_list[0].uname.upper()}
            return render(request,'./myapp/company_home.html')
        else:
            context = {'msg':'Invalid Credentials'}
            return render(request,'./myapp/company_login.html',context)
      else:
        return render(request,'./myapp/company_login.html')

def company_home(request):
    context = {'uname': 'company'}
    return render(request,'./myapp/company_home.html')

def company_change_password(request):
    if request.method == 'POST':
        opasswd=request.POST.get('opswd')
        npasswd=request.POST.get('npswd')
        try:
            uname=request.session['user_name'] #reading session
        except:
            return render(request,'./myapp/company_login.html')
        try:
            user1=user_login.objects.get(uname=uname,passwd=opasswd,utype='company')
            #update query
            user1.passwd=npasswd
            user1.save()
            context = {'msg':'password changed'}
            return render(request, './myapp/company_change_password.html',context)
        except user_login.DoesNotExist:
            context={'msg':'invalid old password'}
            return render(request,'./myapp/company_change_password.html',context)
    else:
         return render(request,'./myapp/company_change_password.html')

def company_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
        return company_login(request)
    #except works if no session is setted
    except:
        return company_login(request)

def company_registration(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        utype='company'
        #insert query
        user1=user_login(uname=uname,passwd=passwd,utype=utype)
        user1.save()
        context={'msg':'company registered successfully'}
        return render(request,'./myapp/company_login.html',context)
    else:
        return render(request,'./myapp/company_registration.html')






