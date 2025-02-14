class TerminalColor:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


WEEKDAYS = {0: "Mon", 1: "Tue", 2: "Wen", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


def bold_print(text):
    print(TerminalColor.BOLD + text + TerminalColor.END)


def bold_input(text):
    answer = input(TerminalColor.BOLD + text + TerminalColor.END)
    return answer


def check_search_by_id(id_search):
    if id_search:
        return "true"
    return "false"
