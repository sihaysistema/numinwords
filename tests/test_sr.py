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


class numinwordsSRTest(TestCase):

    def test_cardinal(self):
        self.assertEqual("sto", numinwords(100, lang='sr'))
        self.assertEqual("sto jedan", numinwords(101, lang='sr'))
        self.assertEqual("sto deset", numinwords(110, lang='sr'))
        self.assertEqual("sto petnaest", numinwords(115, lang='sr'))
        self.assertEqual(
            "sto dvadeset tri", numinwords(123, lang='sr')
        )
        self.assertEqual(
            "jedna hiljada", numinwords(1000, lang='sr')
        )
        self.assertEqual(
            "jedna hiljada jedan", numinwords(1001, lang='sr')
        )
        self.assertEqual(
            "dve hiljade dvanaest", numinwords(2012, lang='sr')
        )
        self.assertEqual(
            "dvanaest hiljada petsto devetnaest zapeta osamdeset pet",
            numinwords(12519.85, lang='sr')
        )
        self.assertEqual(
            "jedan bilion dvesta trideset četiri miliona petsto "
            "šezdeset sedam hiljada osamsto devedeset",
            numinwords(1234567890, lang='sr')
        )
        self.assertEqual(
            "dvesta petnaest noniliona četristo šezdeset jedan "
            "oktilion četristo sedam septiliona osamsto devedeset "
            "dva sekstiliona trideset devet kvintiliona dva kvadriliona "
            "sto pedeset sedam triliona sto osamdeset devet biliona "
            "osamsto osamdeset tri miliona devetsto jedna hiljada "
            "šesto sedamdeset šest",
            numinwords(215461407892039002157189883901676, lang='sr')
        )
        self.assertEqual(
            "sedamsto devetnaest noniliona devedeset četiri oktiliona "
            "dvesta trideset četiri septiliona šesto devedeset tri "
            "sekstiliona šesto šezdeset tri kvintiliona trideset "
            "četiri kvadriliona osamsto dvadeset dva triliona osamsto "
            "dvadeset četiri biliona trista osamdeset četiri miliona "
            "dvesta dvadeset hiljada dvesta devedeset jedan",
            numinwords(719094234693663034822824384220291, lang='sr')
        )
        self.assertEqual("pet", numinwords(5, lang='sr'))
        self.assertEqual("petnaest", numinwords(15, lang='sr'))
        self.assertEqual("sto pedeset četiri", numinwords(154, lang='sr'))
        self.assertEqual(
            "jedna hiljada sto trideset pet",
            numinwords(1135, lang='sr')
        )
        self.assertEqual(
            "četristo osamnaest hiljada petsto trideset jedan",
            numinwords(418531, lang='sr'),
        )
        self.assertEqual(
            "jedan milion sto trideset devet",
            numinwords(1000139, lang='sr')
        )

    def test_floating_point(self):
        self.assertEqual("pet zapeta dva", numinwords(5.2, lang='sr'))
        self.assertEqual(
            "petsto šezdeset jedan zapeta četrdeset dva",
            numinwords(561.42, lang='sr')
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            numinwords(1, lang='sr', to='ordinal')

    def test_to_currency(self):
        self.assertEqual(
            'jedan evro, nula centi',
            numinwords(1.0, lang='sr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dva evra, nula centi',
            numinwords(2.0, lang='sr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'pet evra, nula centi',
            numinwords(5.0, lang='sr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dva evra, jedan cent',
            numinwords(2.01, lang='sr', to='currency', currency='EUR')

        )

        self.assertEqual(
            'dva evra, dva centa',
            numinwords(2.02, lang='sr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dva evra, pet centi',
            numinwords(2.05, lang='sr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dve rublje, nula kopejki',
            numinwords(2.0, lang='sr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'dve rublje, jedna kopejka',
            numinwords(2.01, lang='sr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'dve rublje, dve kopejke',
            numinwords(2.02, lang='sr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'dve rublje, pet kopejki',
            numinwords(2.05, lang='sr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'jedan dinar, nula para',
            numinwords(1.0, lang='sr', to='currency', currency='RSD')
        )
        self.assertEqual(
            'dva dinara, dve pare',
            numinwords(2.02, lang='sr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'pet dinara, pet para',
            numinwords(5.05, lang='sr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'jedanaest dinara, jedanaest para',
            numinwords(11.11, lang='sr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'dvadeset jedan dinar, dvadeset jedna para',
            numinwords(21.21, lang='sr', to='currency', currency='RSD')

        )
        self.assertEqual(
            'dvadeset jedan evro, dvadeset jedan cent',
            numinwords(21.21, lang='sr', to='currency', currency='EUR')

        )
        self.assertEqual(
            'dvadeset jedna rublja, dvadeset jedna kopejka',
            numinwords(21.21, lang='sr', to='currency', currency='RUB')

        )
        self.assertEqual(
            'jedna hiljada dvesta trideset četiri evra, '
            'pedeset šest centi',
            numinwords(
                1234.56, lang='sr', to='currency', currency='EUR'
            )
        )
        self.assertEqual(
            'jedna hiljada dvesta trideset četiri rublje, '
            'pedeset šest kopejki',
            numinwords(
                1234.56, lang='sr', to='currency', currency='RUB'
            )
        )
        self.assertEqual(
            'sto jedan evro i jedanaest centi',
            numinwords(
                10111,
                lang='sr',
                to='currency',
                currency='EUR',
                separator=' i'
            )
        )
        self.assertEqual(
            'sto jedna rublja i dvadeset jedna kopejka',
            numinwords(
                10121,
                lang='sr',
                to='currency',
                currency='RUB',
                separator=' i'
            )
        )
        self.assertEqual(
            'sto jedna rublja i dvadeset dve kopejke',
            numinwords(10122, lang='sr', to='currency', currency='RUB',
                       separator=' i')
        )
        self.assertEqual(
            'sto jedan evro i dvadeset jedan cent',
            numinwords(10121, lang='sr', to='currency', currency='EUR',
                       separator=' i'),
        )
        self.assertEqual(
            'minus dvanaest hiljada petsto devetnaest evra, 85 centi',
            numinwords(
                -1251985,
                lang='sr',
                to='currency',
                currency='EUR',
                cents=False
            )
        )
        self.assertEqual(
            "trideset osam evra i 40 centi",
            numinwords('38.4', lang='sr', to='currency', separator=' i',
                       cents=False, currency='EUR'),
        )
