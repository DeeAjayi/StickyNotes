from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notes
		fields = ('id', 'name', 'content', 'time_stamp', 'is_public')
