"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    >>> serial
    <SerialGenerator start=100 next=101>
    """

    initial_val = 0

    def __init__(self, start=0):
        """Constructor

        Args:
            start (int): initial start value for the serial sequence
        """
        self.start = start
        # Stash away the start value for resetting
        self.initial_val = start

    def __repr__(self):
        return_val = '<SerialGenerator start=' + \
            str(self.initial_val) + ' next=' + str(self.start) + '>'
        return return_val

    def generate(self):
        """Return existing value then increments by 1.

        Returns:
            int : exising value"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """Resets existing value to original start value"""
        self.start = self.initial_val


if __name__ == '__main__':
    # Test harness copied from https://docs.python.org/3/library/doctest.html
    import doctest
    import sys
    flags = doctest.REPORT_NDIFF | doctest.FAIL_FAST
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name in globals():
            obj = globals()[name]
        else:
            obj = __test__[name]
        doctest.run_docstring_examples(obj, globals(), name=name,
                                       optionflags=flags)
    else:
        fail, total = doctest.testmod(optionflags=flags)
        print("{} failures out of {} tests".format(fail, total))
