from enum import Enum, auto
class UserRole(Enum):
   ADMIN = ("Admin", "Has full access")
   EDITOR = ("Editor", "Can edit content")
   VIEWER = ("Viewer", "Can only view content")

   def __init__(self, display_name, description):
        self.display_name = display_name
        self.description = description

   def can_edit(self):
        return self in {UserRole.ADMIN, UserRole.EDITOR}

   def can_delete(self):
        return self == UserRole.ADMIN
#if role in [UserRole.ADMIN, UserRole.EDITOR]:
#    print("User can edit content")
role=UserRole.ADMIN
if role.can_edit():
    print("User can edit content")
    print(role.display_name)  # Admin
    print(role.description)  # Has full access