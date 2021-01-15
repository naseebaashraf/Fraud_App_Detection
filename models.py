from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=50)
    passwd = models.CharField(max_length=25)
    utype = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class company_details(models.Model):
    user_id = models.IntegerField()
    c_name = models.CharField(max_length=50)
    c_descp = models.CharField(max_length=350)
    c_addr1 = models.CharField(max_length=250)
    c_addr2 = models.CharField(max_length=250)
    c_addr3 = models.CharField(max_length=250)
    c_pincode = models.CharField(max_length=10)
    c_email = models.CharField(max_length=150)
    c_contact1 = models.CharField(max_length=15)
    c_contact2 = models.CharField(max_length=15)
    c_url = models.CharField(max_length=150)
    c_dt = models.CharField(max_length=20)
    c_tm = models.CharField(max_length=20)
    c_status = models.CharField(max_length=5)
    c_logo = models.CharField(max_length=5)

class user_details(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=25)
    gender = models.CharField(max_length=7)
    addr = models.CharField(max_length=1000)
    pincode = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    dt = models.CharField(max_length=10)
    tm = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

class category_master(models.Model):
    category_name = models.CharField(max_length=100)

class sub_category_master(models.Model):
    sub_category_name = models.CharField(max_length=100)
    category_master_id = models.IntegerField()

class app_master(models.Model):
    app_name = models.CharField(max_length=100)
    comapny_details_id = models.IntegerField()
    sub_category_master_id = models.IntegerField()
    product_descp = models.CharField(max_length=1000)
    product_price = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

class app_review(models.Model):
    app_master_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField()
    review = models.CharField(max_length=1000)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

class app_pic(models.Model):
    product_master_id = models.IntegerField()
    pic_path = models.CharField(max_length=100)

class data_set(models.Model):
    sentiment_type = models.CharField(max_length=20)
    data_keys = models.CharField(max_length=300)





