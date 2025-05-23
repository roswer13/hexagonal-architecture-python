import random
import pytest

from rest_framework.test import APIRequestFactory

from myapp.application.domain.model.vote import Vote


@pytest.fixture
def a_vote() -> Vote:
    return random.choice(list(Vote))


@pytest.fixture
def arf():
    return APIRequestFactory()
