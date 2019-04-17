"""loads reads and write to config file for python project"""

import configparser

def read_configuration(file_name,*args):
    """function to read config file and return a value for a key value pair
    returns -1 if file not found or read error """
    config=configparser.ConfigParser()

    try:
        with open(file_name) as f:
            config.read_file(f)
    except Exception:
        return -1

    config.read('config.ini')
    return config[args[0]][args[1]]

def main():
    value=read_configuration('config.ini','DEFAULT','CompressionLevel')
    print(value)


if __name__ == "__main__":
    main()


