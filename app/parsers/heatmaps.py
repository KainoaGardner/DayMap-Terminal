from app import parser

heatmaps = parser.add_argument_group("Heatmaps")

heatmaps.add_argument(
    "-hm",
    "--heatmaps",
    nargs="?",
    const="a",
    metavar=("all,a"),
    help="Show heatmaps",
    # type=str,
)
