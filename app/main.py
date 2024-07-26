from . import parser
import sys
from app.parsers import users, heatmaps, entries
from app.functions import users, heatmaps, entries

args = parser.parse_args()


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

if args.heatmaps:
    title = args.heatmaps[0]
    heatmaps.heatmaps_title(title)
elif args.heatmaps_all:
    heatmaps.heatmaps_all()
elif args.create_heatmap:
    title, description = args.create_heatmap
    heatmaps.create_heatmap(title, description)
elif args.remove_heatmap:
    title = args.remove_heatmap[0]
    heatmaps.remove_heatmap(title)
elif args.update_heatmap:
    title, new_title, description = args.update_heatmap
    heatmaps.change_heatmap(title, title, description)

if args.today:
    title = args.today[0]
    entries.today(title)
elif args.today_status:
    entries.today_status()
elif args.finish:
    titles = args.finish
    entries.finish(titles)
elif args.unfinish:
    titles = args.unfinish
    entries.unfinish(titles)
