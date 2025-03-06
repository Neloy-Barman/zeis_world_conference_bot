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


def create_unordered_list_elems(input_string):

    # Split the string into individual items
    items = [item.strip() for item in input_string.split(",")]

    # Generate the unordered list in HTML format
    html_output = "<ul>"
    for item in items:
        html_output += f"<li>{item}</li>"
    html_output += "</ul>"

    # Print the result
    print(f"HTML output: {html_output}")
    return html_output

def create_buttons(options): 
    return [{'text': f'{item}', 'value': f'{item}'} for item in options]
