from django import template

register = template.Library()

@register.filter
def duration_string(value):
    """Convert timedelta to human readable string"""
    total_seconds = int(value.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    
    if hours > 0:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes} minutes"
