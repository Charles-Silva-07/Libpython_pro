from unittest.mock import Mock

import pytest

from libpythonpro import github_api

#
# def test_buscar_avatar():
#     avatar_url = avatar_url()
#     url = github_api.buscar_avatar('Charles-silva-07')
#     assert avatar_url == url


@pytest.fixture()
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/80009663?v=4'
    resp_mock.json.return_value = {
        'login': 'Charles-Silva-07', 'id': 80009663, 'node_id': 'MDQ6VXNlcjgwMDA5NjYz',
        'avatar_url': url
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original
    return url


def test_buscar_avatar_integracao(avatar_url):
    url = github_api.buscar_avatar('Charles-silva-07')
    assert 'https://avatars.githubusercontent.com/u/80009663?v=4' == url
