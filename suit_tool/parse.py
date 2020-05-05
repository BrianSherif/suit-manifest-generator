#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright 2019 ARM Limited or its affiliates
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
import itertools
import json
import textwrap

import cbor

from suit_tool.manifest import SUITWrapper


def main(options):
    # Read the manifest wrapper
    decoded_cbor_wrapper = cbor.loads(options.manifest.read())
    # print(decoded_cbor_wrapper)
    wrapper = SUITWrapper().from_suit(decoded_cbor_wrapper)
    if options.json:
        return json.dumps(wrapper.to_json(), indent=None)
    else:
        return ('\n'.join(itertools.chain.from_iterable(
            [textwrap.wrap(t, 70) for t in wrapper.to_debug('').split('\n')]
        )))
