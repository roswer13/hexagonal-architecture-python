"""
Port interface for finding a voting user.
"""

from typing import Protocol


class FindVotingUserPort(Protocol):
    def find_voting_user(self, article_id: ArticleId, user_id: UserId) -> VotingUser:
        raise NotImplementedError()
