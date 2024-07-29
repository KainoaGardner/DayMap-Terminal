from app import args
from app.parsers import users
from app.functions import users


if args.login:
    username, password = args.login
    users.login(username, password)

elif args.logout:
    users.logout()

elif args.user:
    users.user()

elif args.register:
    username, password = args.register
    users.register(username, password)

elif args.remove_user:
    users.remove_user()
