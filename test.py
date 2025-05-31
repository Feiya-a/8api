import unittest
from bwt import bwt_transform, inverse_bwt, prerpocess_bwt, bw_matching

class TestBWT(unittest.TestCase):

  def test_bwt_transform(self):
    self.assertEqual(bwt_transform(AAAA$), "AAAA$")
    self.assertEqual(bwt_transform("AGGTCAACC$"), "CCA$CTAAGG")

def test_inverse_bwt(self):
  self.assertEQual(inverse_bwt("AC$A"),"ACA$")
  self.assertEQual(inverse_bwt("CCA$CTAAGG"),"AGGTCAACC$")

def test_btw_and_inverse(self):
  original = "ACGTACGTACGT$"
  encoded = bwt_transform(original)
  decoded = inverse_bwt(encoded)
  self.asserEqual(decoded,original)

def test_bw_matching(self):
  text = "AGCCACA$"
  bwt = bwt_transform(text)
  first_occurrence, count = preprocess_bwt(bwt)
  self.assertEqual(bw_matching(bwt, "CA", first_occurrence, count), 2)

text = "AAGGGCGTCGGTGC$"
bwt = bwt_transform(text)
first_occurrence, count = preprocess_bwt(bwt)
self.assertEqual(bw_matching(bwt, "GG", first_occurrence, count), 3)

def test_edge_cases(self):
  self.assertEqual(bwt_transform("$"), "$")
  self.assertEqual(inverse_bwt("$"), "$")

self.assertEqual(bwt_transform("CCCCCC$"), "CCCCCC$")
self.assertEqual(inverse_bwt("CCCCCC$", "CCCCCC$")

self.assertEqual(bwt_transform("ACGT$"), "T$ACG")
self.assertEqual(inverse_bwt("T$ACG"), "ACGT$")

with self.assertRaises(ValueError):
  bwt_transform("ACGT")

text = "A" * 999 + "$"
self.assertEqual(inverse_bwt_transform(text)), text)



if __name__ == '__main__':
  unittest.main()
  
