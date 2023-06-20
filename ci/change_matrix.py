import json
import sys

json_file_path = sys.argv[1:2][0]
changed_files = sys.argv[2:]

with open(json_file_path, "r") as read_file:
    data_list = json.load(read_file)

    for data in data_list:
        expected_path = data["path"] if data["path"].endswith("/") else data["path"]+"/"

        for changed_file in changed_files:
            if changed_file.startswith(expected_path):
                data["changed"] = True
                break

        if not "changed" in data:
            data["changed"] = False

    print(json.dumps(data_list))