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


class numinwordsROTest(TestCase):

    def test_ordinal(self):
        self.assertEqual(
            numinwords(1, lang='ro', to='ordinal'),
            'primul'
        )
        self.assertEqual(
            numinwords(22, lang='ro', to='ordinal'),
            u'al douăzeci și doilea'
        )
        self.assertEqual(
            numinwords(21, lang='ro', to='ordinal'),
            u'al douăzeci și unulea'
        )
        self.assertEqual(
            numinwords(12, lang='ro', to='ordinal'),
            u'al doisprezecelea'
        )
        self.assertEqual(
            numinwords(130, lang='ro', to='ordinal'),
            u'al o sută treizecilea'
        )
        self.assertEqual(
            numinwords(1003, lang='ro', to='ordinal'),
            u'al o mie treilea'
        )

    def test_ordinal_num(self):
        self.assertEqual(
            numinwords(1, lang='ro', to='ordinal_num'),
            '1-ul'
        )
        self.assertEqual(
            numinwords(10, lang='ro', to='ordinal_num'),
            'al 10-lea'
        )
        self.assertEqual(numinwords(
            21, lang='ro', to='ordinal_num'),
            'al 21-lea'
        )
        self.assertEqual(
            numinwords(102, lang='ro', to='ordinal_num'),
            'al 102-lea'
        )
        self.assertEqual(
            numinwords(73, lang='ro', to='ordinal_num'),
            'al 73-lea'
        )

    def test_cardinal_for_float_number(self):
        self.assertEqual(
            numinwords(12.5, lang='ro'),
            u'doisprezece virgulă cinci'
        )
        self.assertEqual(
            numinwords(12.51, lang='ro'),
            u'doisprezece virgulă cinci unu'
        )
        self.assertEqual(
            numinwords(12.53, lang='ro'),
            u'doisprezece virgulă cinci trei'
        )
        self.assertEqual(
            numinwords(12.59, lang='ro'),
            u'doisprezece virgulă cinci nouă'
        )

    def test_big_numbers(self):
        self.assertEqual(
            numinwords(1000000, lang="ro"),
            u"un milion"
        )
        self.assertEqual(
            numinwords(1000000000, lang="ro"),
            u"un miliard"
        )
        self.assertEqual(
            numinwords(33000000, lang="ro"),
            u"treizeci și trei milioane"
        )
        self.assertEqual(
            numinwords(247000000000, lang="ro"),
            u"două sute patruzeci și șapte de miliarde"
        )

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            numinwords(
                "100000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "000000000000000000000000000000000000000000000000000000"
                "0000000000000000000000000000000000000"
            )

    def test_to_currency(self):
        self.assertEqual(
            numinwords(1000, lang='ro', to='currency'),
            u'una mie de lei'
        )
        self.assertEqual(
            numinwords(101, lang='ro', to='currency'),
            u'una sută unu lei'
        )
        self.assertEqual(
            numinwords(100, lang='ro', to='currency'),
            u'una sută de lei'
        )
        self.assertEqual(
            numinwords(38.4, lang='ro', to='currency'),
            u'treizeci și opt de lei și patruzeci de bani'
        )
        self.assertEqual(
            numinwords(1.01, lang='ro', to='currency'),
            u'un leu și un ban'
        )
        self.assertEqual(
            numinwords(4778.00, lang='ro', to='currency'),
            u'patru mii șapte sute șaptezeci și opt de lei')
        self.assertEqual(
            numinwords(4778.32, lang='ro', to='currency'),
            u'patru mii șapte sute șaptezeci și opt de lei'
            u' și treizeci și doi de bani')
        self.assertEqual(
            numinwords(1207, lang='ro', to='currency'),
            u'una mie două sute șapte lei')
        self.assertEqual(
            numinwords(22000, lang='ro', to='currency'),
            u'douăzeci și două de mii de lei')
        self.assertEqual(
            numinwords(80000, lang='ro', to='currency'),
            u'optzeci de mii de lei')
        self.assertEqual(
            numinwords(123456789, lang='ro', to='currency'),
            u'una sută douăzeci și trei milioane patru sute '
            u'cincizeci și șase de mii șapte sute optzeci și nouă de lei')

    def test_to_year(self):
        self.assertEqual(numinwords(1989, lang='ro', to='year'),
                         u'o mie nouă sute optzeci și nouă')
        self.assertEqual(numinwords(1984, lang='ro', to='year'),
                         u'o mie nouă sute optzeci și patru')
        self.assertEqual(numinwords(2018, lang='ro', to='year'),
                         u'două mii optsprezece')
        self.assertEqual(numinwords(1066, lang='ro', to='year'),
                         u'o mie șaizeci și șase')
        self.assertEqual(numinwords(5000, lang='ro', to='year'),
                         u'cinci mii')
        self.assertEqual(numinwords(2001, lang='ro', to='year'),
                         u'două mii unu')
        self.assertEqual(numinwords(905, lang='ro', to='year'),
                         u'nouă sute cinci')
        self.assertEqual(numinwords(6600, lang='ro', to='year'),
                         u'șase mii șase sute')
        self.assertEqual(numinwords(1600, lang='ro', to='year'),
                         u'o mie șase sute')
        self.assertEqual(numinwords(700, lang='ro', to='year'),
                         u'șapte sute')
        self.assertEqual(numinwords(50, lang='ro', to='year'),
                         u'cincizeci')
        self.assertEqual(numinwords(0, lang='ro', to='year'),
                         u'zero')
        self.assertEqual(numinwords(10, lang='ro', to='year'),
                         u'zece')
        # suffixes
        self.assertEqual(numinwords(-44, lang='ro', to='year'),
                         u'patruzeci și patru î.Hr.')
        self.assertEqual(numinwords(-44, lang='ro', to='year',
                                    suffix=u'î.e.n.'),
                         u'patruzeci și patru î.e.n.')
        self.assertEqual(numinwords(1, lang='ro', to='year', suffix='d.Hr.'),
                         u'unu d.Hr.')
        self.assertEqual(numinwords(-66000000, lang='ro', to='year'),
                         u'șaizeci și șase milioane î.Hr.')
