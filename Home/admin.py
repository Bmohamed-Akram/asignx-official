from django.contrib import admin
from Home.models import project,client_feedback,client_logo,contact,subscribe,about_count

# Register your models here.

admin.site.register(project)
admin.site.register(client_feedback)
admin.site.register(client_logo)
admin.site.register(contact)
admin.site.register(subscribe)
admin.site.register(about_count)