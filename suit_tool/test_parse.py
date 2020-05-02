import json
import os

import pytest

from suit_tool.parse import main as parser


class parser_opts:
    def __init__(self, manifest_num):
        manifest_name = '../examples/testcases/testcase' + str(manifest_num) + '.cbor'
        self.json = True
        self.manifest = open(manifest_name, 'rb')


def json_generator(num):
    input_json = '../examples/example' + str(num) + '.json'
    output = 'output' + str(num) + '.json'
    os.system('suit-tool create -i ' + input_json + ' -o ' + output + ' -f json')
    with open(output) as json_file:
        data = json.load(json_file)
        return json.dumps(data)


def output_cleaner(num):
    os.remove('output' + str(num) + '.json')


@pytest.mark.parametrize('expected_json, test_num',
                         [
                             (json_generator(0), 0),
                             (json_generator(1), 1),
                             (json_generator(2), 2),
                             (json_generator(3), 3),
                             (json_generator(4), 4),
                             (json_generator(5), 5),
                             (json_generator(6), 6),
                             (json_generator(7), 7)
                         ]
                         )
def test_main(expected_json, test_num):
    parser_out = parser(parser_opts(test_num))
    assert parser_out == expected_json
    output_cleaner(test_num)
