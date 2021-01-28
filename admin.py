from django.contrib import admin

# Register your models here.
from .models import user_login, company_details, user_details, category_master, app_master, app_review, app_pic, \
    data_set, sub_category_master

admin.site.register(user_login)
admin.site.register(company_details)
admin.site.register(user_details)
admin.site.register(category_master)
admin.site.register(app_master)
admin.site.register(app_review)
admin.site.register(app_pic)
admin.site.register(data_set)
admin.site.register(sub_category_master)