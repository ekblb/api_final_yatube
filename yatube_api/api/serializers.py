from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', read_only=True, default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following', 'user']
            )
        ]

    def validate_following(self, following):
        if self.context.get('request').user == following:
            raise serializers.ValidationError(
                'Подписка на самого себя невозможна'
            )
        return following
