class Printing:
    def __init__(self, n_cols=1, col_len=3):
        self.n_cols = n_cols
        self.col_len = col_len

    def _print_border_line(self):
        """This function prints line of the next format: +--...--+--...--+--...--+"""
        list_print = ["-" * self.col_len] * self.n_cols
        str_print = "+" + "+".join(list_print) + "+"
        print(str_print)

    def _print_messages_line(self, messages_line):
        """This function prints line of the next format: + message_1 + message_2 + message_3 + ... + message_n +"""
        list_print = []
        for message in messages_line:
            left_symbols = self.col_len - 1 - len(message)
            list_print.append(" " + message + " " * left_symbols)

        str_print = "|" + "|".join(list_print) + "|"
        print(str_print)

    def print_messages_lines(self, messages):
        """
        This function prints lines of the next format:
        + message_11 + message_12 + message_13 + ... + message_1n +
        + message_21 + message_22 + message_23 + ... + message_2n +
        ...
        + message_m1 + message_m2 + message_m3 + ... + message_mn +
        """
        self._print_border_line()
        for messages_line in messages:
            self._print_messages_line(messages_line)
            self._print_border_line()