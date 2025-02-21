import re 

def get_slot_category(slot_lists, slot):
    return { name: category for names, category in slot_lists for name in names}.get(slot, None)


def validate_slot(slot_name, slot_value):
    if slot_name == "name":
        # Validate name contains only letters and spaces
        return re.match(r"^[A-Za-z\s]+$", slot_value)
    elif slot_name == "company":
        # Validate company name isn't empty and has letters
        return re.match(r"^[A-Za-z\s]+$", slot_value)
    elif slot_name == "contact_number":
        # Validate phone number (10 digits)
        return re.match(r"^\d{10}$", slot_value)
    return False  # Default: Invalid if no match