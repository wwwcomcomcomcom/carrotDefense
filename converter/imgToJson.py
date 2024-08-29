import json
from psd_tools import PSDImage
import numpy as np


def load_config(config_path):
    with open(config_path, "r") as config_file:
        return json.load(config_file)


def psd_to_map(image_path, config_path, output_path):
    # Load configuration
    config = load_config(config_path)

    # Create a reverse mapping for easier lookup
    reverse_config = {tuple(v): int(k) for k, v in config.items()}

    # Open the PSD file
    psd = PSDImage.open(image_path)
    width, height = psd.size

    # Initialize the output data structure
    output_data = {"width": width, "height": height, "layers": []}

    # Process each layer
    for layer in psd:
        if layer.is_group():
            continue  # Skip group layers

        layer_image = layer.composite()
        layer_array = np.array(layer_image)

        # Process the layer
        map_data = []
        for y in range(height):
            for x in range(width):
                pixel = tuple(layer_array[y, x][:3])  # Get RGB values
                map_value = reverse_config.get(
                    pixel, 0
                )  # Default to 0 if color not in config
                map_data.append(map_value)

        output_data["layers"].append(map_data)

    # Save the output data
    with open(output_path, "w") as output_file:
        json.dump(output_data, output_file, indent=2)


if __name__ == "__main__":
    # These paths can be adjusted as needed
    image_path = "converter/map.psd"
    config_path = "converter/config.json"
    output_path = "converter/output_map.json"

    psd_to_map(image_path, config_path, output_path)
    print(f"Map data has been saved to {output_path}")
