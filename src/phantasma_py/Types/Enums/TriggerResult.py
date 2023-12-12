from enum import Enum


class TriggerResult(Enum):
    Failure = 0
    Missing = 1
    Success = 2