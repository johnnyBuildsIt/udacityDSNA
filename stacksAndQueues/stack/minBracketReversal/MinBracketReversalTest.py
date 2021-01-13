import unittest
from MinBracketReversal import MinBracketReversal


class MinBracketReversalTest(unittest.TestCase):

    def test1(self):
        brackets = "}}}}"

        reversals = MinBracketReversal.minimum_bracket_reversals(brackets)

        self.assertEqual(reversals, 2)

    def test2(self):
        brackets = "}}{{"

        reversals = MinBracketReversal.minimum_bracket_reversals(brackets)

        self.assertEqual(reversals, 2)

    def test3(self):
        brackets = "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}"

        reversals = MinBracketReversal.minimum_bracket_reversals(brackets)

        self.assertEqual(reversals, 13)

    def test4(self):
        brackets = "}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{"

        reversals = MinBracketReversal.minimum_bracket_reversals(brackets)

        self.assertEqual(reversals, 2)

    def test5(self):
        brackets = "}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"

        reversals = MinBracketReversal.minimum_bracket_reversals(brackets)

        self.assertEqual(reversals, 1)

    def testNotBalancedInput(self):
        brackets = "{{{"

        reversals = MinBracketReversal.minimum_bracket_reversals(brackets)

        self.assertEqual(reversals, -1)
