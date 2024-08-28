import json
import os
from PIL import Image


def load_config(config_path):
    with open(config_path, "r") as config_file:
        return json.load(config_file)


def load_existing_map(output_path):
    if os.path.exists(output_path):
        with open(output_path, "r") as existing_file:
            return json.load(existing_file)
    return None


def merge_map_data(existing_data, new_data):
    if existing_data is None:
        return new_data

    # Merge layers
    for i, new_layer in enumerate(new_data["layers"]):
        if i < len(existing_data["layers"]):
            existing_data["layers"][i] = new_layer
        else:
            existing_data["layers"].append(new_layer)

    # Update width and height if necessary
    existing_data["width"] = max(existing_data["width"], new_data["width"])
    existing_data["height"] = max(existing_data["height"], new_data["height"])

    return existing_data


def image_to_map(image_path, config_path, output_path):
    # Load configuration
    config = load_config(config_path)

    # Create a reverse mapping for easier lookup
    reverse_config = {tuple(v): int(k) for k, v in config.items()}

    # Open the image
    with Image.open(image_path) as img:
        width, height = img.size

        # Convert image to RGB mode if it's not already
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Process the image
        map_data = []
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                map_value = reverse_config.get(
                    pixel, 0
                )  # Default to 0 if color not in config
                map_data.append(map_value)

        # Prepare the new data
        new_data = {"width": width, "height": height, "layers": [map_data]}

        # Load existing data if it exists
        existing_data = load_existing_map(output_path)

        # Merge new data with existing data
        final_data = merge_map_data(existing_data, new_data)

        # Save the merged data
        with open(output_path, "w") as output_file:
            json.dump(final_data, output_file)


if __name__ == "__main__":
    # These paths can be adjusted as needed
    image_path = "converter/output_image.png"
    config_path = "converter/config.json"
    output_path = "output_map.json"

    image_to_map(image_path, config_path, output_path)
    print(f"Map data has been merged and saved to {output_path}")
