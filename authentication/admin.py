from django.contrib import admin
from authentication.models import User, Token

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass

class TokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Token,TokenAdmin)
