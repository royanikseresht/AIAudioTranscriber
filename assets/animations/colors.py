import json

def replace_purple_with_green(file_path):
    # Define the RGB values for the green shade you want to replace purple with.
    green_rgb = [115 / 255.0, 156 / 255.0, 146 / 255.0]  # Normalize #739c92 to [0,1]

    # Function to check if the color is purple (this will check if RGB is close to purple)
    def is_purple(color):
        if isinstance(color, list) and len(color) == 3:  # Ensure it's an RGB triplet
            r, g, b = color
            # Consider the color purple if it has strong red and blue, but low green
            return r > 0.4 and g < 0.3 and b > 0.4
        return False

    def replace_color(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "c" and isinstance(value, dict) and "k" in value and isinstance(value["k"], list):
                    # We have a "color" key that we need to check
                    if isinstance(value["k"][0], list):
                        color = value["k"][0]
                        if is_purple(color):
                            # If it's purple, replace it with the desired green color
                            value["k"][0] = green_rgb
                else:
                    replace_color(value)  # Recursively process nested dictionaries
        elif isinstance(obj, list):
            for item in obj:
                replace_color(item)  # Recursively process items in a list

    # Read the JSON data from the file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Replace purple colors with green
    replace_color(data)

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Specify the path to your JSON file
file_path = '/Users/roya/Downloads/AIAudioTranscriber-master/assets/animations/contact.json'
replace_purple_with_green(file_path)