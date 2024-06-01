from dataclasses import dataclass;

@dataclass
class YoutrackConfigModel:
    url: str;
    project: str;
    token: str;