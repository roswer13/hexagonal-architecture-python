"""
Model for a vote in the application.
"""
from dataclasses import dataclass

from src.myapp.application.domain.model.vote_for_article_result import(
    VoteForArticleResult,
    AlreadyVotedResult,
    SuccessfullyVotedResult,
    InsufficientKarmaResult
)


@dataclass
class VotingUser:
    """
    Model for a vote in the application.
    """
    id: UserId
    karma: Karma
    votes_for_articles: list[ArticleVote] = field(default_factory=list)

    def vote_for_article(
        self,
        article_id: ArticleId,
        vote: Vote
    ) -> VoteForArticleResult:
        if self._user_voted_for_article(article_id):
            return AlreadyVotedResult(article_id, self.id)

        if not self._karma_enough_for_voting():
            return InsufficientKarmaResult(user_id=self.id)

        ## IMPORTANT! The model state changes! ##
        self.votes_for_articles.append(
            ArticleVote(article_id, self.id, vote)
        )

        return SuccessfullyVotedResult(article_id, self.id, vote)