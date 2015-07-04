from rest_framework import serializers
from general.models import Tag
# from ideas.serializers import IdeaSerializer


class TagSerializer(serializers.ModelSerializer):
	#tagged_ideas = IdeaSerializer(many=True, read_only=True)
	class Meta:
		model = Tag
		fields = ('id', 'name', 'tagged_ideas')
		# fields = ('id', 'name', 'slug', 'tagged_ideas')
		# read_only_fields = ('tagged_ideas')