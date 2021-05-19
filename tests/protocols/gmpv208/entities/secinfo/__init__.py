# -*- coding: utf-8 -*-
# Copyright (C) 2021 Greenbone Networks GmbH
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

from .test_get_cert_bund_advisory import GmpGetCertBundTestMixin
from .test_get_cert_bund_advisory_list import GmpGetCertBundListTestMixin
from .test_get_cpe import GmpGetCpeTestMixin
from .test_get_cpe_list import GmpGetCpeListTestMixin
from .test_get_cve import GmpGetCveTestMixin
from .test_get_cve_list import GmpGetCveListTestMixin
from .test_get_dfn_cert_advisory import GmpGetDfnCertTestMixin
from .test_get_dfn_cert_advisory_list import GmpGetDfnCertListTestMixin
from .test_get_info import GmpGetInfoTestMixin
from .test_get_info_list import GmpGetInfoListTestMixin
from .test_get_nvt import GmpGetNvtTestMixin
from .test_get_nvt_list import GmpGetNvtListTestMixin
from .test_get_nvt_families import GmpGetNvtFamiliesTestMixin
from .test_get_oval_definition import GmpGetOvalDefTestMixin
from .test_get_oval_definition_list import GmpGetOvalDefListTestMixin
from .test_get_scan_config_nvt import GmpGetScanConfigNvtTestMixin
from .test_get_scan_config_nvts import GmpGetScanConfigNvtsTestMixin