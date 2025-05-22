"""
Service protocol interface for saving a voting user.
"""
from typing import Protocol

class SaveVotingUserPort(Protocol):
    """
    Port interface for saving a voting user.
    """

    def save_voting_user(self, article_id: str, user_id: str) -> None:
        """
        Save a voting user.

        :param article_id: The ID of the article.
        :param user_id: The ID of the user.
        """
        raise NotImplementedError()
