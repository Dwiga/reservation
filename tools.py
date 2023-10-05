import sys
from seeds import user_seeding
from seeds import tables_seeding

action = sys.argv[1]
args = sys.argv[2]

if action == "seed":
    if args == "users":
        user_seeding.user_seeding()
    elif args == "tables":
        tables_seeding.table_seeding()
    else:
        print("Invalid argument")
else:
    print("Invalid action")
