from unittest import mock

from roadmap_ai.services.ai import OpenAIService

@mock.patch.object(OpenAIService, "get_roadmap")
def test_create_roadmap(mock_openai_get_roadmap, client):
    mock_openai_get_roadmap.return_value = "test content"

    expected_response = {
        'id': 1,
        'status': 'done',
        'skill': 'test',
        'content': 'test content'
    }

    response = client.post("/roadmaps", json={
        "skill": "test"
    })

    assert response.status_code == 201
    assert response.json() == expected_response

def test_retrieve_roadmap(client, roadmap):
    expected_response = {
        'id': 1,
        'status': 'done',
        'skill': 'test',
        'content': 'test content'
    }

    response = client.get("/roadmaps/1")

    assert response.status_code == 200
    assert response.json() == expected_response
