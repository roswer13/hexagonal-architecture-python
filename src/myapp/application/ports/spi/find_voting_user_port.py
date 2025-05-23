"""
Port interface for finding a voting user.
"""
from typing import Protocol

from myapp.application.domain.model.identifier.article_id import ArticleId
from myapp.application.domain.model.identifier.user_id import UserId
from myapp.application.domain.model.voting_user import VotingUser


class FindVotingUserPort(Protocol):
    def find_voting_user(self, article_id: ArticleId, user_id: UserId) -> VotingUser:
        raise NotImplementedError()
