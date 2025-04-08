#!/usr/bin/python3
from os.path import exists

"""
def generate_invitations(template_content, attendees):
function that generates personalized invitation files
from a template with placeholders and a list of objects.
"""


def generate_invitations(template_content, attendees):

    if not isinstance(template_content, str) or not isinstance(attendees, list):
        print("Invalid input type")
        return

    if not template_content.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated")
        return

    def data(guest_d):
        required_keys = ["name", "event_title", "event_date", "event_location"]
        missing_keys = [key for key in required_keys if key not in guest_d]

        if missing_keys:
            print(f"Warning: Missing keys in guest data: {missing_keys}")
            return None

        updated_data = {}
        for key in required_keys:
            value = guest_d.get(key)
            updated_data[key] = value if value else "N/A"

        return updated_data

    def write_to_temp():
        for i, guest in enumerate(attendees):
            parsed_d = data(guest)

            try:
                updated_content = template_content.format(**parsed_d)
                if not exists(f"output_{i+1}.txt"):
                    with open(f"output_{i+1}.txt", "w") as file:
                        file.write(updated_content)
                else:
                    print(f"Error: file  output_{i+1}.txt already exists")
            except Exception as e:
                print(f"Error writing output_{i+1}.txt: {e}")

    write_to_temp()
