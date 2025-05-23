from uuid import UUID

import pytest

from myapp.application.domain.model.identifier.article_id import ArticleId
from myapp.application.domain.model.identifier.user_id import UserId
from myapp.application.domain.model.karma import Karma
from myapp.application.domain.model.vote import Vote
from myapp.application.domain.model.vote_for_article_result import AlreadyVotedResult
from myapp.application.domain.model.voting_user import ArticleVote, VotingUser


def test_vote_for_article_twice_returns_already_voted_result(
    voting_user_who_has_voted: VotingUser,
    article_id_for_which_user_has_voted: ArticleId,
    a_vote: Vote,
    expected_already_voted_result: AlreadyVotedResult
):
    voting_result = voting_user_who_has_voted.vote_for_article(
        article_id_for_which_user_has_voted,
        a_vote
    )
    assert voting_result == expected_already_voted_result

@pytest.fixture(scope='module')
def article_id_for_which_user_has_voted() -> ArticleId:
    return ArticleId(UUID('4df32c92-0000-0000-0000-000000000000'))

@pytest.fixture(scope='module')
def voting_user_who_has_voted() -> VotingUser:
    return VotingUser(
        UserId(UUID('7ebd50e7-0000-0000-0000-000000000000')),
        Karma(10),
        [
            ArticleVote(
                ArticleId(UUID('4df32c92-0000-0000-0000-000000000000')),
                UserId(UUID('7ebd50e7-0000-0000-0000-000000000000')),
                Vote.DOWN
            )
        ]
    )

@pytest.fixture(scope='module')
def expected_already_voted_result() -> AlreadyVotedResult:
    return AlreadyVotedResult(
        ArticleId(UUID('4df32c92-0000-0000-0000-000000000000')),
        UserId(UUID('7ebd50e7-0000-0000-0000-000000000000'))
    )
