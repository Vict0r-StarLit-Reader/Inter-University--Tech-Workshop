from django.contrib import admin
from .models import Speaker, Schedule, Registration

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'organization', 'topic']
    search_fields = ['name', 'organization']
    list_filter = ['organization']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'duration', 'location', 'description']
    search_fields = ['location', 'description']
    list_filter = ['location']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'email', 'registration_date']
    search_fields = ['name', 'organization']
    list_filter = ['registration_date']
