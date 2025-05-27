import re
import json
import requests
from data.constants import guided_buttons
from helpers.generic import create_buttons
from helpers.lex_response import nextIntent, nextIntentWithResponseCard


# Function to convert URLs in text to clickable links with 'click here' text
def make_links_clickable(text):
    url_pattern = r"(https?://[^\s]+)"
    
    def replace_link(match):
        url = match.group(0)
        if "maps/embed" in url:
            return f' ~ <iframe src="{url}" width="225" height="200" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
        else:
            return f'<a href="{url}" target="_blank" style="color: #156087;">click here</a>'
    
    return re.sub(url_pattern, replace_link, text)


# Function to split text into segments of max 320 characters ending at the last period
def split_text_with_limit(text, limit=320):
    segments = []
    url_pattern = (
        r"https?://\S+"  # Pattern to match URLs starting with http:// or https://
    )

    while len(text) > limit:
        # Search for any URL in the current segment
        match = re.search(url_pattern, text)
        if match:
            # If URL found, ensure we don't split the URL by extending the limit to the end of the URL
            url_start = match.start()
            url_end = match.end()
            # If URL starts before the limit, include the full URL in this segment
            if url_start < limit:
                cut_index = url_end
            else:
                # Otherwise, cut at the last period within the limit
                cut_index = text[:limit].rfind(".")
                if cut_index == -1:
                    cut_index = limit  # fallback if no period is found
        else:
            # No URL, just cut at the last period within the limit
            cut_index = text[:limit].rfind(".")
            if cut_index == -1:
                cut_index = limit  # fallback if no period is found

        # Append the current segment and remove it from text
        segments.append(text[: cut_index + 1].strip())
        text = text[cut_index + 1 :].strip()

    # Add any remaining text as the last segment
    segments.append(text)
    return " ~ ".join(segments)




def handle_fallback(event):
    
    # Intent Name
    intent_name = event["sessionState"]["intent"]["name"]

    # Session Attributes
    session_attributes = event["sessionState"]["sessionAttributes"] if event["sessionState"]["sessionAttributes"] is not None else {}


    print("Fallback Handler Triggered......")
    url = "http://100.24.63.222/api"
    
    user_input = event['inputTranscript']
    print("User Input", user_input)

    params = {
        "text1": user_input,
        # Provide the API key here.....
        "key": "NWVkY2ZiYzktNDkxNC00Mzg0LTllZmMtZmNjZmZiZGRiMDZkIGh0dHBzOi8vd3d3LmdyYXZpdGFzLmFpLyAxMQ==",
    }
    payload = {}
    headers = {"Content-Type": "application/json"}

    response = requests.request(
        "GET", url, data=payload, headers=headers, params=params
    )

    if response.status_code == 200:
        try:
            temp = response.json()
            print(temp)

            if float(temp["score"]) > 0.4:
                answer = temp["answer"]

                if len(answer) > 320:
                    answer = split_text_with_limit(answer, 320)

                answer = make_links_clickable(answer)
                
                return nextIntentWithResponseCard(
                    intent_name,
                    session_attributes,
                    answer,
                    None,
                    None,
                    create_buttons(guided_buttons)
                )
                
            else:
                answer = "Apologies, not sure if I understand. Did you mean to ask any of the following questions?"
                print("Returning from fallback intent........")
                
                options =  [
                        {
                            "text": temp["question1"].capitalize(),
                            "value": temp["question1"],
                        },
                        {
                            "text": temp["question2"].capitalize(),
                            "value": temp["question2"],
                        },
                        {
                            "text": temp["question3"].capitalize(),
                            "value": temp["question3"],
                        },
                        {
                            "text": "Main Menu", 
                            "value": "main menu"
                        }
                    ]
                
                return nextIntentWithResponseCard(
                    intent_name,
                    session_attributes,
                    "Here are some suggestions",
                    None,
                    None,
                    options
                )
                
        except json.JSONDecodeError as e:
            print("Failed to decode JSON response:", e)
            return nextIntentWithResponseCard(
                intent_name,
                session_attributes,
                "Here are some suggestions",
                None,
                None,
                create_buttons(guided_buttons)
            )
            
    else:
        print("Request failed with status code:", response.status_code)
        msg = "Sorry, currently we are facing some technical issue. Please try after sometime."
        return nextIntent(
            session_attributes,
            intent_name,
            msg
        )

