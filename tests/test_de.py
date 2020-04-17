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

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'ein Euro und null Cent'),
    (2.01, 'zwei Euro und ein Cent'),
    (8.10, 'acht Euro und zehn Cent'),
    (12.26, 'zwölf Euro und sechsundzwanzig Cent'),
    (21.29, 'einundzwanzig Euro und neunundzwanzig Cent'),
    (81.25, 'einundachtzig Euro und fünfundzwanzig Cent'),
    (100.00, 'einhundert Euro und null Cent'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'ein Dollar und null Cent'),
    (2.01, 'zwei Dollar und ein Cent'),
    (8.10, 'acht Dollar und zehn Cent'),
    (12.26, 'zwölf Dollar und sechsundzwanzig Cent'),
    (21.29, 'einundzwanzig Dollar und neunundzwanzig Cent'),
    (81.25, 'einundachtzig Dollar und fünfundzwanzig Cent'),
    (100.00, 'einhundert Dollar und null Cent'),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, 'ein Pfund und null Pence'),
    (2.01, 'zwei Pfund und ein Penny'),
    (8.10, 'acht Pfund und zehn Pence'),
    (12.26, 'zwölf Pfund und sechsundzwanzig Pence'),
    (21.29, 'einundzwanzig Pfund und neunundzwanzig Pence'),
    (81.25, 'einundachtzig Pfund und fünfundzwanzig Pence'),
    (100.00, 'einhundert Pfund und null Pence'),
)

TEST_CASES_TO_CURRENCY_DEM = (
    (1.00, 'ein Mark und null Pfennig'),
    (2.01, 'zwei Mark und ein Pfennig'),
    (8.10, 'acht Mark und zehn Pfennig'),
    (12.26, 'zwölf Mark und sechsundzwanzig Pfennig'),
    (21.29, 'einundzwanzig Mark und neunundzwanzig Pfennig'),
    (81.25, 'einundachtzig Mark und fünfundzwanzig Pfennig'),
    (100.00, 'einhundert Mark und null Pfennig'),
)


class numinwordsDETest(TestCase):

    def test_ordinal_less_than_twenty(self):
        self.assertEqual(numinwords(0, ordinal=True, lang='de'), "nullte")
        self.assertEqual(numinwords(1, ordinal=True, lang='de'), "erste")
        self.assertEqual(numinwords(7, ordinal=True, lang='de'), "siebte")
        self.assertEqual(numinwords(8, ordinal=True, lang='de'), "achte")
        self.assertEqual(numinwords(12, ordinal=True, lang='de'), "zwölfte")
        self.assertEqual(numinwords(17, ordinal=True, lang='de'), "siebzehnte")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            numinwords(81, ordinal=True, lang='de'), "einundachtzigste"
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(
            numinwords(100, ordinal=True, lang='de'), "hundertste"
        )
        self.assertEqual(
            numinwords(1000, ordinal=True, lang='de'), "tausendste"
        )
        self.assertEqual(
            numinwords(4000, ordinal=True, lang='de'), "viertausendste"
        )
        self.assertEqual(
            numinwords(1000000, ordinal=True, lang='de'), "millionste"
        )
        self.assertEqual(
            numinwords(2000000, ordinal=True, lang='de'), "zweimillionste"
        )
        self.assertEqual(
            numinwords(1000000000, ordinal=True, lang='de'), "milliardste"
        )
        self.assertEqual(
            numinwords(5000000000, ordinal=True, lang='de'),
            "fünfmilliardste"
        )

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(numinwords(100, lang='de'), "einhundert")
        self.assertEqual(numinwords(1000, lang='de'), "eintausend")
        self.assertEqual(numinwords(5000, lang='de'), "fünftausend")
        self.assertEqual(numinwords(10000, lang='de'), "zehntausend")
        self.assertEqual(numinwords(1000000, lang='de'), "eine Million")
        self.assertEqual(numinwords(2000000, lang='de'), "zwei Millionen")
        self.assertEqual(numinwords(4000000000, lang='de'), "vier Milliarden")
        self.assertEqual(numinwords(1000000000, lang='de'), "eine Milliarde")

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            numinwords(3.486, lang='de'), "drei Komma vier acht sechs"
        )

    def test_giant_cardinal_for_merge(self):
        self.assertEqual(
            numinwords(4500072900000111, lang='de'),
            "vier Billiarden fünfhundert Billionen " +
            "zweiundsiebzig Milliarden neunhundert Millionen einhundertelf"
        )

    def test_ordinal_num(self):
        self.assertEqual(numinwords(7, to="ordinal_num", lang='de'), "7.")
        self.assertEqual(numinwords(81, to="ordinal_num", lang='de'), "81.")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, numinwords, -12, ordinal=True, lang='de')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, numinwords, 2.453, ordinal=True,
                          lang='de')

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                numinwords(test[0], lang='de', to='currency', currency='EUR'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                numinwords(test[0], lang='de', to='currency', currency='USD'),
                test[1]
            )

    def test_currency_dem(self):
        for test in TEST_CASES_TO_CURRENCY_DEM:
            self.assertEqual(
                numinwords(test[0], lang='de', to='currency', currency='DEM'),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                numinwords(test[0], lang='de', to='currency', currency='GBP'),
                test[1]
            )

    def test_year(self):
        self.assertEqual(numinwords(2002, to='year', lang='de'),
                         'zweitausendzwei')

    def test_year_before_2000(self):
        self.assertEqual(numinwords(1780, to='year', lang='de'),
                         'siebzehnhundertachtzig')
