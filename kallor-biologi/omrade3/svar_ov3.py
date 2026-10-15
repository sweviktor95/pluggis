# -*- coding: utf-8 -*-
"""Facit till kontrollfrågorna i kapitel 3 (Biologisk mångfald). Samma källa som häftet (KQ i ch03n)."""
import sys; sys.path.insert(0, '/tmp/bio')
import ch03n
KOLLA2 = {q: a for qs in ch03n.KQ.values() for q, a in qs}
