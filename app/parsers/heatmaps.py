from app import parser

heatmaps = parser.add_argument_group("Heatmaps")

heatmaps.add_argument(
    "-hm",
    "--heatmaps",
    nargs="?",
    const="a",
    metavar=("all,a"),
    help="Show heatmaps",
)

heatmaps.add_argument(
    "-chm",
    "--create_heatmap",
    nargs=2,
    metavar=("title", "description"),
    help="create a heatmap",
)

heatmaps.add_argument(
    "-rhm",
    "--remove_heatmap",
    nargs=1,
    metavar=("id"),
    help="remove a heatmap",
)

heatmaps.add_argument(
    "-uhm",
    "--update_heatmap",
    nargs=3,
    metavar=("id,title,description"),
    help="remove a heatmap",
)
