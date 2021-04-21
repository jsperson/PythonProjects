"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """[summary]
    >>> wf = WordFinder("./test.txt"); len(wf.lines) > 0
    4 words read
    True

    >>> wf.random() in wf.lines
    True

    """

    def __init__(self, filename):
        def print_count(self, count):
            print(str(count) + ' words read')

        self.lines = self.parse_file(filename)

        print_count(self, len(self.lines))

    def random(self):
        """Return random value from the list
        """
        return random.choice(self.lines)

    def parse_file(self, filename):
        f = open(filename, 'r')
        lines = [line.strip() for line in f]
        f.close()
        return lines


class SpecialWordFinder(WordFinder):
    """
    >>> swf = SpecialWordFinder("./special.txt")
    4 words read

    >>> swf.random() in swf.lines
    True
    """

    def parse_file(self, filename):
        f = open(filename, 'r')
        lines = [line.strip() for line in f if len(
            line.strip()) > 0 and line[0] != '#']
        f.close()
        return lines


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
