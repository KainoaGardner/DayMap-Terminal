from app import args
from app.other import check_search_by_id
from app.parsers import heatmaps
from app.functions import heatmaps

if args.heatmaps:
    search = args.heatmaps[0]
    search_by_id = check_search_by_id(args.id_search)

    heatmaps.heatmaps_title(search, search_by_id)
elif args.heatmaps_all:
    heatmaps.heatmaps_all()

elif args.streak_heatmap:
    search = args.streak_heatmap[0]
    search_by_id = check_search_by_id(args.id_search)
    heatmaps.heatmap_streak(search, search_by_id)

elif args.create_heatmap:
    title, description = args.create_heatmap
    heatmaps.create_heatmap(title, description)

elif args.remove_heatmap:
    search = args.remove_heatmap[0]
    search_by_id = check_search_by_id(args.id_search)
    heatmaps.remove_heatmap(search, search_by_id)

elif args.update_heatmap:
    search, new_title, new_description = args.update_heatmap
    search_by_id = check_search_by_id(args.id_search)
    heatmaps.change_heatmap(search, search_by_id, new_title, new_description)
