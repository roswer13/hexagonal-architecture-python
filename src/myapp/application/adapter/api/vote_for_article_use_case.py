

from myapp.application.domain.model.vote_for_article_result import(
    VoteForArticleResult
)

class VoteForArticleUseCase(Protocol):
    def vote_for_article(self, command: VoteForArticleCommand) -> VoteForArticleResult:
        pass