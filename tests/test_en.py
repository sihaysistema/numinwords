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


class numinwordsENTest(TestCase):
    def test_and_join_199(self):
        # ref https://github.com/savoirfairelinux/numinwords/issues/8
        self.assertEqual(numinwords(199), "one hundred and ninety-nine")

    def test_ordinal(self):
        self.assertEqual(
            numinwords(0, lang='en', to='ordinal'),
            'zeroth'
        )
        self.assertEqual(
            numinwords(1, lang='en', to='ordinal'),
            'first'
        )
        self.assertEqual(
            numinwords(13, lang='en', to='ordinal'),
            'thirteenth'
        )
        self.assertEqual(
            numinwords(22, lang='en', to='ordinal'),
            'twenty-second'
        )
        self.assertEqual(
            numinwords(12, lang='en', to='ordinal'),
            'twelfth'
        )
        self.assertEqual(
            numinwords(130, lang='en', to='ordinal'),
            'one hundred and thirtieth'
        )
        self.assertEqual(
            numinwords(1003, lang='en', to='ordinal'),
            'one thousand and third'
        )

    def test_ordinal_num(self):
        self.assertEqual(numinwords(10, lang='en', to='ordinal_num'), '10th')
        self.assertEqual(numinwords(21, lang='en', to='ordinal_num'), '21st')
        self.assertEqual(numinwords(102, lang='en', to='ordinal_num'), '102nd')
        self.assertEqual(numinwords(73, lang='en', to='ordinal_num'), '73rd')

    def test_cardinal_for_float_number(self):
        # issue 24
        self.assertEqual(numinwords(12.5), "twelve point five")
        self.assertEqual(numinwords(12.51), "twelve point five one")
        self.assertEqual(numinwords(12.53), "twelve point five three")
        self.assertEqual(numinwords(12.59), "twelve point five nine")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            numinwords(
                "1000000000000000000000000000000000000000000000000000000"
                "0000000000000000000000000000000000000000000000000000000"
                "0000000000000000000000000000000000000000000000000000000"
                "0000000000000000000000000000000000000000000000000000000"
                "0000000000000000000000000000000000000000000000000000000"
                "00000000000000000000000000000000"
            )

    def test_to_currency(self):
        self.assertEqual(
            numinwords('38.4', lang='en', to='currency', separator=' and',
                       cents=False, currency='USD'),
            "thirty-eight dollars and 40 cents"
        )
        self.assertEqual(
            numinwords('0', lang='en', to='currency', separator=' and',
                       cents=False, currency='USD'),
            "zero dollars and 00 cents"
        )

        self.assertEqual(
            numinwords('1.01', lang='en', to='currency', separator=' and',
                       cents=True, currency='USD'),
            "one dollar and one cent"
        )

        self.assertEqual(
            numinwords('4778.00', lang='en', to='currency', separator=' and',
                       cents=True, currency='USD', adjective=True),
            'four thousand, seven hundred and seventy-eight US dollars'
            ' and zero cents')

        self.assertEqual(
            numinwords('4778.00', lang='en', to='currency', separator=' and',
                       cents=True, currency='USD'),
            'four thousand, seven hundred and seventy-eight dollars and'
            ' zero cents')

        self.assertEqual(
            numinwords('1.1', lang='en', to='currency', separator=' and',
                       cents=True, currency='MXN'),
            "one peso and ten cents"
        )

        self.assertEqual(
            numinwords('158.3', lang='en', to='currency', separator=' and',
                       cents=True, currency='MXN'),
            "one hundred and fifty-eight pesos and thirty cents"
        )

        self.assertEqual(
            numinwords('2000.00', lang='en', to='currency', separator=' and',
                       cents=True, currency='MXN'),
            "two thousand pesos and zero cents"
        )

        self.assertEqual(
            numinwords('4.01', lang='en', to='currency', separator=' and',
                       cents=True, currency='MXN'),
            "four pesos and one cent"
        )

    def test_to_year(self):
        # issue 141
        # "e2 e2"
        self.assertEqual(numinwords(1990, lang='en', to='year'),
                         'nineteen ninety')
        self.assertEqual(numinwords(5555, lang='en', to='year'),
                         'fifty-five fifty-five')
        self.assertEqual(numinwords(2017, lang='en', to='year'),
                         'twenty seventeen')
        self.assertEqual(numinwords(1066, lang='en', to='year'),
                         'ten sixty-six')
        self.assertEqual(numinwords(1865, lang='en', to='year'),
                         'eighteen sixty-five')
        # "e3 and e1"; "e2 oh-e1"; "e3"
        self.assertEqual(numinwords(3000, lang='en', to='year'),
                         'three thousand')
        self.assertEqual(numinwords(2001, lang='en', to='year'),
                         'two thousand and one')
        self.assertEqual(numinwords(1901, lang='en', to='year'),
                         'nineteen oh-one')
        self.assertEqual(numinwords(2000, lang='en', to='year'),
                         'two thousand')
        self.assertEqual(numinwords(905, lang='en', to='year'),
                         'nine oh-five')
        # "e2 hundred"; "e3"
        self.assertEqual(numinwords(6600, lang='en', to='year'),
                         'sixty-six hundred')
        self.assertEqual(numinwords(1900, lang='en', to='year'),
                         'nineteen hundred')
        self.assertEqual(numinwords(600, lang='en', to='year'),
                         'six hundred')
        self.assertEqual(numinwords(50, lang='en', to='year'),
                         'fifty')
        self.assertEqual(numinwords(0, lang='en', to='year'),
                         'zero')
        # suffixes
        self.assertEqual(numinwords(-44, lang='en', to='year'),
                         'forty-four BC')
        self.assertEqual(numinwords(-44, lang='en', to='year', suffix='BCE'),
                         'forty-four BCE')
        self.assertEqual(numinwords(1, lang='en', to='year', suffix='AD'),
                         'one AD')
        self.assertEqual(numinwords(66, lang='en', to='year',
                                    suffix='m.y.a.'),
                         'sixty-six m.y.a.')
        self.assertEqual(numinwords(-66000000, lang='en', to='year'),
                         'sixty-six million BC')
