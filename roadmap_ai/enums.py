import enum

class RoadmapStatus(str, enum.Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"
