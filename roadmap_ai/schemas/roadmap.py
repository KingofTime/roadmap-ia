from typing import Optional

from pydantic import BaseModel

from roadmap_ai.enums import RoadmapStatus


class RoadmapSchema(BaseModel):
    skill: str

class RoadmapPublicSchema(RoadmapSchema):
    id: int
    status: RoadmapStatus
    content: Optional[str] = None
