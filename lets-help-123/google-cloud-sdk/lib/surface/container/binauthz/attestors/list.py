# -*- coding: utf-8 -*- #
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""List attestors command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.container.binauthz import apis
from googlecloudsdk.api_lib.container.binauthz import attestors
from googlecloudsdk.api_lib.container.binauthz import util
from googlecloudsdk.calliope import base


class List(base.ListCommand):
  """List Attestors associated with the current project."""

  @classmethod
  def Args(cls, parser):
    parser.display_info.AddFormat("""
        table[box](
            name.scope().segment(3):sort=1,
            userOwnedDrydockNote.noteReference:label=NOTE,
            userOwnedDrydockNote.publicKeys.len():label=NUM_PUBLIC_KEYS
        )
    """)

  def Run(self, args):
    api_version = apis.GetApiVersion(self.ReleaseTrack())
    return attestors.Client(api_version).List(util.GetProjectRef())
