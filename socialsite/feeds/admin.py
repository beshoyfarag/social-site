from django.contrib import admin
from feeds.models import Post
class PostAdmin(admin.ModelAdmin):
 list_display= ('heading','body','date','user')
 search_fields = ('heading','body','date','user')

admin.site.register(Post,PostAdmin)
