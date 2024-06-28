import cowsay
import sys

from reqAPI import get_response, print_3

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])