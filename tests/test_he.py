# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from numinwords import numinwords


class numinwordsHETest(TestCase):
    maxDiff = None

    def test_0(self):
        self.assertEqual(numinwords(0, lang="he"), u'אפס')

    def test_1_to_10(self):
        self.assertEqual(numinwords(1, lang="he"), u'אחת')
        self.assertEqual(numinwords(2, lang="he"), u'שתים')
        self.assertEqual(numinwords(7, lang="he"), u'שבע')
        self.assertEqual(numinwords(10, lang="he"), u'עשר')

    def test_11_to_19(self):
        self.assertEqual(numinwords(11, lang="he"), u'אחת עשרה')
        self.assertEqual(numinwords(13, lang="he"), u'שלש עשרה')
        self.assertEqual(numinwords(15, lang="he"), u'חמש עשרה')
        self.assertEqual(numinwords(16, lang="he"), u'שש עשרה')
        self.assertEqual(numinwords(19, lang="he"), u'תשע עשרה')

    def test_20_to_99(self):
        self.assertEqual(numinwords(20, lang="he"), u'עשרים')
        self.assertEqual(numinwords(23, lang="he"), u'עשרים ושלש')
        self.assertEqual(numinwords(28, lang="he"), u'עשרים ושמונה')
        self.assertEqual(numinwords(31, lang="he"), u'שלשים ואחת')
        self.assertEqual(numinwords(40, lang="he"), u'ארבעים')
        self.assertEqual(numinwords(66, lang="he"), u'ששים ושש')
        self.assertEqual(numinwords(92, lang="he"), u'תשעים ושתים')

    def test_100_to_999(self):
        self.assertEqual(numinwords(100, lang="he"), u'מאה')
        self.assertEqual(numinwords(111, lang="he"), u'מאה ואחת עשרה')
        self.assertEqual(numinwords(150, lang="he"), u'מאה וחמישים')
        self.assertEqual(numinwords(196, lang="he"), u'מאה תשעים ושש')
        self.assertEqual(numinwords(200, lang="he"), u'מאתיים')
        self.assertEqual(numinwords(210, lang="he"), u'מאתיים ועשר')
        self.assertEqual(numinwords(701, lang="he"), u'שבע מאות ואחת')

    def test_1000_to_9999(self):
        self.assertEqual(numinwords(1000, lang="he"), u'אלף')
        self.assertEqual(numinwords(1001, lang="he"), u'אלף ואחת')
        self.assertEqual(numinwords(1500, lang="he"), u'אלף וחמש מאות')
        self.assertEqual(
            numinwords(7378, lang="he"), u'שבעת אלפים שלש מאות שבעים ושמונה'
        )
        self.assertEqual(numinwords(2000, lang="he"), u'אלפיים')
        self.assertEqual(numinwords(2100, lang="he"), u'אלפיים ומאה')
        self.assertEqual(
            numinwords(6870, lang="he"), u'ששת אלפים שמונה מאות ושבעים'
        )
