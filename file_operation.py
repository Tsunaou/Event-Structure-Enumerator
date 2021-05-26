from utils import load_json, save_obj2json
import os

if __name__ == '__main__':
    n = 8
    filename = "strictPo0-{}.json".format(n)
    pos = load_json(filename)

    output_template = "POFile/strictPartialOrder{}.json"
    for i in range(n):
        key = str(i)
        file = output_template.format(i)
        if os.path.exists(file):
            print("{} exists".format(file))
            continue
        else:
            save_obj2json(pos[key], file)

    output_template = "POFileDict/strictPartialOrder{}.json"
    for i in range(n):
        key = str(i)
        file = output_template.format(i)
        if os.path.exists(file):
            print("{} exists".format(file))
            continue
        else:
            po_dict = dict()
            for idx, obj in enumerate(pos[key]):
                po_dict[idx] = obj
            save_obj2json(po_dict, file)
