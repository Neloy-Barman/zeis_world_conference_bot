import json

from intent_handlers.welcome_hlr import handle_welcome
from intent_handlers.fallback_hlr import handle_fallback
from intent_handlers.main_menu_hlr import handle_main_menu
from intent_handlers.sponsor_info_hlr import handle_sponsor
from intent_handlers.contact_info_hlr import handle_contact
from intent_handlers.speaker_info_hlr import handle_speaker
from intent_handlers.event_info_hlr import handle_event_info
from intent_handlers.founder_info_hlr import handle_founder_info
from intent_handlers.about_us_info_hlr import handle_about_us_info
from intent_handlers.lead_collection_hlr import handle_lead_collection
from intent_handlers.conference_info_hlr import handle_conference_info
from intent_handlers.guest_of_honour_info_hlr import handle_guest_of_honour
from intent_handlers.location_timing_info_hlr import handle_location_timing





def lambda_handler(event, context):

    # Current Intent Name
    intent_name = event['currentIntent']['name']
    print(f"Triggered Intent Name: {intent_name}")

    intent_to_handlers = {
        "Guest_Of_Honour_Info_ZIES" : handle_guest_of_honour,
        "Sponsor_Partner_Info_ZIES": handle_sponsor,
        "Location_Timings_ZIES": handle_location_timing,
        "Contact_Info_ZIES": handle_contact,
        "Conference_Info_ZIES": handle_conference_info,
        "About_Us_ZIES": handle_about_us_info,
        "Lead_Generation_ZIES": handle_lead_collection,
        "Founder_Info_ZIES": handle_founder_info,
        "Speaker_Info_ZIES": handle_speaker,
        "Fallback_ZIES": handle_fallback,
        "Main_Menu_ZIES": handle_main_menu,
        "Welcome_ZIES": handle_welcome,
        "Event_Info_ZIES": handle_event_info
    }

    return intent_to_handlers[intent_name](event)