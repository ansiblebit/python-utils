# -*- coding: utf-8 -*-
#
# Copyright 2018 ansiblebit
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
#

import steenzout.object


class Download (steenzout.object.Object):
    """Represents a download target.

    Attributes:
        title (str): name of the target.
        size (str): size of the target (units included).
        filepath (str): URL where the target can be downloaded.
        md5 (str): MD5 checksum of the target.
        sha256 (str): SHA256 checksum of the target.
    """

    def __init__(self, title=None, size=None, filepath=None, md5=None, sha256=None):
        self.title = title
        self.size = size
        self.filepath = filepath
        self.md5 = md5
        self.sha256 = sha256
