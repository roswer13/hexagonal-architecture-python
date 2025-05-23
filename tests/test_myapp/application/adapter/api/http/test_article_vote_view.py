from http import HTTPStatus
from uuid import UUID

from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

from myapp.application.adapter.api.http.article_vote_view import ArticleVoteView
from myapp.application.adapter.api.vote_for_article_use_case import VoteForArticleUseCase
from myapp.application.domain.model.identifier.article_id import ArticleId
from myapp.application.domain.model.identifier.user_id import UserId
from myapp.application.domain.model.vote import Vote
from myapp.application.domain.model.vote_for_article_result import (
    AlreadyVotedResult,
    VoteForArticleResult
)
from myapp.application.ports.api.command.vote_for_article_command import (
    VoteForArticleCommand
)


def test_user_votes_for_the_same_article_returns_conflict(
    arf: APIRequestFactory
):
    # This is *the* view we are testing
    article_vote_view = ArticleVoteView.as_view(
        # we are injecting a stub which always
        # returns AlreadyVotedResult (see below)
        vote_for_article_use_case=VoteForArticleUseCaseAlreadyVotedStub()
    )

    # A valid article vote is POSTed
    response: Response = article_vote_view(
        arf.post(
            '/article_vote',
            {
                'user_id': UserId(UUID('a3854820-0000-0000-0000-000000000000')),
                'article_id': ArticleId(UUID('dd494bd6-0000-0000-0000-000000000000')),
                'vote': Vote.UP.value
            },
            format='json'
        )
    )

    # But the result is HTTP 409, as defined in the specification
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.data == {
        'status': 409,
        'detail': "User \"a3854820-0000-0000-0000-000000000000\" has already voted"
        " for article \"dd494bd6-0000-0000-0000-000000000000\"",
        'title': "Cannot vote for an article"
    }


class VoteForArticleUseCaseAlreadyVotedStub(VoteForArticleUseCase):
    def vote_for_article(self, command: VoteForArticleCommand) -> VoteForArticleResult:
        return AlreadyVotedResult(
            user_id=command.user_id,
            article_id=command.article_id
        )
