from django.contrib import admin
from .models import post,description,Category

class descriptionAdminInline(admin.TabularInline):
    model=description
    fields=['subject','message']
    extra=0

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','updated_time', 'Active']
    date_hierarchy='created_time'
    search_fields=['title','content']
    list_filter=('Active',)
    list_display_links=['id','title']
    inlines=[descriptionAdminInline]
    #list_editable=['Active']

admin.site.register(post,PostAdmin)
#admin.site.register(description)
admin.site.register(Category)
