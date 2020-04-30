#!/usr/bin/python3
import json
import os
import sys

import cbor

suittoolPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
sys.path.insert(0, suittoolPath)
from suit_tool.compile import compile_manifest


def open_json(example):
    with open('../examples/example' + str(example) + '.json', 'rb') as fp:
        data = json.load(fp)
        return data


class Emptyopts:
    def __init__(self):
        self.components = []


def generator():
    for num in range(8):
        nm = compile_manifest(Emptyopts(), open_json(num))
        with open('../examples/testcases/testcase' + str(num) + '.cbor', 'wb') as fd:
            fd.write(cbor.dumps(nm.to_suit(), sort_keys=True))


if __name__ == "__main__":
    sys.exit(generator())
