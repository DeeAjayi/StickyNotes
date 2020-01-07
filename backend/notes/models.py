import uuid
from django.db import models


class Notes(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=30, unique=True, null=False, blank=False)
	description = models.CharField(max_length=250)
	content = models.TextField()
	time_stamp = models.DateTimeField(auto_now_add=True)
	is_public = models.BooleanField(default=True)
