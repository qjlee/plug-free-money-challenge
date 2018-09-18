import pytest
import mock
from pytest_mock import mocker

from client.api_client import get_api_client
from key_manager import MockKeyManager
import plug_api

class FakeApiClient:
    uri: "hello"

def test_get_api_client(mocker):
    client = get_api_client()

    assert type(client.key_manager) is MockKeyManager
    assert type(client) is (plug_api.clients.v1.PlugApiClient)
