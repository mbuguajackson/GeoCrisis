from django.contrib.gis.db import models

class KenyaConflictData(models.Model):
    """
    Model representing the kenya_conflict_data table in the jack schema.
    This table contains conflict event data with geographic information.
    """
    objectid = models.AutoField(primary_key=True)
    field1 = models.IntegerField(blank=True, null=True)
    event_id_cnty = models.CharField(max_length=8000, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    time_precision = models.IntegerField(blank=True, null=True)
    disorder_type = models.CharField(max_length=8000, blank=True, null=True)
    event_type = models.CharField(max_length=8000, blank=True, null=True)
    sub_event_type = models.CharField(max_length=8000, blank=True, null=True)
    actor1 = models.CharField(max_length=8000, blank=True, null=True)
    assoc_actor_1 = models.CharField(max_length=8000, blank=True, null=True)
    inter1 = models.CharField(max_length=8000, blank=True, null=True)
    actor2 = models.CharField(max_length=8000, blank=True, null=True)
    assoc_actor_2 = models.CharField(max_length=8000, blank=True, null=True)
    inter2 = models.CharField(max_length=8000, blank=True, null=True)
    interaction = models.CharField(max_length=8000, blank=True, null=True)
    civilian_targeting = models.CharField(max_length=8000, blank=True, null=True)
    iso = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=8000, blank=True, null=True)
    country = models.CharField(max_length=8000, blank=True, null=True)
    admin1 = models.CharField(max_length=8000, blank=True, null=True)
    admin2 = models.CharField(max_length=8000, blank=True, null=True)
    admin3 = models.CharField(max_length=8000, blank=True, null=True)
    location = models.CharField(max_length=8000, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    geo_precision = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=8000, blank=True, null=True)
    source_scale = models.CharField(max_length=8000, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)  # Using TextField for potentially long notes
    fatalities = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=8000, blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    gdb_geomattr_data = models.BinaryField(blank=True, null=True)
    shape = models.GeometryField(srid=4326, blank=True, null=True)  # Assuming WGS84 (SRID 4326)

    class Meta:
        managed = False  # Set to False since the table already exists
        db_table = 'jack"."kenya_conflict_data'  # Schema-qualified table name
        verbose_name = 'Kenya Conflict Event'
        verbose_name_plural = 'Kenya Conflict Events'
        ordering = ['-event_date']

    def __str__(self):
        return f"{self.event_type} - {self.location} ({self.event_date})"