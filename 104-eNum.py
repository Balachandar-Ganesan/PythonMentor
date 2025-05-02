from enum import Enum, auto
class UserRole(Enum):
    ADMIN = 1
    EDITOR = 2
    VIEWER = 3

    def can_edit(self):
        return self in {UserRole.ADMIN, UserRole.EDITOR}

    def can_delete(self):
        return self == UserRole.ADMIN
#if role in [UserRole.ADMIN, UserRole.EDITOR]:
#    print("User can edit content")
role=UserRole.ADMIN
if role.can_edit():
    print("User can edit content")