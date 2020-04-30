import json
import os
import sys

import cbor
import pytest

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
    with open('../examples/testcases/testcase' + str(example) + '.cbor', 'rb') as fp:
        data = cbor.load(fp)
        return data


@pytest.mark.parametrize('input_json, expected_output',
                         [
                             (example_loader(0), manifest_loader(0)),
                             (example_loader(1), manifest_loader(1)),
                             (example_loader(2), manifest_loader(2)),
                             (example_loader(3), manifest_loader(3)),
                             (example_loader(4), manifest_loader(4)),
                             (example_loader(5), manifest_loader(5)),
                             (example_loader(6), manifest_loader(6)),
                             (example_loader(7), manifest_loader(7))
                         ]
                         )
def test_compile_manifest(input_json, expected_output):
    nm = compile_manifest(Emptyopts(), input_json)
    with open('../examples/testcases/answer.cbor', 'wb') as fd:
        fd.write(cbor.dumps(nm.to_suit(), sort_keys=True))
        fd.close()
    with open('../examples/testcases/answer.cbor', 'rb') as fp:
        data = cbor.load(fp)
    assert data == expected_output
