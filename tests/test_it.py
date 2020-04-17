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


class numinwordsITTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = numinwords(+number, lang="it")
        neg_crd = numinwords(-number, lang="it")
        pos_ord = numinwords(+number, lang="it", ordinal=True)
        neg_ord = numinwords(-number, lang="it", ordinal=True)
        self.assertEqual("meno " + pos_crd, neg_crd)
        self.assertEqual("meno " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            numinwords(3.1415, lang="it"), "tre virgola uno quattro uno cinque"
        )
        self.assertEqual(
            numinwords(-5.15, lang="it"), "meno cinque virgola uno cinque"
        )
        self.assertEqual(
            numinwords(-0.15, lang="it"), "meno zero virgola uno cinque"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            numinwords(3.1415, lang="it", ordinal=True),
            "terzo virgola uno quattro uno cinque"
        )
        self.assertEqual(
            numinwords(-5.15, lang="it", ordinal=True),
            "meno quinto virgola uno cinque"
        )
        self.assertEqual(
            numinwords(-0.15, lang="it", ordinal=True),
            "meno zero virgola uno cinque"
        )

    def test_0(self):
        self.assertEqual(numinwords(0, lang="it"), "zero")
        self.assertEqual(numinwords(0, lang="it", ordinal=True), "zero")

    def test_1_to_10(self):
        self.assertEqual(numinwords(1, lang="it"), "uno")
        self.assertEqual(numinwords(2, lang="it"), "due")
        self.assertEqual(numinwords(7, lang="it"), "sette")
        self.assertEqual(numinwords(10, lang="it"), "dieci")

    def test_11_to_19(self):
        self.assertEqual(numinwords(11, lang="it"), "undici")
        self.assertEqual(numinwords(13, lang="it"), "tredici")
        self.assertEqual(numinwords(15, lang="it"), "quindici")
        self.assertEqual(numinwords(16, lang="it"), "sedici")
        self.assertEqual(numinwords(19, lang="it"), "diciannove")

    def test_20_to_99(self):
        self.assertEqual(numinwords(20, lang="it"), "venti")
        self.assertEqual(numinwords(21, lang="it"), "ventuno")
        self.assertEqual(numinwords(23, lang="it"), "ventitré")
        self.assertEqual(numinwords(28, lang="it"), "ventotto")
        self.assertEqual(numinwords(31, lang="it"), "trentuno")
        self.assertEqual(numinwords(40, lang="it"), "quaranta")
        self.assertEqual(numinwords(66, lang="it"), "sessantasei")
        self.assertEqual(numinwords(92, lang="it"), "novantadue")

    def test_100_to_999(self):
        self.assertEqual(numinwords(100, lang="it"), "cento")
        self.assertEqual(numinwords(111, lang="it"), "centoundici")
        self.assertEqual(numinwords(150, lang="it"), "centocinquanta")
        self.assertEqual(numinwords(196, lang="it"), "centonovantasei")
        self.assertEqual(numinwords(200, lang="it"), "duecento")
        self.assertEqual(numinwords(210, lang="it"), "duecentodieci")
        self.assertEqual(numinwords(701, lang="it"), "settecentouno")

    def test_1000_to_9999(self):
        self.assertEqual(numinwords(1000, lang="it"), "mille")
        self.assertEqual(numinwords(1001, lang="it"), "milleuno")
        self.assertEqual(numinwords(1500, lang="it"), "millecinquecento")
        self.assertEqual(
            numinwords(7378, lang="it"), "settemilatrecentosettantotto"
        )
        self.assertEqual(numinwords(2000, lang="it"), "duemila")
        self.assertEqual(numinwords(2100, lang="it"), "duemilacento")
        self.assertEqual(
            numinwords(6870, lang="it"), "seimilaottocentosettanta"
        )
        self.assertEqual(numinwords(10000, lang="it"), "diecimila")
        self.assertEqual(
            numinwords(98765, lang="it"),
            "novantottomilasettecentosessantacinque"
        )
        self.assertEqual(numinwords(100000, lang="it"), "centomila")
        self.assertEqual(
            numinwords(523456, lang="it"),
            "cinquecentoventitremilaquattrocentocinquantasei"
        )

    def test_big(self):
        self.assertEqual(numinwords(1000000, lang="it"), "un milione")
        self.assertEqual(numinwords(1000007, lang="it"), "un milione e sette")
        self.assertEqual(
            numinwords(1200000, lang="it"), "un milione e duecentomila"
        )
        self.assertEqual(numinwords(3000000, lang="it"), "tre milioni")
        self.assertEqual(numinwords(3000005, lang="it"),
                         "tre milioni e cinque")
        self.assertEqual(
            numinwords(3800000, lang="it"), "tre milioni e ottocentomila"
        )
        self.assertEqual(numinwords(1000000000, lang="it"), "un miliardo")
        self.assertEqual(
            numinwords(1000000017, lang="it"), "un miliardo e diciassette"
        )
        self.assertEqual(numinwords(2000000000, lang="it"), "due miliardi")
        self.assertEqual(
            numinwords(2000001000, lang="it"), "due miliardi e mille"
        )
        self.assertEqual(
            numinwords(1234567890, lang="it"),
            "un miliardo, duecentotrentaquattro milioni e "
            "cinquecentosessantasettemilaottocentonovanta"
        )
        self.assertEqual(numinwords(1000000000000, lang="it"), "un bilione")
        self.assertEqual(
            numinwords(123456789012345678901234567890, lang="it"),
            "centoventitré quadriliardi, quattrocentocinquantasei "
            "quadrilioni, settecentottantanove triliardi, dodici trilioni, "
            "trecentoquarantacinque biliardi, seicentosettantotto bilioni, "
            "novecentouno miliardi, duecentotrentaquattro milioni e "
            "cinquecentosessantasettemilaottocentonovanta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(numinwords(1, lang="it", ordinal=True), "primo")
        self.assertEqual(numinwords(8, lang="it", ordinal=True), "ottavo")
        self.assertEqual(
            numinwords(21, lang="it", ordinal=True), "ventunesimo"
        )
        self.assertEqual(
            numinwords(23, lang="it", ordinal=True), "ventitreesimo"
        )
        self.assertEqual(
            numinwords(47, lang="it", ordinal=True), "quarantasettesimo"
        )
        self.assertEqual(
            numinwords(99, lang="it", ordinal=True), "novantanovesimo"
        )

    def test_nth_100_to_999(self):
        self.assertEqual(numinwords(100, lang="it", ordinal=True), "centesimo")
        self.assertEqual(
            numinwords(112, lang="it", ordinal=True), "centododicesimo"
        )
        self.assertEqual(
            numinwords(120, lang="it", ordinal=True), "centoventesimo"
        )
        self.assertEqual(
            numinwords(121, lang="it", ordinal=True), "centoventunesimo"
        )
        self.assertEqual(
            numinwords(316, lang="it", ordinal=True), "trecentosedicesimo"
        )
        self.assertEqual(
            numinwords(700, lang="it", ordinal=True), "settecentesimo"
        )
        self.assertEqual(
            numinwords(803, lang="it", ordinal=True), "ottocentotreesimo"
        )
        self.assertEqual(
            numinwords(923, lang="it", ordinal=True), "novecentoventitreesimo"
        )

    def test_nth_1000_to_999999(self):
        self.assertEqual(numinwords(
            1000, lang="it", ordinal=True), "millesimo")
        self.assertEqual(
            numinwords(1001, lang="it", ordinal=True), "milleunesimo"
        )
        self.assertEqual(
            numinwords(1003, lang="it", ordinal=True), "milletreesimo"
        )
        self.assertEqual(
            numinwords(1200, lang="it", ordinal=True), "milleduecentesimo"
        )
        self.assertEqual(
            numinwords(8640, lang="it", ordinal=True),
            "ottomilaseicentoquarantesimo"
        )
        self.assertEqual(
            numinwords(14000, lang="it", ordinal=True), "quattordicimillesimo"
        )
        self.assertEqual(
            numinwords(123456, lang="it", ordinal=True),
            "centoventitremilaquattrocentocinquantaseiesimo"
        )
        self.assertEqual(
            numinwords(987654, lang="it", ordinal=True),
            "novecentottantasettemilaseicentocinquantaquattresimo"
        )

    def test_nth_big(self):
        self.assertEqual(
            numinwords(1000000001, lang="it", ordinal=True),
            "un miliardo e unesimo"
        )
        self.assertEqual(
            numinwords(123456789012345678901234567890, lang="it",
                       ordinal=True),
            "centoventitré quadriliardi, quattrocentocinquantasei "
            "quadrilioni, settecentottantanove triliardi, dodici trilioni, "
            "trecentoquarantacinque biliardi, seicentosettantotto bilioni, "
            "novecentouno miliardi, duecentotrentaquattro milioni e "
            "cinquecentosessantasettemilaottocentonovantesimo"
        )

    def test_with_decimals(self):
        self.assertAlmostEqual(
            numinwords(1.0, lang="it"), "uno virgola zero"
        )
        self.assertAlmostEqual(
            numinwords(1.1, lang="it"), "uno virgola uno"
        )
