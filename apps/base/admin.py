from django.contrib import admin
from apps.base.models import *

# Register your models here.
admin.site.register(Admin)
admin.site.register(Banner)
admin.site.register(AboutUs)
admin.site.register(Contact)
admin.site.register(ContactPost)
admin.site.register(Footer)
admin.site.register(FooterPost)
admin.site.register(Facilties)
admin.site.register(NewsBackground)
admin.site.register(Video)

# class ContactPostInline(admin.TabularInline):
#     model = ContactPost
#     extra = 0

# class ContactFilterAdmin(admin.ModelAdmin):
#     inlines = [ContactPostInline]

# admin.site.register(Contact, ContactFilterAdmin)


# class FooterPostInline(admin.TabularInline):
#     model = FooterPost
#     extra = 0

# class FooterFilterAdmin(admin.ModelAdmin):
#     inlines = [FooterPostInline]

# admin.site.register(Footer, FooterFilterAdmin)


class TeamInline(admin.TabularInline):
    model = Team
    extra = 0

class TeamPageFilterAdmin(admin.ModelAdmin):
    inlines = [TeamInline]

admin.site.register(TeamPage, TeamPageFilterAdmin)

class GallaryInline(admin.TabularInline):
    model = Gallery
    extra = 0

class GalleryPageFilterAdmin(admin.ModelAdmin):
    inlines = [GallaryInline]

admin.site.register(GalleryPage, GalleryPageFilterAdmin)