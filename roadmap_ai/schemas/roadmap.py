from pydantic import BaseModel

from roadmap_ai.enums import RoadmapStatus


class RoadmapSchema(BaseModel):
    skill: str

class RoadmapPublicSchema(RoadmapSchema):
    status: RoadmapStatus
    content: str
