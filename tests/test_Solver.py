from tame_of_thrones.Solver import Solver
import collections
import unittest


class TestSolver(unittest.TestCase):
    def setUp(self):
        """
        setUp --> Creates a solver instance for every test,
        the dict is of the format {"Kingdom": ["emblem", "encoded emblem"]}
        """
        self.solver = Solver()
        self.test_dict = {
            "AIR": ["OWL", "RZO"],
            "FIRE": ["DRAGON", "JXGMUT"],
            "ICE": ["MAMMOTH", "THTTVAO"],
            "LAND": ["PANDA", "UFSIF"],
            "SPACE": ["GORILLA", "NVYPSSH"],
            "WATER": ["OCTOPUS", "VJAVWBZ"],
        }

    def test_if_accepted_add_to_forged_pact_list(self):
        self.assertEqual(self.solver.kingdoms_pact_forged_with, [])
        kingdom_list = ["AIR", "LAND", "ICE"]
        encoded_string_list = ["ROZO", "FAIJWJSOOFAMAU", "STHSTSTVSASOS"]
        for kingdom, encoded_string in zip(
            kingdom_list, encoded_string_list
        ):
            self.solver.if_accepted_add_to_forged_pact_list(
                kingdom,
                encoded_string,
                collections.Counter(self.test_dict[kingdom][1]),
            )
        self.assertEqual(
            self.solver.kingdoms_pact_forged_with, ["AIR", "LAND", "ICE"],
        )

    def test_if_accepted_add_to_forged_pact_list_is_not_possible(self):
        self.assertEqual(self.solver.kingdoms_pact_forged_with, [])
        kingdom_list = ["AIR", "WATER"]
        encoded_string_list = [
            "OWLAOWLBOWLC",
            "SUMMER IS COMING",
        ]
        for kingdom, encoded_string in zip(
            kingdom_list, encoded_string_list
        ):
            self.solver.if_accepted_add_to_forged_pact_list(
                kingdom,
                encoded_string,
                collections.Counter(self.test_dict[kingdom][1]),
            )
        self.assertEqual(
            self.solver.kingdoms_pact_forged_with, [],
        )

    def test_input_contents_are_repeated(self):
        self.assertEqual(self.solver.kingdoms_pact_forged_with, [])
        kingdom_list = ["AIR", "AIR", "AIR"]
        encoded_string_list = [
            "ROZO",
            "ROZO",
            "ROZO",
        ]
        for kingdom, encoded_string in zip(
            kingdom_list, encoded_string_list
        ):
            self.solver.if_accepted_add_to_forged_pact_list(
                kingdom,
                encoded_string,
                collections.Counter(self.test_dict[kingdom][1]),
            )
        self.assertEqual(
            self.solver.kingdoms_pact_forged_with, ["AIR"],
        )
