import json


def json_file_print(url):
    with open(url, 'r') as f:
        data = json.load(f)
    print(data)


def main():
    json_file_print("relation.json")


if __name__ == "__main__":
    main()
