from fastapi.testclient import TestClient
from main import app
from peers.queries.peers import PeerQueries
client = TestClient(app)


class EmptyPeerQueries:
    def get_peer_request(self, user_id: int):
        return {
             "peerConnections": [
                {
                    "sender": 0,
                    "recipient": 0,
                    "status": "string",
                    "has_messaged": "string",
                    "sender_name": "string",
                    "recipient_name": "string"
                }
             ]
        }


def test_get_peer_request():
    app.dependency_overrides[PeerQueries] = EmptyPeerQueries
    response = client.get("/api/peer_connections/1/")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == {
            "peerConnections": []
        }
