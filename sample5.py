import time

def KMPSearch(pat, txt):

    m = len(pat)
    n = len(txt)

    lps = [0] * m

    print("LPS Array:", lps)

    j = 0

    computeLPSArray(pat, m, lps)

    i = 0

    while i < n:

        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:
            print("Found pattern at index", str(i - j))
            j = lps[j - 1]

        elif i < n and pat[j] != txt[i]:

            if j != 0:
                j = lps[j - 1]

            else:
                i += 1


def computeLPSArray(pat, m, lps):

    length = 0

    lps[0] = 0

    i = 1

    while i < m:

        if pat[i] == pat[length]:

            length += 1
            lps[i] = length
            i += 1

        else:

            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

    print("Final LPS Array:", lps)


txt = input("Enter text: ")
pat = input("Enter pattern: ")

stime = time.time()

time.sleep(1)

KMPSearch(pat, txt)

etime = time.time()

print("Length of Text:", len(txt))
print("Length of Pattern:", len(pat))

print("Execution Time:", etime - stime - 1)