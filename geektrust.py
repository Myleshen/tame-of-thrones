from tame_of_thrones.CommandLineParser import CommandLineParser
from tame_of_thrones.Kingdom import Kingdom
from tame_of_thrones.EachLine import EachLine
from tame_of_thrones.Solver import Solver


def main():
    kingdom_instance = Kingdom()
    file_contents = CommandLineParser().get_file_contents()
    solver = Solver()
    line_parser = EachLine()

    # Main Logic
    for line in file_contents:
        kingdom, message = line_parser.parse_line(line)
        # If kingdom is already added in the list then,
        # There is no need to send the data into
        # the solver class
        if kingdom not in solver.kingdoms_pact_forged_with:
            solver.if_accepted_add_to_forged_pact_list(
                kingdom, message, kingdom_instance.kingdom_dict[kingdom]
            )

    solver.print_answer()


if __name__ == "__main__":
    main()
