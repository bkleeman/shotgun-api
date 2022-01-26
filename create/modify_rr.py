try:
    import simplejson as json
except ImportError:
    import json


with open('./data/grid-dc.json', 'r') as f:
    file_data = json.loads(f.read())

with open('./data/new_data/grid-dc.json', 'w') as f:
    for feature in file_data["features"]:
        feature["properties"] = { "original" : feature["properties"]}
        feature["properties"]["required"] = {
            "unit": "kV",
            # visual dimension
            "viz_dim": "class",
            "legend": "500-1000 kV DC",
            "years": []
        }

        feature["properties"]["optional"] = {
            "description": "",
        }

        feature["properties"]["type"] = {
            "primary": "electric_grid",
            "secondary": "dc"
        }

    json.dump(file_data, f)