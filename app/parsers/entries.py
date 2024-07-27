from app import parser

entries = parser.add_argument_group("Entries")

entries.add_argument(
    "-t",
    "--today",
    nargs=1,
    metavar=("title"),
    help="Check heatmap finished today",
)

entries.add_argument(
    "-ts",
    "--today_status",
    action="store_true",
    help="Show finised status of todays status",
)

entries.add_argument(
    "-f",
    "--finish",
    nargs="+",
    metavar=("id"),
    help="Finish today",
)

entries.add_argument(
    "-uf",
    "--unfinish",
    nargs="+",
    metavar=("id"),
    help="Unfinish today",
)
