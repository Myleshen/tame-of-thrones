from tame_of_thrones.CommandLineParser import CommandLineParser
from tame_of_thrones.Solver import Solver


def main():
    file_contents = CommandLineParser().get_file_contents()
    solver = Solver()

    # Main Logic
    for line in file_contents:
        kingdom, *message = line.split()
        message = (
            "".join(message) if isinstance(message, list) else message
        )
        solver.if_accepted_add_to_forged_pact_list(kingdom, message)

    solver.print_answer()


if __name__ == "__main__":
    main()
