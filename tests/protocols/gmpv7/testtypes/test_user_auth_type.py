# -*- coding: utf-8 -*-
# Copyright (C) 2019-2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from gvm.errors import InvalidArgument
from gvm.protocols.gmpv7 import UserAuthType, get_user_auth_type_from_string


class GetUserAuthTypeFromStringTestCase(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaises(InvalidArgument):
            get_user_auth_type_from_string('foo')

    def test_none_or_empty(self):
        ct = get_user_auth_type_from_string(None)
        self.assertIsNone(ct)
        ct = get_user_auth_type_from_string('')
        self.assertIsNone(ct)

    def test_file(self):
        ct = get_user_auth_type_from_string('file')
        self.assertEqual(ct, UserAuthType.FILE)

    def test_radius_connect(self):
        ct = get_user_auth_type_from_string('radius_connect')
        self.assertEqual(ct, UserAuthType.RADIUS_CONNECT)

    def test_ldap_connect(self):
        ct = get_user_auth_type_from_string('ldap_connect')
        self.assertEqual(ct, UserAuthType.LDAP_CONNECT)


if __name__ == '__main__':
    unittest.main()
