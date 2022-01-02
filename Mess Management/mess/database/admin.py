from django.contrib import admin
#from django.contrib.auth import Group
from database.models import *
# Register your models here.

admin.site.site_header = 'LNMIIT Mess Management Admin Panel'

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=('StudentID','Firstname', 'Lastname', 'Number', 'Address', 'Email', 'roll_num')
    search_fields = ['roll_num', 'Firstname', 'Lastname',]
    list_filter = ('roll_num', 'Firstname', 'Lastname')
    

@admin.register(MessWorker)
class AdminMessWorker(admin.ModelAdmin):
    list_display=('WorkerID','Name', 'Email', 'Number','Gender', 'Address', 'Document')


@admin.register(Coupon)
class AdminCoupon(admin.ModelAdmin):
     list_display=('Coupon_ID', 'Date', 'Breakfast', 'Lunch', 'Evening_snacks', 'Dinner')
     date_hierarchy = 'Date'


@admin.register(ComplaintRecord)
class AdminComplaintRecord(admin.ModelAdmin):
    list_display=('Complaint_ID','Subject', 'Description', 'Status', 'Comments', 'Date')
    search_fields = ['Complaint_ID', 'Status',]
    date_hierarchy = 'Date'
    list_filter = ('Complaint_ID', 'Status')

admin.site.register(MessMenu)