# -*- coding: utf-8 -*-
"""Facit till kontrollfrågorna i kapitel 2 Materia och partiklar. Samma källa som häftet (KQ i ch02k)."""
import sys; sys.path.insert(0, '/tmp/kem')
import ch02k
KOLLA2 = {q: a for qs in ch02k.KQ.values() for q, a in qs}
