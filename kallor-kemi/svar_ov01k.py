# -*- coding: utf-8 -*-
"""Facit till kontrollfrågorna i kapitel 1 Kemi som vetenskap. Samma källa som häftet (KQ i ch01k)."""
import sys; sys.path.insert(0, '/tmp/kem')
import ch01k
KOLLA2 = {q: a for qs in ch01k.KQ.values() for q, a in qs}
