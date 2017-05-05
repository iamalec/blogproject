from django.contrib import admin
from blog.models import BBS,BBS_user,Category

class bbsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary',  'author', 'signature', 'view_count', 'create_at')
    def signature(self, obj):
        return obj.author.signature
    signature.short_description = 'hah'
admin.site.register(BBS, bbsAdmin)
admin.site.register(BBS_user, )
admin.site.register(Category, )
