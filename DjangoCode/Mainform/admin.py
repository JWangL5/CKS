from django.contrib import admin

# superuser：lw
# pwd:lw

# Register your models here.
from .models import users, notes, reviews, pictures



class usersAdmin(admin.ModelAdmin):

	list_display = ['uid', 'uid2', 'uname', 'uintro', 'upsg_count', 'ucolumn', 'usign_datetime']
	list_filter = ['ucolumn']
	search_fields = ['uname', 'uid2']
	list_pep_page = 15
	fields = ['uid2', 'uname', 'upwd', 'uintro', 'uhead', 'ucolumn','upsg_count']
	

class notesAdmin(admin.ModelAdmin):

	list_display = ['nid', 'ntitle', 'nauthor', 'ndatetime', 'ncolumn', 'ngood', 'nread']
	list_filter = ['ncolumn']
	search_fields = ['nauthor', 'nid', 'ntitle']
	list_pep_page = 15
	

admin.site.register(users, usersAdmin)
admin.site.register(notes, notesAdmin)