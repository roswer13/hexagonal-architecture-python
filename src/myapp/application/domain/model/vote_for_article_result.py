from dataclasses import dataclass


class VoteForArticleResult:
    pass


@dataclass
class InsufficientKarmaResult(VoteForArticleResult):
    user_id: UserId


@dataclass
class AlreadyVotedResult(VoteForArticleResult):
    article_id: ArticleId
    user_id: UserId


@dataclass
class SuccessfullyVotedResult(VoteForArticleResult):
    article_id: ArticleId
    user_id: UserId
    vote: Vote
