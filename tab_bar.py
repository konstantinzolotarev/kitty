import os

def draw_title(data):
    tab = data.get("tab")
    active_wd = getattr(tab, "active_wd", "")

    last_dir = os.path.basename(active_wd) if active_wd else "~"

    return f"{last_dir}"
