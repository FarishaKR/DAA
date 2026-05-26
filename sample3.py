import time

def rabin_karp(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1) % q

    p = 0
    t = 0

    result = []

    # Calculate hash values
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Sliding window
    for s in range(n - m + 1):

        # Hash values match
        if p == t:

            # Check characters one by one
            if text[s:s + m] == pattern:
                result.append(s)

        # Calculate next window hash
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

            if t < 0:
                t += q

    return result


# User Input
text = input("Enter Text: ")
pattern = input("Enter Pattern: ")

# Start Time
stime = time.time()

time.sleep(1)

# Function Call
result = rabin_karp(text, pattern)

# End Time
etime = time.time()

# Output
print("Pattern Found at Index:", result)

print("Length of Text:", len(text))
print("Length of Pattern:", len(pattern))

print("Execution Time:", etime - stime - 1)