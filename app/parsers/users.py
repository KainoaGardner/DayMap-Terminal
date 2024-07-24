from app import parser

users = parser.add_argument_group("Users")

users.add_argument(
    "-li",
    "--login",
    nargs=2,
    metavar=("username", "password"),
    help="Login to your account",
)

users.add_argument(
    "-lo",
    "--logout",
    action="store_true",
    help="Logout of your account",
)

users.add_argument(
    "-u",
    "--user",
    action="store_true",
    help="Show user if logged in",
)

users.add_argument(
    "-r",
    "--register",
    nargs=2,
    metavar=("username", "password"),
    help="Register a user",
)

users.add_argument(
    "-rmu",
    "--remove_user",
    action="store_true",
    help="Remove a user",
)
