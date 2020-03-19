from django.contrib import admin

# Register your models here.
# 关于后台管理站点的配置
from .models import  Post, Category, Tag



class PostAdmin(admin.ModelAdmin):
    list_display =  ['title', 'created_time', 'modified_time', 'category']
    list_display_links = ['title', 'created_time']
    search_fields = ['title']
    list_per_page = 5

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

