ADMIN = 1
EDITOR = 2
VIEWER = 3

role=2
if role in [ADMIN, EDITOR]:
    print("User can edit content")
