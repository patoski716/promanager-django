from rest_framework import serializers

from .models import Client,Project


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
            'created_by',
            'created_at',
            
        ),
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'created_at',
            'created_by',
        )

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        read_only_fields = (
            'created_by',
            'created_at',
            
        ),
        fields = (
            'id',
            'title',
            'description',
            'status',
            'client',
            'created_at',
            'created_by',
        )