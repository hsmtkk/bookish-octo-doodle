import faker
from fastapi import status
from fastapi.testclient import TestClient

import main

fake = faker.Faker("ja_JP")

client = TestClient(main.app)


def test_post_item(user_factory):
    user = user_factory()
    data = {"title": fake.word(), "user_id": user.id}
    resp = client.post("/item", json=data)
    assert resp.status_code == status.HTTP_200_OK


def test_get_item(item_factory):
    item_factory()
    resp = client.get("/item")
    assert resp.status_code == status.HTTP_200_OK
    got = resp.json()
    assert len(got) > 0


def test_get_item_id(item_factory):
    item = item_factory()
    resp = client.get(f"/item/{item.id}")
    assert resp.status_code == status.HTTP_200_OK
    got = resp.json()
    assert item.title == got["title"]


def test_post_user():
    data = {"email": fake.email()}
    resp = client.post("/user", json=data)
    assert resp.status_code == status.HTTP_200_OK


def test_get_user(user_factory):
    user = user_factory()
    resp = client.get("/user")
    assert resp.status_code == status.HTTP_200_OK
    got = resp.json()
    assert len(got) > 0


def test_get_user_id(user_factory):
    user = user_factory()
    resp = client.get(f"/user/{user.id}")
    assert resp.status_code == status.HTTP_200_OK
    got = resp.json()
    assert user.email == got["email"]
