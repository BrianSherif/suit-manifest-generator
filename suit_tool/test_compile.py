import json
import os
import sys

import cbor
import pytest

from suit_tool.generate_test_case import test_generator

suittoolPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
sys.path.insert(0, suittoolPath)
from suit_tool.compile import compile_manifest



class Emptyopts:
    def __init__(self):
        self.components = []


def example_loader(example):
    with open('../examples/example' + str(example) + '.json') as json_file:
        data = json.load(json_file)
        return data


def manifest_loader(example):
    test_generator(example)
    with open('../examples/testcases/testcase' + str(example) + '.cbor', 'rb') as fp:
        data = cbor.load(fp)
        return data


@pytest.mark.parametrize('input_json, expected_output, test_num', [
    (example_loader(0), manifest_loader(0), 0),
    (example_loader(1), manifest_loader(1), 1),
    (example_loader(2), manifest_loader(2), 2),
    (example_loader(3), manifest_loader(3), 3),
    (example_loader(4), manifest_loader(4), 4),
    (example_loader(5), manifest_loader(5), 5),
    (example_loader(6), manifest_loader(6), 6),
    (example_loader(7), manifest_loader(7), 7)
])
def test_compile_manifest(input_json, expected_output, test_num):
    nm = compile_manifest(Emptyopts(), input_json)
    with open('../examples/testcases/answer.cbor', 'wb') as fd:
        cbor.dump(nm.to_suit(), fd)
    with open('../examples/testcases/answer.cbor', 'rb') as fp:
        data = cbor.load(fp)
    # print(data)
    assert data == expected_output
    os.remove('../examples/testcases/answer.cbor')
    os.remove('../examples/testcases/testcase' + str(test_num) + '.cbor')
