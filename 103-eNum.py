from enum import Enum

class UserRole(Enum):
    ADMIN = 1
    EDITOR = 2
    VIEWER = 3

role = UserRole.ADMIN
print(role)  # UserRole.ADMIN
print(role.value)  # 1
