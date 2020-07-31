from tame_of_thrones.CommandLineParser import CommandLineParser
from tame_of_thrones.Message import Message
from tame_of_thrones.Solver import Solver


def main():
    file_contents = CommandLineParser().get_file_contents()
    solver = Solver()

    # Main Logic
    for line in file_contents:
        message = Message(line)
        solver.if_accepted_add_to_forged_pact_list(
            message.kingdom, message.message
        )

    solver.print_answer()


if __name__ == "__main__":
    main()
