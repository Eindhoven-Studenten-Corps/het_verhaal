import json



def convert_old_format_to_new(old_format):
    start_date_list = old_format["startDate"].split(",")
    start_date = {
        "year": start_date_list[0],
        "month": start_date_list[1].replace("0", ""),
        "day": start_date_list[2].replace("0", "")
    }
    try:
        new_format = {
            "media": {
                "url": None,
                "caption": old_format["asset"]["caption"],
                "credit": old_format["asset"]["credit"]
            },
            "start_date": start_date,
            "text": {
                "headline": old_format["headline"],
                "text": old_format["text"]
            }
        }
    except KeyError:
        new_format = {
            "start_date": start_date,
            "text": {
                "headline": old_format["headline"],
                "text": old_format["text"]
            }
        }

    return new_format

# Read the old JSON file
with open("data_old.json", "r") as f:
    old_json_list = json.load(f)

old_json_list = old_json_list["timeline"]["date"]
# Assuming the old JSON format list is stored in a variable called 'old_json_list'
new_json_list = [convert_old_format_to_new(item) for item in old_json_list]

# Print the converted JSON list
print(json.dumps(new_json_list, indent=2))