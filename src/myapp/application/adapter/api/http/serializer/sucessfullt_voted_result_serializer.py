"""
Serializer for SuccessfullyVotedResult.
"""
from rest_enumfield import EnumField
from rest_framework import serializers

from myapp.application.domain.model.vote_for_article_result import SuccessfullyVotedResult
from myapp.application.domain.model.vote import Vote


class SuccessfullyVotedResultSerializer(
    serializers.Serializer[SuccessfullyVotedResult]
):
    user_id = serializers.UUIDField()
    article_id = serializers.UUIDField()
    vote = EnumField(Vote)
