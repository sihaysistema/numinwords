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
from numinwords.lang_NL import Num2Word_NL


class numinwordsNLTest(TestCase):
    def test_ordinal_less_than_twenty(self):
        self.assertEqual(numinwords(7, ordinal=True, lang='nl'), "zevende")
        self.assertEqual(numinwords(8, ordinal=True, lang='nl'), "achtste")
        self.assertEqual(numinwords(12, ordinal=True, lang='nl'), "twaalfde")
        self.assertEqual(numinwords(17, ordinal=True, lang='nl'),
                         "zeventiende")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            numinwords(81, ordinal=True, lang='nl'), "eenentachtigste"
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(numinwords(100, ordinal=True, lang='nl'),
                         "honderdste")
        self.assertEqual(
            numinwords(1000, ordinal=True, lang='nl'), "duizendste"
        )
        self.assertEqual(
            numinwords(4000, ordinal=True, lang='nl'), "vierduizendste"
        )
        self.assertEqual(
            numinwords(2000000, ordinal=True, lang='nl'), "twee miljoenste"
        )
        self.assertEqual(
            numinwords(5000000000, ordinal=True, lang='nl'), "vijf miljardste"
        )

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(numinwords(82, lang='nl'), u'twee\xebntachtig')
        self.assertEqual(numinwords(1013, lang='nl'), "duizenddertien")
        self.assertEqual(numinwords(2000000, lang='nl'), "twee miljoen")
        self.assertEqual(numinwords(4000000000, lang='nl'), "vier miljard")

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            numinwords(3.486, lang='nl'), "drie komma vier acht zes"
        )

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, numinwords, -12, ordinal=True, lang='nl')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, numinwords, 2.453, ordinal=True,
                          lang='nl')

    def test_to_currency_eur(self):
        self.assertEqual(
            numinwords('38.4', lang='nl', to='currency', separator=' en',
                       cents=False, currency='EUR'),
            "achtendertig euro en 40 cent"
        )
        self.assertEqual(
            numinwords('0', lang='nl', to='currency', separator=' en',
                       cents=False, currency='EUR'),
            "nul euro en 00 cent"
        )

        self.assertEqual(
            numinwords('1.01', lang='nl', to='currency', separator=' en',
                       cents=True, currency='EUR'),
            "één euro en één cent"
        )

        self.assertEqual(
            numinwords('4778.00', lang='nl', to='currency', separator=' en',
                       cents=True, currency='EUR'),
            'vierduizendzevenhonderdachtenzeventig euro en nul cent')

    def test_to_currency_usd(self):
        self.assertEqual(
            numinwords('38.4', lang='nl', to='currency', separator=' en',
                       cents=False, currency='USD'),
            "achtendertig dollar en 40 cent"
        )
        self.assertEqual(
            numinwords('0', lang='nl', to='currency', separator=' en',
                       cents=False, currency='USD'),
            "nul dollar en 00 cent"
        )

        self.assertEqual(
            numinwords('1.01', lang='nl', to='currency', separator=' en',
                       cents=True, currency='USD'),
            "één dollar en één cent"
        )

        self.assertEqual(
            numinwords('4778.00', lang='nl', to='currency', separator=' en',
                       cents=True, currency='USD'),
            'vierduizendzevenhonderdachtenzeventig dollar en nul cent')

    def test_pluralize(self):
        n = Num2Word_NL()
        # euros always singular
        cr1, cr2 = n.CURRENCY_FORMS['EUR']
        self.assertEqual(n.pluralize(1, cr1), 'euro')
        self.assertEqual(n.pluralize(2, cr1), 'euro')
        self.assertEqual(n.pluralize(1, cr2), 'cent')
        self.assertEqual(n.pluralize(2, cr2), 'cent')

        # @TODO other currency

    def test_to_year(self):
        self.assertEqual(numinwords(2018, lang='nl', to='year'),
                         'tweeduizendachttien')
        self.assertEqual(numinwords(2100, lang='nl', to='year'),
                         'eenentwintig honderd')
