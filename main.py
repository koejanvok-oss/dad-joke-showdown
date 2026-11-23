"""Dad Joke Showdown entry: "The Upbeat Toaster".

The setup has Dad asking the toaster why it is always so upbeat.
The punchline turns on "rise to the occasion": bread rises in a
toaster, and a cheerful person rises to meet a challenge. The word
"upbeat" quietly sets up the toast popping up, so the pun lands on
the first read and the joke reads naturally aloud.
"""

import os

LINE = (
    "Dad asked the toaster why it's always so upbeat. "
    "It said, 'I rise to the occasion.'"
)

assert 1 <= len(LINE) <= 200, "joke must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
