from typing import List, cast

from myapp.application.adapter.spi.persistence.entity.article_vote_entity import (
    ArticleVoteEntity
)
from myapp.application.adapter.spi.persistence.entity.voting_user_entity import (
    VotingUserEntity
)
from myapp.application.adapter.spi.persistence.exceptions.voting_user_not_found import (
    VotingUserNotFound
)
from myapp.application.domain.model.identifier.article_id import ArticleId
from myapp.application.domain.model.identifier.user_id import UserId
from myapp.application.domain.model.karma import Karma
from myapp.application.domain.model.vote import Vote
from myapp.application.domain.model.voting_user import ArticleVote, VotingUser
from myapp.application.ports.spi.find_voting_user_port import FindVotingUserPort
from myapp.application.ports.spi.save_voting_user_port import SaveVotingUserPort


class VotingUserRepository(
    FindVotingUserPort,
    SaveVotingUserPort
):
    """
    VotingUserRepository is an interface that defines the methods for
    finding and saving voting users in the database.
    """

    def find_voting_user(self, article_id: ArticleId, user_id: UserId) -> VotingUser:
        """
        Find a voting user by article ID and user ID.

        :param article_id: The ID of the article.
        :param user_id: The ID of the user.
        :return: The voting user if found, otherwise None.
        """
        voting_user_entity = self._get_voting_user_entity(user_id)
        votes_for_articles = self._get_votes_for_articles(article_id, user_id)

        return VotingUser(
            user_id,
            Karma(voting_user_entity.karma),
            votes_for_articles
        )

    def _get_voting_user_entity(self, user_id: UserId) -> VotingUserEntity:
        try:
            return VotingUserEntity.objects.get(user_id=user_id)
        except VotingUserEntity.DoesNotExist as e:
            raise VotingUserNotFound(user_id) from e

    def _get_votes_for_articles(
        self,
        article_id: ArticleId,
        user_id: UserId
    ) -> List[ArticleVote]:
        article_vote_entity = ArticleVoteEntity.objects.filter(
            article_id=article_id,
            user_id=user_id
        ).first()

        if article_vote_entity is not None:
            article_vote = self._article_entity_to_domain_model(article_vote_entity)
            return [article_vote]
        else:
            return []

    def save_voting_user(self, voting_user: VotingUser) -> VotingUser:
        """
        Save a voting user to the database.

        :param voting_user: The voting user to save.
        :return: The saved voting user.
        """
        saved_article_vote_entities = self._save_votes_for_articles(
            voting_user.votes_for_articles
        )
        saved_votes_for_articles = [
            self._article_entity_to_domain_model(article_vote_entity)
            for article_vote_entity in saved_article_vote_entities
        ]

        return VotingUser(
            id=voting_user.id,
            karma=voting_user.karma,
            votes_for_articles=saved_votes_for_articles
        )

    def _article_vote_to_entity(self, article_vote: ArticleVote) -> ArticleVoteEntity:
        return ArticleVoteEntity(
            article_id=article_vote.article_id,
            user_id=article_vote.user_id,
            vote=cast(str, article_vote.vote.value)
        )

    def _article_entity_to_domain_model(self, entity: ArticleVoteEntity) -> ArticleVote:
        return ArticleVote(
            ArticleId(entity.article_id),
            UserId(entity.user_id),
            Vote(entity.vote)
        )
