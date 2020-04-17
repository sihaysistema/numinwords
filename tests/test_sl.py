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


class numinwordsSLTest(TestCase):
    def test_ordinal_less_than_twenty(self):
        self.assertEqual(numinwords(2, ordinal=True, lang='sl'), "drugi")
        self.assertEqual(numinwords(4, ordinal=True, lang='sl'), "četrti")
        self.assertEqual(numinwords(7, ordinal=True, lang='sl'), "sedmi")
        self.assertEqual(numinwords(8, ordinal=True, lang='sl'), "osmi")
        self.assertEqual(numinwords(12, ordinal=True, lang='sl'), "dvanajsti")
        self.assertEqual(numinwords(
            17, ordinal=True, lang='sl'), "sedemnajsti")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            numinwords(81, ordinal=True, lang='sl'), "enainosemdeseti"
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(numinwords(100, ordinal=True, lang='sl'), "stoti")
        self.assertEqual(numinwords(1000, ordinal=True, lang='sl'), "tisoči")
        self.assertEqual(
            numinwords(4000, ordinal=True, lang='sl'), "štiritisoči"
        )
        self.assertEqual(
            numinwords(2000000, ordinal=True, lang='sl'), "dvamilijonti"
        )
        self.assertEqual(
            numinwords(5000000000, ordinal=True, lang='sl'), "petmilijardti"
        )

    def test_ordinal_numbers_from_repository_of_test_cases(self):
        # Tests were compiled from cases in
        # https://github.com/gregopet/zapis-slovenskih-stevil
        # The male gender is used by the project so those test cases were
        # copied
        self.assertEqual(numinwords(1, ordinal=True, lang='sl'), "prvi")
        self.assertEqual(numinwords(2, ordinal=True, lang='sl'), "drugi")
        self.assertEqual(numinwords(3, ordinal=True, lang='sl'), "tretji")
        self.assertEqual(numinwords(4, ordinal=True, lang='sl'), "četrti")
        self.assertEqual(numinwords(5, ordinal=True, lang='sl'), "peti")
        self.assertEqual(numinwords(6, ordinal=True, lang='sl'), "šesti")
        self.assertEqual(numinwords(7, ordinal=True, lang='sl'), "sedmi")
        self.assertEqual(numinwords(8, ordinal=True, lang='sl'), "osmi")
        self.assertEqual(numinwords(9, ordinal=True, lang='sl'), "deveti")
        self.assertEqual(numinwords(10, ordinal=True, lang='sl'), "deseti")
        self.assertEqual(numinwords(100, ordinal=True, lang='sl'), "stoti")
        self.assertEqual(numinwords(101, ordinal=True, lang='sl'), "stoprvi")
        self.assertEqual(numinwords(102, ordinal=True, lang='sl'), "stodrugi")
        self.assertEqual(numinwords(103, ordinal=True, lang='sl'), "stotretji")
        self.assertEqual(numinwords(104, ordinal=True, lang='sl'), "stočetrti")
        self.assertEqual(numinwords(105, ordinal=True, lang='sl'), "stopeti")
        self.assertEqual(numinwords(106, ordinal=True, lang='sl'), "stošesti")
        self.assertEqual(numinwords(200, ordinal=True, lang='sl'), "dvestoti")
        self.assertEqual(numinwords(1000, ordinal=True, lang='sl'), "tisoči")
        self.assertEqual(numinwords(
            1001, ordinal=True, lang='sl'), "tisočprvi")
        self.assertEqual(numinwords(1002, ordinal=True, lang='sl'),
                         "tisočdrugi")
        self.assertEqual(numinwords(1003, ordinal=True, lang='sl'),
                         "tisočtretji")
        self.assertEqual(numinwords(1004, ordinal=True, lang='sl'),
                         "tisoččetrti")
        self.assertEqual(numinwords(1005, ordinal=True, lang='sl'),
                         "tisočpeti")
        self.assertEqual(numinwords(1006, ordinal=True, lang='sl'),
                         "tisočšesti")
        self.assertEqual(numinwords(2000, ordinal=True, lang='sl'),
                         "dvatisoči")
        self.assertEqual(numinwords(20000, ordinal=True, lang='sl'),
                         "dvajsettisoči")
        self.assertEqual(numinwords(200000, ordinal=True, lang='sl'),
                         "dvestotisoči")
        self.assertEqual(numinwords(1000000, ordinal=True, lang='sl'),
                         "milijonti")
        self.assertEqual(numinwords(2000000, ordinal=True, lang='sl'),
                         "dvamilijonti")
        self.assertEqual(numinwords(3000000, ordinal=True, lang='sl'),
                         "trimilijonti")
        self.assertEqual(numinwords(101000000, ordinal=True, lang='sl'),
                         "stoenmilijonti")
        self.assertEqual(numinwords(202000000, ordinal=True, lang='sl'),
                         "dvestodvamilijonti")
        self.assertEqual(numinwords(1121, ordinal=True, lang='sl'),
                         "tisočstoenaindvajseti")
        self.assertEqual(numinwords(2405, ordinal=True, lang='sl'),
                         "dvatisočštiristopeti")

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(numinwords(2, lang='sl'), "dve")
        self.assertEqual(numinwords(4000, lang='sl'), "štiri tisoč")
        self.assertEqual(numinwords(2000000, lang='sl'), "dva milijona")
        self.assertEqual(numinwords(4000000000, lang='sl'), "štiri milijarde")

    def test_cardinal_numbers_from_repository_of_test_cases(self):
        # Tests were compiled from cases in
        # https://github.com/gregopet/zapis-slovenskih-stevil
        self.assertEqual(numinwords(0, lang='sl'), "nič")
        self.assertEqual(numinwords(1, lang='sl'), "ena")
        self.assertEqual(numinwords(2, lang='sl'), "dve")
        self.assertEqual(numinwords(3, lang='sl'), "tri")
        self.assertEqual(numinwords(4, lang='sl'), "štiri")
        self.assertEqual(numinwords(5, lang='sl'), "pet")
        self.assertEqual(numinwords(6, lang='sl'), "šest")
        self.assertEqual(numinwords(7, lang='sl'), "sedem")
        self.assertEqual(numinwords(8, lang='sl'), "osem")
        self.assertEqual(numinwords(9, lang='sl'), "devet")
        self.assertEqual(numinwords(10, lang='sl'), "deset")
        self.assertEqual(numinwords(11, lang='sl'), "enajst")
        self.assertEqual(numinwords(12, lang='sl'), "dvanajst")
        self.assertEqual(numinwords(13, lang='sl'), "trinajst")
        self.assertEqual(numinwords(14, lang='sl'), "štirinajst")
        self.assertEqual(numinwords(15, lang='sl'), "petnajst")
        self.assertEqual(numinwords(16, lang='sl'), "šestnajst")
        self.assertEqual(numinwords(17, lang='sl'), "sedemnajst")
        self.assertEqual(numinwords(18, lang='sl'), "osemnajst")
        self.assertEqual(numinwords(19, lang='sl'), "devetnajst")
        self.assertEqual(numinwords(20, lang='sl'), "dvajset")
        self.assertEqual(numinwords(21, lang='sl'), "enaindvajset")
        self.assertEqual(numinwords(22, lang='sl'), "dvaindvajset")
        self.assertEqual(numinwords(23, lang='sl'), "triindvajset")
        self.assertEqual(numinwords(24, lang='sl'), "štiriindvajset")
        self.assertEqual(numinwords(25, lang='sl'), "petindvajset")
        self.assertEqual(numinwords(26, lang='sl'), "šestindvajset")
        self.assertEqual(numinwords(27, lang='sl'), "sedemindvajset")
        self.assertEqual(numinwords(28, lang='sl'), "osemindvajset")
        self.assertEqual(numinwords(29, lang='sl'), "devetindvajset")
        self.assertEqual(numinwords(30, lang='sl'), "trideset")
        self.assertEqual(numinwords(40, lang='sl'), "štirideset")
        self.assertEqual(numinwords(50, lang='sl'), "petdeset")
        self.assertEqual(numinwords(60, lang='sl'), "šestdeset")
        self.assertEqual(numinwords(70, lang='sl'), "sedemdeset")
        self.assertEqual(numinwords(80, lang='sl'), "osemdeset")
        self.assertEqual(numinwords(90, lang='sl'), "devetdeset")
        self.assertEqual(numinwords(100, lang='sl'), "sto")
        self.assertEqual(numinwords(101, lang='sl'), "sto ena")
        self.assertEqual(numinwords(102, lang='sl'), "sto dve")
        self.assertEqual(numinwords(103, lang='sl'), "sto tri")
        self.assertEqual(numinwords(104, lang='sl'), "sto štiri")
        self.assertEqual(numinwords(105, lang='sl'), "sto pet")
        self.assertEqual(numinwords(106, lang='sl'), "sto šest")
        self.assertEqual(numinwords(200, lang='sl'), "dvesto")
        self.assertEqual(numinwords(300, lang='sl'), "tristo")
        self.assertEqual(numinwords(400, lang='sl'), "štiristo")
        self.assertEqual(numinwords(500, lang='sl'), "petsto")
        self.assertEqual(numinwords(600, lang='sl'), "šeststo")
        self.assertEqual(numinwords(700, lang='sl'), "sedemsto")
        self.assertEqual(numinwords(800, lang='sl'), "osemsto")
        self.assertEqual(numinwords(900, lang='sl'), "devetsto")
        self.assertEqual(numinwords(1000, lang='sl'), "tisoč")
        self.assertEqual(numinwords(1001, lang='sl'), "tisoč ena")
        self.assertEqual(numinwords(1002, lang='sl'), "tisoč dve")
        self.assertEqual(numinwords(1003, lang='sl'), "tisoč tri")
        self.assertEqual(numinwords(1004, lang='sl'), "tisoč štiri")
        self.assertEqual(numinwords(1005, lang='sl'), "tisoč pet")
        self.assertEqual(numinwords(1006, lang='sl'), "tisoč šest")
        self.assertEqual(numinwords(2000, lang='sl'), "dva tisoč")
        self.assertEqual(numinwords(20000, lang='sl'), "dvajset tisoč")
        self.assertEqual(numinwords(100000, lang='sl'), "sto tisoč")
        self.assertEqual(numinwords(101000, lang='sl'), "sto en tisoč")
        self.assertEqual(numinwords(200000, lang='sl'), "dvesto tisoč")
        self.assertEqual(numinwords(1000000, lang='sl'), "milijon")
        self.assertEqual(numinwords(2000000, lang='sl'), "dva milijona")
        self.assertEqual(numinwords(3000000, lang='sl'), "trije milijoni")
        self.assertEqual(numinwords(101000000, lang='sl'), "sto en milijon")
        self.assertEqual(numinwords(202000000, lang='sl'),
                         "dvesto dva milijona")
        self.assertEqual(numinwords(303000000, lang='sl'),
                         "tristo trije milijoni")
        self.assertEqual(numinwords(304000000, lang='sl'),
                         "tristo štirje milijoni")
        self.assertEqual(numinwords(1000000000, lang='sl'), "milijarda")
        self.assertEqual(numinwords(2000000000, lang='sl'), "dve milijardi")
        self.assertEqual(numinwords(1121, lang='sl'), "tisoč sto enaindvajset")
        self.assertEqual(numinwords(2401, lang='sl'), "dva tisoč štiristo ena")
        self.assertEqual(numinwords(201001004, lang='sl'),
                         "dvesto en milijon tisoč štiri")
        self.assertEqual(
            numinwords(1803603801, lang='sl'),
            "milijarda osemsto trije milijoni šeststo tri tisoč osemsto ena")

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(numinwords(3.48, lang='sl'), "tri celih štiri osem")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, numinwords, -12, ordinal=True, lang='sl')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, numinwords, 2.453,
                          ordinal=True, lang='sl')
