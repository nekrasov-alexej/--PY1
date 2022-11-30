import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=',', new_line='\n') -> list[dict]:
    # TODO реализовать конвертер из csv в json
    with open(filename) as f:
        conv_file = []
        for index, line in enumerate(f):
            str_i = line.strip(new_line).split(delimeter)
            if index == 0:
                heads = str_i
                continue
            conv_file.append({})
            for i, _ in enumerate(heads):
                conv_file[-1][heads[i]] = str_i[i]
    return conv_file


json_file = csv_to_list_dict(INPUT_FILE)

print(json.dumps(json_file, indent=4))
