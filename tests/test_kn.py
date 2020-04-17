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


from unittest import TestCase

from numinwords import numinwords


class numinwordsKNTest(TestCase):
    def test_numbers(self):
        self.assertEqual(numinwords(42, lang="kn"), u"ನಲವತ್ತ್ ಎರಡು")
        self.assertEqual(numinwords(893, lang="kn"), u"ಎಂಟು ನೂರ ತೊಂಬತ್ತ ಮೂರು")
        self.assertEqual(
            numinwords(1729, lang="kn"), u"ಒಂದು ಸಾವಿರ ಏಳು ನೂರ ಇಪ್ಪತ್ತ್ಒಂಬತ್ತು"
        )
        self.assertEqual(numinwords(123, lang="kn"), u"ಒಂದು ನೂರ ಇಪ್ಪತ್ತ್ ಮೂರು")
        self.assertEqual(numinwords(32211, lang="kn"),
                         u"ಮೂವತ್ತ್ಎರಡು ಸಾವಿರ ಎರಡು ನೂರ ಹನ್ನೊಂದು")

    def test_cardinal_for_float_number(self):
        self.assertEqual(numinwords(3.14, lang="kn"),
                         u"ಮೂರು ಬಿಂದು ಒಂದು ನಾಲ್ಕು")
        self.assertEqual(numinwords(1.61803, lang="kn"),
                         u"ಒಂದು ಬಿಂದು ಆರು ಒಂದು ಎಂಟು ಸೊನ್ನೆ ಮೂರು")

    def test_ordinal(self):
        self.assertEqual(
            numinwords(1, lang='kn', to='ordinal'),
            u'ಒಂದನೇ'
        )
        self.assertEqual(
            numinwords(22, lang='kn', to='ordinal'),
            u'ಇಪ್ಪತ್ತ್ ಎರಡನೇ'
        )
        self.assertEqual(
            numinwords(12, lang='kn', to='ordinal'),
            u'ಹನ್ನೆರಡನೇ'
        )
        self.assertEqual(
            numinwords(130, lang='kn', to='ordinal'),
            u'ಒಂದು ನೂರ ಮೂವತ್ತನೇ'
        )
        self.assertEqual(
            numinwords(1003, lang='kn', to='ordinal'),
            u'ಒಂದು ಸಾವಿರದ ಮೂರನೇ'
        )
        self.assertEqual(numinwords(2, lang="kn", ordinal=True), u"ಎರಡನೇ")
        self.assertEqual(numinwords(5, lang="kn", ordinal=True), u"ಐದನೇ")
        self.assertEqual(numinwords(16, lang="kn", ordinal=True), u"ಹದಿನಾರನೇ")
        self.assertEqual(numinwords(113, lang="kn", ordinal=True),
                         u"ಒಂದು ನೂರ ಹದಿಮೂರನೇ")

    def test_ordinal_num(self):
        self.assertEqual(numinwords(2, lang="kn", to='ordinal_num'), u"2ಎರಡನೇ")
        self.assertEqual(numinwords(5, lang="kn", to='ordinal_num'), u"5ಐದನೇ")
        self.assertEqual(numinwords(16, lang="kn", to='ordinal_num'),
                         u"16ಹದಿನಾರನೇ")
        self.assertEqual(numinwords(113, lang="kn", to='ordinal_num'),
                         u"113ಒಂದು ನೂರ ಹದಿಮೂರನೇ")
