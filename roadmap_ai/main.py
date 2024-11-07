from http import HTTPStatus
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from roadmap_ai.enums import RoadmapStatus
from roadmap_ai.models import Roadmap
from roadmap_ai.schemas.roadmap import RoadmapSchema, RoadmapPublicSchema
from roadmap_ai.settings import get_session

app = FastAPI()

@app.post(
    "/roadmaps",
    status_code=HTTPStatus.CREATED,
    response_model=RoadmapPublicSchema
)
def create_roadmap(schema: RoadmapSchema, session: Session = Depends(get_session)):
    try:
        roadmap = Roadmap(skill=schema.skill, status=RoadmapStatus.NEW)

        session.add(roadmap)
        session.commit()
        session.refresh(roadmap)
    except:
        session.rollback()
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Error creating roadmap"
        )

    return roadmap

@app.get("/roadmaps/{roadmap_id}", response_model=RoadmapPublicSchema)
def retrieve_roadmap(roadmap_id: int, session: Session = Depends(get_session)):
    roadmap = session.get(Roadmap, roadmap_id)

    if not roadmap:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return roadmap
