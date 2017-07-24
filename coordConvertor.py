import json
import locale
from os import path


def main():
    filename = "subregions.json"
    with open(filename, 'r') as data_file:
        data = data_file.read()

    src_regions = json.loads(data)

    index = 0
    features = list()
    for region in src_regions:
        index += 1
        coords = src_regions[region]
        feature = {
            "id": "{}".format(index),
            "type": "Feature",
            "properties": {
                "name": region,
                "density": index * 10
            }
        }

        wrap_coords = list()
        for coord in coords.values():
            dst_coord = list()
            for pair in coord:
                dst_pair = [pair[1], pair[0]]
                dst_coord.append(dst_pair)
            wrap_coords.append(dst_coord)

        wrap_coords = sorted(wrap_coords, key=lambda item: -len(item))
        if len(wrap_coords) > 1:
            geometry = {
                "type": "MultiPolygon",
                "coordinates": [wrap_coords]
            }
        else:
            geometry = {
                "type": "Polygon",
                "coordinates": [wrap_coords[0]]
            }

        feature["geometry"] = geometry
        features.append(feature)

    dst_regions = {
        "type": "FeatureCollection",
        "features": features
    }

    with open("subregions_dst.json", 'w') as dst_file:
        json.dump(dst_regions, dst_file)

    index = 0
    for feature in features:
        index += 1
        file_name = "./concrete/_{}.json".format(index)
        with open(file_name, 'w') as dst_file:
            json_str = json.dumps(feature)
            json_with_stripped_floats = remove_float_rests(json_str)
            dst_file.write(json_with_stripped_floats)


def remove_float_rests(text):
    beg_pos = 0
    MIN_LENGTH = 4
    while True:
        beg_pos = text.find('.', beg_pos+1)
        end_pos = find_next_not_digit(text, beg_pos)
        if beg_pos == -1 or end_pos == -1:
            return text
        length = end_pos - beg_pos
        if length > MIN_LENGTH:
            text = text[0:beg_pos + MIN_LENGTH] + text[end_pos:]


def find_next_not_digit(str, position):
    while True:
        position += 1
        if position >= len(str):
            return -1
        if not str[position].isdigit():
            return position

if __name__ == "__main__":
    main()