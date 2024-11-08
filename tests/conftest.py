from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import Session

from roadmap_ai.main import app
from roadmap_ai.models import Roadmap
from roadmap_ai.models.roadmap import table_registry
from roadmap_ai.settings import get_session

@pytest.fixture
def client(session) -> Generator:
    def session_override():
        return session

    app.dependency_overrides[get_session] = session_override
    yield TestClient(app)

@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)

@pytest.fixture()
def roadmap(session):
    roadmap = Roadmap(skill="test", content="test content", status="done")

    session.add(roadmap)
    session.commit()
    session.refresh(roadmap)

    return roadmap
