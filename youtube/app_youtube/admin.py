from django.contrib import admin
from .models import Users, Videos, Comments, Likes, Dislikes, UserViews

# Register your models here.
admin.site.register(Users)
admin.site.register(Videos)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Dislikes)
admin.site.register(UserViews)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('')