import logging

from http import HTTPStatus
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session


from roadmap_ai.enums import RoadmapStatus
from roadmap_ai.models import Roadmap
from roadmap_ai.schemas.roadmap import RoadmapSchema, RoadmapPublicSchema
from roadmap_ai.services.ai import OpenAIService
from roadmap_ai.settings import get_session

router = APIRouter()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@router.post(
    "/roadmaps",
    status_code=HTTPStatus.CREATED,
    response_model=RoadmapPublicSchema
)
def create_roadmap(schema: RoadmapSchema, session: Session = Depends(get_session)):
    openai_service = OpenAIService()
    content = openai_service.get_roadmap(schema.skill)

    try:
        roadmap = Roadmap(skill=schema.skill, status=RoadmapStatus.done, content=content)
        session.add(roadmap)
        session.commit()
        session.refresh(roadmap)
    except Exception as exception:
        session.rollback()
        logger.exception(exception)
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Error creating roadmap"
        )

    return roadmap

@router.get("/roadmaps/{roadmap_id}", response_model=RoadmapPublicSchema)
def retrieve_roadmap(roadmap_id: int, session: Session = Depends(get_session)):
    roadmap = session.get(Roadmap, roadmap_id)

    if not roadmap:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return roadmap
