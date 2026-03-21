import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    # Arrange: No special setup needed as activities are predefined

    # Act: Make GET request to /activities
    response = client.get("/activities")

    # Assert: Check status code and response content
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert "Chess Club" in activities
    assert "Basketball Team" in activities


def test_signup_for_activity():
    # Arrange: Choose an activity with available spots
    activity_name = "Basketball Team"
    email = "test@mergington.edu"

    # Act: Make POST request to signup
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert: Check success and message
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert f"Signed up {email} for {activity_name}" in data["message"]

    # Verify the participant was added
    response = client.get("/activities")
    activities = response.json()
    assert email in activities[activity_name]["participants"]


def test_prevent_duplicate_signup():
    # Arrange: Sign up first
    activity_name = "Basketball Team"
    email = "duplicate@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act: Try to sign up again
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert: Should fail with 400
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"]


def test_unregister_from_activity():
    # Arrange: Sign up first
    activity_name = "Soccer Club"
    email = "unregister@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act: Make DELETE request to unregister
    response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    # Assert: Check success
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert f"Unregistered {email} from {activity_name}" in data["message"]

    # Verify the participant was removed
    response = client.get("/activities")
    activities = response.json()
    assert email not in activities[activity_name]["participants"]


def test_signup_nonexistent_activity():
    # Arrange: Use a non-existent activity
    activity_name = "Nonexistent Activity"
    email = "test@mergington.edu"

    # Act: Try to sign up
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert: Should fail with 404
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]


def test_unregister_not_signed_up():
    # Arrange: Try to unregister without being signed up
    activity_name = "Drama Club"
    email = "notsigned@mergington.edu"

    # Act: Make DELETE request
    response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    # Assert: Should fail with 400
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "not signed up" in data["detail"]