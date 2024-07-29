from app import args
from app.other import check_search_by_id
from app.parsers import entries
from app.functions import entries

if args.today:
    search = args.today[0]
    search_by_id = check_search_by_id(args.id_search)
    entries.today(search, search_by_id)

elif args.today_status:
    entries.today_status()

elif args.finish:
    searches = args.finish
    search_by_id = check_search_by_id(args.id_search)
    entries.finish(searches, search_by_id)

elif args.unfinish:
    searches = args.unfinish
    search_by_id = check_search_by_id(args.id_search)

    entries.unfinish(searches, search_by_id)
