from app import parser

heatmaps = parser.add_argument_group("Heatmaps")

heatmaps.add_argument(
    "-hm",
    "--heatmaps",
    nargs=1,
    metavar=("title"),
    help="Show heatmaps by title",
)

heatmaps.add_argument(
    "-hma",
    "--heatmaps_all",
    action="store_true",
    help="Show all heatmaps",
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
    metavar=("title"),
    help="remove a heatmap",
)

heatmaps.add_argument(
    "-uhm",
    "--update_heatmap",
    nargs=3,
    metavar=("title,new_title,description"),
    help="remove a heatmap",
)
