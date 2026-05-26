import time

def function1(txt, pat, m, n):
    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

# Open files
f = open("input1.txt", "r")
f2 = open("pattern.txt", "r")

# Read content
txt = f.read().strip()
pat = f2.read().strip()

# Close files
f.close()
f2.close()

# Start time
stime = time.time()

time.sleep(1)

# Function call
print(function1(txt, pat, len(txt), len(pat)))

# End time
etime = time.time()

# Print lengths
print("Length of Text:", len(txt))
print("Length of Pattern:", len(pat))

# Execution time
print("Execution Time:", etime - stime - 1)