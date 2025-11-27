#from django.contrib import admin
from django.contrib.gis import admin
from .models import KenyaConflictData

@admin.register(KenyaConflictData)
class KenyaConflictDataAdmin(admin.GISModelAdmin):
    # Fields to display in the list view
    list_display = ('event_type', 'event_date', 'location', 'fatalities', 'country')
    
    # Enable filtering by these fields
    list_filter = ('event_type', 'year', 'country', 'region','event_date')
    
    # Enable search for these fields
    search_fields = ('location', 'event_type', 'sub_event_type', 'actor1', 'actor2')
    
    # Date-based navigation
    date_hierarchy = 'event_date'
    
    # Fields to show in the detail view
    fieldsets = (
        ('Event Information', {
            'fields': ('event_date', 'year', 'event_type', 'sub_event_type', 'disorder_type')
        }),
        ('Location', {
            'fields': ('country', 'region', 'admin1', 'admin2', 'location', 'latitude', 'longitude', 'shape')
        }),
        ('Actors', {
            'fields': ('actor1', 'assoc_actor_1', 'actor2', 'assoc_actor_2', 'interaction')
        }),
        ('Details', {
            'fields': ('fatalities', 'source', 'notes', 'tags')
        }),
    )
    
    # OpenLayers widget settings for the map
    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js'
    default_lon = 37.9062  # Center of Kenya (approximate)
    default_lat = 0.0236
    default_zoom = 6
    
    # Make the map read-only since we're using managed=False
    modifiable = False
    
    # Disable the ability to add new records since we're using managed=False
    def has_add_permission(self, request):
        return False
        
    # Disable the ability to delete records since we're using managed=False
    def has_delete_permission(self, request, obj=None):
        return False
