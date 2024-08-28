import json
from PIL import Image


def load_config(config_path):
    with open(config_path, "r") as config_file:
        return json.load(config_file)


def load_map_data(map_path):
    with open(map_path, "r") as map_file:
        return json.load(map_file)


def map_to_image(map_path, config_path, output_path):
    # Load configuration
    config = load_config(config_path)

    # Load map data
    map_data = load_map_data(map_path)

    width = map_data["width"]
    height = map_data["height"]
    tile_data = map_data["layers"][0]  # Assuming we're using the first layer

    # Create a new image
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    # Fill the image with appropriate colors
    for y in range(height):
        for x in range(width):
            index = y * width + x
            tile_value = str(tile_data[index])  # Convert to string to match config keys
            color = tuple(
                config.get(tile_value, (0, 0, 0))
            )  # Default to black if not in config
            pixels[x, y] = color

    # Save the image
    img.save(output_path)


if __name__ == "__main__":
    # These paths can be adjusted as needed
    map_path = "save/town.json"
    config_path = "converter/config.json"
    output_path = "converter/output_image.png"

    map_to_image(map_path, config_path, output_path)
    print(f"Image has been saved to {output_path}")
