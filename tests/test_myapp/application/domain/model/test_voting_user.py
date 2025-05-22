from myapp.application.domain.model.vote_for_article_result import AlreadyVotedResult


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
