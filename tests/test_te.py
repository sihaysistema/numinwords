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


class numinwordsTETest(TestCase):
    def test_numbers(self):
        self.assertEqual(numinwords(66, lang="te"), u"అరవై ఆరు")
        self.assertEqual(numinwords(1734, lang="te"),
                         u"ఒకటి వేయి ఏడు వందల ముప్పై నాలుగు")
        self.assertEqual(numinwords(134, lang="te"),
                         u"ఒకటి వందల ముప్పై నాలుగు")
        self.assertEqual(numinwords(54411, lang="te"),
                         u"యాభై నాలుగు వేయి నాలుగు వందల పదకొండు")
        self.assertEqual(numinwords(42, lang="te"), u"నలభై రెండు")
        self.assertEqual(numinwords(893, lang="te"),
                         u"ఎనిమిది వందల తొంభై మూడు")
        self.assertEqual(
            numinwords(1729, lang="te"), u"ఒకటి వేయి ఏడు వందల ఇరవై తొమ్మిది"
        )
        self.assertEqual(numinwords(123, lang="te"), u"ఒకటి వందల ఇరవై మూడు")
        self.assertEqual(numinwords(32211, lang="te"),
                         u"ముప్పై రెండు వేయి రెండు వందల పదకొండు")

    def test_cardinal_for_float_number(self):
        self.assertEqual(numinwords(1.61803, lang="te"),
                         u"ఒకటి బిందువు  ఆరు ఒకటి ఎనిమిది సున్న మూడు")
        self.assertEqual(numinwords(34.876, lang="te"),
                         u"ముప్పై నాలుగు బిందువు  ఎనిమిది ఏడు ఆరు")
        self.assertEqual(numinwords(3.14, lang="te"),
                         u"మూడు బిందువు  ఒకటి నాలుగు")

    def test_ordinal(self):
        self.assertEqual(numinwords(1, lang='te', to='ordinal'), u"ఒకటివ")
        self.assertEqual(numinwords(22, lang='te', to='ordinal'),
                         u"ఇరవై రెండువ")
        self.assertEqual(numinwords(23, lang='te', to='ordinal'),
                         u"ఇరవై మూడువ")
        self.assertEqual(numinwords(12, lang='te', to='ordinal'), u"పన్నెండువ")
        self.assertEqual(numinwords(130, lang='te', to='ordinal'),
                         u"ఒకటి వందల ముప్పైవ")
        self.assertEqual(numinwords(1003, lang='te', to='ordinal'),
                         u"ఒకటి వేయిల మూడువ")
        self.assertEqual(numinwords(4, lang='te', to='ordinal'),
                         u"నాలుగువ")

    def test_ordinal_num(self):
        self.assertEqual(numinwords(2, lang="te", to='ordinal_num'), u"2వ")
        self.assertEqual(numinwords(3, lang="te", to='ordinal_num'), u"3వ")
        self.assertEqual(numinwords(5, lang="te", to='ordinal_num'), u"5వ")
        self.assertEqual(numinwords(16, lang="te", to='ordinal_num'), u"16వ")
        self.assertEqual(numinwords(113, lang="te", to='ordinal_num'),
                         u"113వ")
