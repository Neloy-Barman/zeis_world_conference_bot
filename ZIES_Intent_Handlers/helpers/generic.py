def get_slot_category(slot_lists, slot):
    return { name: category for names, category in slot_lists for name in names}.get(slot, None)

