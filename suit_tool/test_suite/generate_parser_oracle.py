import json

import cbor

from suit_tool.manifest import SUITWrapper


class parser_opts:
    def __init__(self, manifest_num):
        manifest_name = '../../examples/manifest_compile_oracle/oracle' + str(manifest_num) + '.cbor'
        self.json = True
        self.manifest = open(manifest_name, 'rb')


def main():
    for num in range(8):
        manifest_oracle = parser_opts(num)
        decoded_cbor_wrapper = cbor.loads(manifest_oracle.manifest.read())
        wrapper = SUITWrapper().from_suit(decoded_cbor_wrapper)
        json_output = json.dumps(wrapper.to_json(), indent=None)
        with open("../../examples/manifest_parser_oracle/oracle" + str(num) + ".json", "w") as outfile:
            outfile.write(json_output)
    return 0


if __name__ == '__main__':
    main()
