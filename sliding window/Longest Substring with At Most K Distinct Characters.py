''''''''''''''''''''''
s = "eceba"
k = 2
Find the length of the longest substring containing at most 2 distinct characters.
'''''''''''''''

s = "eceba"
k = 2

left = 0
count = {}
maximum = 0

for right in range(len(s)):

    # Expand the window
    count[s[right]] = count.get(s[right], 0) + 1

    # Shrink if invalid
    while len(count) > k:

        count[s[left]] -= 1

        if count[s[left]] == 0:
            del count[s[left]]

        left += 1

    # Window is valid, update answer
    maximum = max(maximum, right - left + 1)

print(maximum)