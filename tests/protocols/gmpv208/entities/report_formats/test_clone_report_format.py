# -*- coding: utf-8 -*-
# Copyright (C) 2018-2021 Greenbone Networks GmbH
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

from gvm.errors import RequiredArgument
from gvm.protocols.gmpv208.entities.report_formats import (
    ReportFormatType,
    get_report_format_id_from_string,
)


class GmpCloneReportFormatTestMixin:
    def test_clone(self):
        self.gmp.clone_report_format('a1')

        self.connection.send.has_been_called_with(
            '<create_report_format>' '<copy>a1</copy>' '</create_report_format>'
        )

    def test_missing_id(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.clone_report_format('')

        with self.assertRaises(RequiredArgument):
            self.gmp.clone_report_format(None)

    def test_clone_with_type(self):
        self.gmp.clone_report_format(ReportFormatType.SVG)

        report_format_id = get_report_format_id_from_string('svg').value

        self.connection.send.has_been_called_with(
            '<create_report_format>'
            f'<copy>{report_format_id}</copy>'
            '</create_report_format>'
        )
