from typing import Optional

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.orm import (
    registry,
    Mapped,
    mapped_column
)

from roadmap_ai.enums import RoadmapStatus

table_registry = registry()

@table_registry.mapped_as_dataclass
class Roadmap:
    __tablename__ = "roadmaps"

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    status: Mapped[RoadmapStatus] = mapped_column(SQLAlchemyEnum(RoadmapStatus), nullable=False)
    skill: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[Optional[str]] = mapped_column(nullable=True, default=None)
