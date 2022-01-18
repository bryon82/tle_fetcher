import pytest


@pytest.fixture()
def true_fixture():
    return True


def smoke_test(true_fixture):
    assert true_fixture
