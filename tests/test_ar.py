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


class numinwordsARTest(TestCase):

    def test_default_currency(self):
        self.assertEqual(numinwords(1, to='currency', lang='ar'), 'واحد ريال')
        self.assertEqual(numinwords(2, to='currency', lang='ar'),
                         'اثنان ريالان')
        self.assertEqual(numinwords(10, to='currency', lang='ar'),
                         'عشرة ريالات')
        self.assertEqual(numinwords(
            100, to='currency', lang='ar'), 'مائة ريال')
        self.assertEqual(numinwords(652.12, to='currency', lang='ar'),
                         'ستمائة و اثنان و خمسون ريالاً و اثنتا عشرة هللة')
        self.assertEqual(numinwords(324, to='currency', lang='ar'),
                         'ثلاثمائة و أربعة و عشرون ريالاً')
        self.assertEqual(numinwords(2000, to='currency', lang='ar'),
                         'ألفا ريال')
        self.assertEqual(numinwords(541, to='currency', lang='ar'),
                         'خمسمائة و واحد و أربعون ريالاً')
        self.assertEqual(numinwords(10000, to='currency', lang='ar'),
                         'عشرة آلاف ريال')
        self.assertEqual(numinwords(20000.12, to='currency', lang='ar'),
                         'عشرون ألف ريال و اثنتا عشرة هللة')
        self.assertEqual(numinwords(1000000, to='currency', lang='ar'),
                         'واحد مليون ريال')
        val = 'تسعمائة و ثلاثة و عشرون ألفاً  و أربعمائة و أحد عشر ريالاً'
        self.assertEqual(numinwords(923411, to='currency', lang='ar'), val)
        self.assertEqual(numinwords(63411, to='currency', lang='ar'),
                         'ثلاثة و ستون ألفاً  و أربعمائة و أحد عشر ريالاً')
        self.assertEqual(numinwords(1000000.99, to='currency', lang='ar'),
                         'واحد مليون ريال و تسع و تسعون هللة')

    def test_currency_parm(self):
        self.assertEqual(
            numinwords(1, to='currency', lang='ar', currency="KWD"),
            'واحد دينار')
        self.assertEqual(
            numinwords(10, to='currency', lang='ar', currency="EGP"),
            'عشرة جنيهات')
        self.assertEqual(
            numinwords(20000.12, to='currency', lang='ar', currency="EGP"),
            'عشرون ألف جنيه و اثنتا عشرة قرش')
        self.assertEqual(
            numinwords(923411, to='currency', lang='ar', currency="SR"),
            'تسعمائة و ثلاثة و عشرون ألفاً  و أربعمائة و أحد عشر ريالاً')
        self.assertEqual(
            numinwords(1000000.99, to='currency', lang='ar', currency="KWD"),
            'واحد مليون دينار و تسع و تسعون فلس')

    def test_ordinal(self):
        self.assertEqual(numinwords(1, to='ordinal', lang='ar'), 'اول')
        self.assertEqual(numinwords(2, to='ordinal', lang='ar'), 'ثاني')
        self.assertEqual(numinwords(3, to='ordinal', lang='ar'), 'ثالث')
        self.assertEqual(numinwords(4, to='ordinal', lang='ar'), 'رابع')
        self.assertEqual(numinwords(5, to='ordinal', lang='ar'), 'خامس')
        self.assertEqual(numinwords(6, to='ordinal', lang='ar'), 'سادس')
        self.assertEqual(numinwords(9, to='ordinal', lang='ar'), 'تاسع')
        self.assertEqual(numinwords(20, to='ordinal', lang='ar'), 'عشرون')
        self.assertEqual(numinwords(94, to='ordinal', lang='ar'),
                         'أربع و تسعون')
        self.assertEqual(numinwords(102, to='ordinal', lang='ar'),
                         'مائة و اثنان')
        self.assertEqual(
            numinwords(923411, to='ordinal_num', lang='ar'),
            'تسعمائة و ثلاثة و عشرون ألفاً  و أربعمائة و أحد عشر')

    def test_cardinal(self):
        self.assertEqual(numinwords(12, to='cardinal', lang='ar'), 'اثنا عشر')
        self.assertEqual(numinwords(-8324, to='cardinal', lang='ar'),
                         'سالب ثمانية آلاف  و ثلاثمائة و أربعة و عشرون')
        self.assertEqual(
            numinwords(3431.12, to='cardinal', lang='ar'),
            'ثلاثة آلاف  و أربعمائة و واحد و ثلاثون  , اثنتا عشرة')
        self.assertEqual(numinwords(431, to='cardinal', lang='ar'),
                         'أربعمائة و واحد و ثلاثون')
        self.assertEqual(numinwords(94231, to='cardinal', lang='ar'),
                         'أربعة و تسعون ألفاً  و مئتان و واحد و ثلاثون')
        self.assertEqual(numinwords(1431, to='cardinal', lang='ar'),
                         'واحد ألف  و أربعمائة و واحد و ثلاثون')

    def test_prefix_and_suffix(self):
        self.assertEqual(numinwords(645, to='currency',
                                    lang='ar', prefix="فقط", suffix="لاغير"),
                         'فقط ستمائة و خمسة و أربعون ريالاً لاغير')

    def test_year(self):
        self.assertEqual(numinwords(2000, to='year', lang='ar'), 'ألفا')

    def test_max_numbers(self):
        with self.assertRaises(Exception) as context:
            numinwords(10 ** 36, to='year', lang='ar')

        self.assertTrue('Too large' in str(context.exception))
