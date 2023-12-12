from enum import Enum


class OrganizationTrigger(Enum):
    OnAdd = 0
    OnRemove = 1
    OnUpgrade = 2