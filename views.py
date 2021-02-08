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


def admin_view_users(request):
    user_list = user_login.objects.filter(utype='user')
    context= {'user_list':user_list}
    return render(request,'./myapp/admin_view_users.html',context)

def admin_view_company(request):
    company_list = user_login.objects.filter(utype='company')
    context= {'company_list':company_list}
    return render(request,'./myapp/admin_view_company.html',context)


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

from .models import sub_category_master
def admin_add_sub_category(request):
    if request.method == 'POST':
        sub_category_name =request.POST.get('sub_category_name')
        category_master_id = int(request.POST.get('category_master_id'))

        sub_list = sub_category_master(sub_category_name=sub_category_name,category_master_id=category_master_id)
        sub_list.save()
        context = {'msg': 'Sub Category Added Successfully'}
        cat_list = category_master.objects.all()
        context = {'node_list': cat_list}
        return render(request, 'myapp/admin_add_sub_category.html',context)

    else:
        cat_list = category_master.objects.all()
        context = {'node_list': cat_list}
        return render(request, 'myapp/admin_add_sub_category.html',context)

def admin_delete_sub_category(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = sub_category_master.objects.get(id=int(id))
    nm.delete()

    msg = 'deleted'
    cm_l = category_master.objects.all()
    cmd = {}
    for cm in cm_l:
        cmd[cm.id] = cm.category_name

    st_l = sub_category_master.objects.all()
    context ={'subcategory_list':st_l,'category_list':cmd}
    return render(request,'myapp/admin_view_sub_category.html',context)

def admin_view_sub_category(request):
    cat_list = category_master.objects.all()
    cmd = {}
    for cd in cat_list:
        cmd[cd.id] = cd.category_name

    sub_list = sub_category_master.objects.all()
    context = {'sub_list':  sub_list, 'category_list': cmd}
    return render(request, 'myapp/admin_view_sub_category.html', context)


from .models import data_set

def admin_add_dataset(request):
    if request.method == "POST":
        sentiment_type = request.POST.get('sentiment_type')
        data_keys = request.POST.get('data_keys')

        data_list = data_set(sentiment_type=sentiment_type, data_keys=data_keys)
        data_list.save()
        context = {'msg': 'Data Set Added Successfully'}
        return render(request, './myapp/admin_add_dataset.html', context)
    else:
        return render(request, './myapp/admin_add_dataset.html')

def admin_view_dataset(request):
        data_list = data_set.objects.all()
        msg = ''
        context = {'msg': msg, 'data_list': data_list}
        return render(request, './myapp/admin_view_dataset.html', context)

def admin_delete_dataset(request):
    id = request.GET.get('id')
    dd = data_set.objects.get(id=int(id))
    dd.delete()

    msg = 'deleted'
    data_list = data_set.objects.all()
    context = {'msg': msg, 'data_list': data_list}
    return render(request, './myapp/admin_view_dataset.html', context)

def admin_view_app(request):
        app_list = app_master.objects.all()
        msg = ''
        context = {'msg': msg, 'app_list': app_list}
        return render(request, './myapp/admin_view_app.html', context)


########################## COMPANY ###############################

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


from datetime import datetime
from django.db.models import Max
from .models import company_details
from django.core.files.storage import FileSystemStorage
def company_registration(request):
    if request.method == 'POST':
        u_file = request.FILES['logo']
        fs = FileSystemStorage()
        c_logo = fs.save(u_file.name, u_file)
        #user_id = request.POST.get('user_id')
        c_name = request.POST.get('c_name')
        c_descp = request.POST.get('c_descp')
        c_addr1 = request.POST.get('c_addr1')
        c_addr2 = request.POST.get('c_addr2')
        c_addr3 = request.POST.get('c_addr3')
        c_pincode = request.POST.get('c_pincode')
        c_email = request.POST.get('c_email')
        c_contact1 = request.POST.get('c_contact1')
        c_contact2 = request.POST.get('c_contact2')
        c_url = request.POST.get('c_url')
        c_dt = datetime.today().strftime('%Y-%m-%d')
        c_tm = datetime.today().strftime('%H:%M:%S')
        c_status = "new"
        password='1234'


        ul = user_login(uname=c_email, passwd=password, utype='company')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = company_details(user_id=user_id, c_name=c_name, c_descp=c_descp, c_addr1=c_addr1, c_addr2=c_addr2, c_addr3=c_addr3, c_pincode=c_pincode, c_email=c_email,
                          c_contact1=c_contact1, c_contact2=c_contact2, c_url=c_url, c_dt=c_dt, c_tm=c_tm, c_status=c_status,c_logo=c_logo)
        ud.save()

        print(user_id)
        context={'msg':'Company Registered'}
        return render(request, 'myapp/company_login.html', context)

    else:
        return render(request, 'myapp/company_registration.html')

from .models import app_master
def company_add_app(request):
    if request.method == 'POST':

        app_name = request.POST.get('app_name')
        comapny_details_id = int(request.POST.get('comapny_details_id'))
        sub_category_master_id = int(request.POST.get('sub_category_master_id'))
        product_descp = request.POST.get('product_descp')
        product_price = request.POST.get('product_price')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = "new"
        password = '1234'

        app_list = app_master(app_name=app_name, comapny_details_id=comapny_details_id, sub_category_master_id=sub_category_master_id, product_descp=product_descp,
                              product_price=product_price, dt=dt, tm=tm, status=status)
        app_list.save()
        context = {'msg': 'App Added Successfully'}
        app_list = app_master.objects.all()
        context = {'app_list': app_list}
        return render(request, 'myapp/company_add_app.html',context)

    else:
        app_list = app_master.objects.all()
        context = {'app_list': app_list}
        return render(request, 'myapp/company_add_app.html',context)

def company_delete_app(request):
    id = request.GET.get('id')
    al = app_master.objects.get(id=int(id))
    al.delete()

    msg = 'deleted'
    app_list = app_master.objects.all()
    context = {'msg': msg, 'app_list': app_list}
    return render(request, './myapp/company_view_app.html', context)

def company_view_app(request):
        app_list = app_master.objects.all()
        msg = ''
        context = {'msg': msg, 'app_list': app_list}
        return render(request, './myapp/company_view_app.html', context)


####################### USER ################################

from .models import user_login
def user_login2(request):
      if request.method == 'POST':
        uname=request.POST.get('uname')
        password = request.POST.get('password')
        # select query
        user_list = user_login.objects.filter(uname=uname, passwd=password, utype='user')

        if len(user_list) == 1:
            #setting session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            print ('user_id', request.session['user_id'])
            context = {'uname': user_list[0].uname.upper()}
            return render(request,'./myapp/user_home.html')
        else:
            context = {'msg':'Invalid Credentials'}
            return render(request,'./myapp/user_login.html',context)
      else:
        return render(request,'./myapp/user_login.html')

def user_home(request):
    context = {'uname': 'user'}
    return render(request,'./myapp/user_home.html')


from datetime import datetime
from django.db.models import Max
from .models import user_details
def user_registration(request):
    if request.method == 'POST':

        #user_id = request.POST.get('user_id')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        addr = request.POST.get('addr')
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = "new"
        password='1234'


        ul = user_login(uname=email, passwd=password, utype='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(f_name=f_name, l_name=l_name,dob=dob, gender=gender, addr=addr, pincode=pincode, email=email,
                          contact=contact,  dt=dt, tm=tm, status=status)
        ud.save()

        print(user_id)
        context={'msg':'User Registered'}
        return render(request, 'myapp/user_login.html', context)

    else:
        return render(request, 'myapp/user_registration.html')

def user_change_password(request):
    if request.method == 'POST':
        opasswd=request.POST.get('opswd')
        npasswd=request.POST.get('npswd')
        try:
            uname = request.session['user_name'] #reading session
        except:
            return render(request, './myapp/user_login.html')
        try:
            user1 = user_login.objects.get(uname=uname, passwd=opasswd, utype='user')
            #update query
            user1.passwd = npasswd
            user1.save()
            context = {'msg': 'password changed'}
            return render(request, './myapp/user_change_password.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'invalid old password'}
            return render(request, './myapp/user_change_password.html', context)
    else:
         return render(request, './myapp/user_change_password.html')

def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
        return user_login2(request)
    #except works if no session is setted
    except:
        return user_login2(request)

def user_view_company(request):
    company_view = user_login.objects.filter(utype='company')
    context= {'company_view':company_view}
    return render(request,'./myapp/user_view_company.html',context)

def user_view_app(request):
    app_list = app_master.objects.all()
    msg = ''
    context = {'msg': msg, 'app_list': app_list}
    return render(request, './myapp/user_view_app.html', context)


from .models import app_review
def user_add_app_reviews(request):
    if request.method == "POST":
        app_master_id = 1#int(request.POST.get('app_master_id'))
        user_id = int(request.session['user_id'])
        rating = int(request.POST.get('rating'))
        review = request.POST.get('review')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = "ok"

        ar = app_review(app_master_id=int(app_master_id), user_id=int(user_id), rating=int(rating), review=review,
                             dt=dt, tm=tm, status=status)
        ar.save()
        context = {'msg': 'Review added', 'app_master_id': app_master_id}
        return render(request, 'myapp/user_add_app_reviews.html', context)

    else:
        app_master_id = request.GET.get('app_master_id')
        context = {'msg': '', 'app_master_id': app_master_id}
        return render(request, 'myapp/user_add_app_reviews.html', context)

def user_view_app_reviews(request):
    review_list = app_review.objects.all()
    msg = ''
    context = {'msg': msg, 'review_list': review_list}
    return render(request, './myapp/user_view_app_reviews.html', context)

def user_delete_app_reviews(request):
    id = request.GET.get('id')
    ar = app_review.objects.get(id=int(id))
    ar.delete()

    msg = 'deleted'
    review_list = app_review.objects.all()
    context = {'msg': msg, 'review_list': review_list}
    return render(request, './myapp/user_delete_app_reviews.html', context)


