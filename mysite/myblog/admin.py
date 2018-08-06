from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

# Create inline editing template for Category in Post Admin
class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]

# Exclude posts from category admin window
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

