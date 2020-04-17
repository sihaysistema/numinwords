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


class numinwordsIDTest(TestCase):
    def test_cardinal_for_natural_number(self):
        self.assertEqual(numinwords(10, lang='id'), "sepuluh")
        self.assertEqual(numinwords(11, lang='id'), "sebelas")
        self.assertEqual(numinwords(108, lang='id'), "seratus delapan")
        self.assertEqual(numinwords(1075, lang='id'),
                         "seribu tujuh puluh lima")
        self.assertEqual(
            numinwords(1087231, lang='id'),
            "satu juta delapan puluh tujuh ribu dua ratus tiga puluh satu"
        )
        self.assertEqual(
            numinwords(1000000408, lang='id'),
            "satu miliar empat ratus delapan"
        )

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            numinwords(12.234, lang='id'), "dua belas koma dua tiga empat"
        )
        self.assertEqual(
            numinwords(9.076, lang='id'), "sembilan koma nol tujuh enam"
        )

    def test_cardinal_for_negative_number(self):
        self.assertEqual(
            numinwords(-923, lang='id'), "min sembilan ratus dua puluh tiga"
        )
        self.assertEqual(
            numinwords(-0.234, lang='id'), "min nol koma dua tiga empat"
        )

    def test_ordinal_for_natural_number(self):
        self.assertEqual(numinwords(1, ordinal=True, lang='id'), "pertama")
        self.assertEqual(numinwords(10, ordinal=True, lang='id'), "kesepuluh")

    def test_ordinal_for_negative_number(self):
        self.assertRaises(TypeError, numinwords, -12, ordinal=True, lang='id')

    def test_ordinal_for_floating_number(self):
        self.assertRaises(TypeError, numinwords, 3.243,
                          ordinal=True, lang='id')
