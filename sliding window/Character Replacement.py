'''''''''''''''''''''''
Longest Repeating Character Replacement
We use:
s = "AABABBA"
k = 1
'''''
s = "AABABBA"
k = 1

left = 0
count = {}
max_frequency = 0
maximum = 0

for right in range(len(s)):

    # Add the new character
    count[s[right]] = count.get(s[right], 0) + 1

    # Update the highest frequency
    max_frequency = max(
        max_frequency,
        count[s[right]]
    )

    # Shrink if too many replacements are needed
    while (right - left + 1) - max_frequency > k:

        count[s[left]] -= 1
        left += 1

    # Window is valid
    maximum = max(
        maximum,
        right - left + 1
    )

print(maximum)