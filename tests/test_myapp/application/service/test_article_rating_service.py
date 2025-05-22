import pytest

from myapp.application.domain.model.vote_for_article_result import(
    SuccessfullyVotedResult
)


@pytest.mark.usefixtures("atomic_transactions_noop_stub_for_article_service")
class TestArticleRatingService:
    def test_successfully_voted_for_article(
        self,
        vote_for_article_command: VoteForArticleCommand,
        successfully_voted_result: SuccessfullyVotedResult
    ):
        article_rating_service = build_article_rating_service()

        vote_for_article_result = article_rating_service.vote_for_article(
            vote_for_article_command
        )

        assert vote_for_article_result == successfully_voted_result

    def test_voting_user_saved(
        self,
        vote_for_article_command: VoteForArticleCommand,
        saved_voting_user: VotingUser
    ):
        save_voting_user_port_mock = SaveVotingUserPortMock()
        article_rating_service = build_article_rating_service(
            save_voting_user_port=save_voting_user_port_mock
        )

        article_rating_service.vote_for_article(vote_for_article_command)

        assert save_voting_user_port_mock.saved_voting_user == saved_voting_user
