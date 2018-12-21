# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Abstraction layer for third party dependencies."""
from cauliflowervest.server import services


inventory_service = None
account_service = None


def GetInventoryService():
  global inventory_service
  if inventory_service:
    return inventory_service
  inventory_service = services.InventoryService()
  return inventory_service


def GetAccountsService():
  global account_service
  if account_service:
    return account_service
  account_service = services.AccountsService()
  return account_service
