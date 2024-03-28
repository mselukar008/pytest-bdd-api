import os


def get_abs_dir(relativePath):
    project_root_dir = get_project_root_dir()
    absolute_path = project_root_dir + relativePath
    return absolute_path


def get_project_root_dir():
    ROOT_DIR = os.getcwd()
    return ROOT_DIR


def extract_single_value(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return str(results[0])


def extract_values(obj, key):

    def extract(obj, key):
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for k, v in obj.items():
                yield from extract(v, key)
        elif isinstance(obj, list):
            for i in obj:
                yield from extract(i, key)

    results = list(extract(obj,key))
    return results