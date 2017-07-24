import json
import locale
from os import path
from os import listdir
from os.path import isfile, join


def main():
    directory_path = '.\\concrete'
    geom_file_names = [join(directory_path, f) for f in listdir(directory_path) if isfile(join(directory_path, f)) and f.endswith('.json')]

    geometries = load_geometries(geom_file_names)
    income_stats = load_stats('income_stats.txt')
    result = zip(geometries, income_stats)
    json_str = json.dumps(result)
    print json_str


def zip(geometries, income_stats):
    for geometry in geometries:
        for stat in income_stats:
            if geometry['id'] == stat['id']:
                geometry['properties']['place'] = stat['place']
                geometry['properties']['income'] = stat['income']
                break

    return geometries

def load_geometries(files):
    geometries = list()
    for filename in files:
        with open(filename, 'r') as data_file:
            data = data_file.read()
        data = data.replace('\n', '').replace('\r', '').replace('\t', '')
        try:
            region = json.loads(data)
            geometries.append(region)
        except:
            print 'Region from file \'{}\' is failed to load.'.format(filename)

    return geometries


def load_stats(filename):
    stats = list()
    with open(filename) as file_handler:
        lines = file_handler.readlines()

    index = 1
    for line in lines:
        line = line.replace('\n', '')
        parts = line.split(' ')
        stats.append({
            "id": str(index).zfill(2),
            "place": parts[-1],
            "income": parts[-2]
        })
        index += 1
    return stats

if __name__ == "__main__":
    main()