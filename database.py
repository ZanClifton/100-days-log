entries = []


def add_entry(entry_activity, entry_thoughts, entry_date, entry_day):
    """Adds entry content and date, as an object, to the entries array"""
    entries.append({"activity": entry_activity,
                   "thoughts": entry_thoughts, "date": entry_date, "day": entry_day})


def get_entries():
    return entries
