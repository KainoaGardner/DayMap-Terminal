from . import parser

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
    heatmaps.heatmaps(args.heatmaps)
elif args.create_heatmap:
    title, description = args.create_heatmap
    heatmaps.create_heatmap(title, description)
elif args.remove_heatmap:
    id = int(args.remove_heatmap[0])
    heatmaps.remove_heatmap(id)
elif args.update_heatmap:
    id, title, description = args.update_heatmap
    heatmaps.change_heatmap(int(id), title, description)

if args.today:
    id = int(args.today[0])
    entries.today(id)
elif args.today_status:
    entries.today_status()
elif args.finish:
    ids = args.finish
    entries.finish(ids)
elif args.unfinish:
    ids = args.finish
    entries.unfinish(ids)
