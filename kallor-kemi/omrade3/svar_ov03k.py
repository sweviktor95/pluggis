# -*- coding: utf-8 -*-
"""Facit till kontrollfrågorna i kapitel 2 Atomer och grundämnen. Samma källa som häftet (KQ i ch03k)."""
import sys; sys.path.insert(0, '/tmp/kem')
import ch03k
KOLLA2 = {q: a for qs in ch03k.KQ.values() for q, a in qs}
