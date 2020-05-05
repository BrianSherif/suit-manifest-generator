#!/usr/bin/python3
import json
import os
import sys

suittoolPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
sys.path.insert(0, suittoolPath)


def open_json(example):
    with open('../../examples/example' + str(example) + '.json', 'rb') as fp:
        data = json.load(fp)
        return data


class Emptyopts:
    def __init__(self):
        self.components = []


def main():
    for num in range(8):
        os.system(
            "suit-tool create -i ../../examples/example" + str(
                num) + ".json -o ../../examples/manifest_compile_oracle/oracle" + str(
                num) + ".cbor")
    return 0


if __name__ == '__main__':
    main()
