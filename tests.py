import argparse
import nmw
import hirschberg


def print_matrix(mat):
    # Loop over all rows
    for k in range(0, len(mat)):
        print("[", end="")
        # Loop over each column in row i
        for t in range(0, len(mat[k])):
            # Print out the value in row i, column j
            print(mat[k][t], end="")
            # Only add a tab if we're not in the last column
            if t != len(mat[k]) - 1:
                print("\t", end="")
        print("]\n")


parser = argparse.ArgumentParser()
parser.add_argument("-t", action="store_true", help="Print i & j iterations")
parser.add_argument("-f", action="store_true", help="The input is a file")
parser.add_argument("-l", action="store_true", help="The file input sequences are lines & not characters")
parser.add_argument("gap", type=int, help="Parameter gap penalty \"g\" for the construction of F")
parser.add_argument("match", type=int, help="Parameter match is m for the construction of F")
parser.add_argument("diff", type=int, help="Parameter diff is d for the construction of F")
parser.add_argument("A", help="The 1st sequence or file")
parser.add_argument("B", help="The 2nd sequence or file")
args = parser.parse_args()
g = args.gap
m = args.match
d = args.diff
align_nmw = nmw.nmw(g, m, d)
if args.f:
    with open(args.A, 'r') as A, open(args.B, 'r') as B:
        if args.l:
            a = A.read().splitlines()
            b = B.read().splitlines()
            f = align_nmw.F(a, b)
            w = []
            z = []
            ww, zz = align_nmw.EnumerateAlignments_lines(a, b, f, w, z)
            for w, z in zip(ww, zz):
                for i, j in zip(w, z):
                    if i == j:
                        print("=", i, "\n=", j)
                    else:
                        print("<", i, "\n>", j)
        else:
            a = A.read().splitlines()
            b = B.read().splitlines()
            a = ''.join(a)
            b = ''.join(b)
            f = align_nmw.F(a, b)
            w = ""
            z = ""
            ww, zz = align_nmw.EnumerateAlignments(a, b, f, w, z)
            for w, z in zip(ww, zz):
                print(w)
                print(z)
else:
    a = args.A
    b = args.B
    f = align_nmw.F(a, b)
    w = ""
    z = ""
    #ww, zz = align_nmw.EnumerateAlignments(a, b, f, w, z)
    #for w, z in zip(ww, zz):
    #    print(w)
    #    print(z)

    align_hb = hirschberg.hb(g, m, d)
    ww, zz = align_hb.Hirschberg(a, b)
    print(ww, zz)
    for w, z in zip(ww, zz):
        print(w)
        print(z)
