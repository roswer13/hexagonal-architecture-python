class ArticleVoteView(APIView):

    def __init__(self, vote_for_article_use_case: VoteForArticleUseCase):
        self.vote_for_article_use_case = vote_for_article_use_case
        super().__init__()

    def post(self, request: Request) -> Response:
        vote_for_article_command = self._read_command(request)
        result = self.vote_for_article_use_case.vote_for_article(
            vote_for_article_command
        )
        return self._build_response(result)
