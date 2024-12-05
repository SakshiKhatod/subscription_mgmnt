from enum import Enum


class SubscriptionCategory(Enum):
    def __init__(self) -> None:
        MUSIC = "MUSIC"
        VIDEO = "VIDEO"
        PODCAST = "PODCAST"
