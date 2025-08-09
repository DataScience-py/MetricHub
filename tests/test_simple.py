"""Simple test to check if the server is up and running."""

from fastapi.testclient import TestClient


def test_simple(client: TestClient) -> None:
    """
    test_simple check if the server is up and running.

    Parameters
    ----------
    client : TestClient
        The client used to make the request to the server.
    """
    assert client.get("/").status_code == 200
