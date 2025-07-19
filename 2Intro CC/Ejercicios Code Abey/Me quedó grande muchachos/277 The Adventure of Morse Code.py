#Author: Sebastian Ochoa. Date: 08/20/2024
# -*- coding: utf-8 -*-

"""
"What do you think of this telegram, Watson?" Holmes asked me one morning.

I glanced at the piece of paper he handed me.

--.--.---.......-..-.-.---.-..-......-..-.......-..-..-------.--.....-....-.-.....--..........-.-...-.-.-..-..-..-.--
"Looks like Morse code," I said.

"Your mental alacrity never ceases to amaze me," said Holmes dryly. "I was inquiring, however, after its meaning."

"I was in the medical corps, not in communications," I started, but Holmes interrupted.

"I do not expect you to know Morse code by heart," he said. "I have, however, recently published a monograph on the 831 most common coding systems. Here is the relevant page."

The book he handed to me contained the following table.

a   .-
b   -...
c   -.-.
d   -..
e   .
f   ..-.
g   --.
h   ....
i   ..
j   .---
k   -.-
l   .-..
m   --
n   -.
o   ---
p   .--.
q   --.-
r   .-.
s   ...
t   -
u   ..-
v   ...-
w   .--
x   -..-
y   -.--
z   --..
"Then," I said, "it's a simple matter of decoding."

"I do concur," said Holmes, "that at the first glance the problem appears easy."

"Let's see," I said. "This starts with two dashes. So that's an 'm'."

"Or, possibly," interjected Holmes, "the start of a 'g'. Or of a 'q'. Or a 't', followed by something else."

I stared at the telegram. "Wait," I said, "this has no breaks between the letters."

"If you had spent as much time as I did studying the professional habits of British telegraph operators," said Holmes, "you would know they, as a rule, do not insert breaks between the letters and are well-trained enough to understand the transmission as an uninterrupted stream."

I must have looked entirely lost, because Holmes took pity on me.

"I happen to know," he said, "that this is Moriarty's passcode. He never misses a chance to demonstrate his disdain of me and always uses for his passcodes the contiguous sequences of between ten and thirteen words, inclusively, from your first book. Don't ask how I obtained this knowledge. My memories of having to disguise myself as a telegram girl are too painful yet."

"My first book?" I asked, dazed.

"Yes," said Holmes, "A Study in Scarlet. He uses the text that is lowercased, stripped of all punctuation, and concatenated into a single line. As a matter of fact, here it is, for your convenience: A Study in Scarlet. I obtained this via hacking into Moriarty's calculation engine."

"How does one hack into a calculation engine?" I asked.

Holmes raised an eyebrow at me. "How does one hack into anything?" he said. "With an axe, of course."

I stared at the file.

"But," I started, "to analyze the letters' relative frequencies and all possible breaks in the code would take..."

"As I said," interrupted Holmes, "at the first glance, the problem appears easy. At the second glance, it's elementary, Watson. Here's the encoded text."

may be very clever i said to myself but he is certainly

"How did you determine that?!" I exclaimed.

"This," said Holmes, "is indeed the problem. How did I? Maybe you could use your calculation engine and apply my deductive method to the other telegram, the code of which appears below? Your answer should be between ten and thirteen words, lowercased and separated with spaces, as a single string."

For the input / answer example please kindly use the samples found in the text above.
"""
"""
a = open('Ejercicios Code Abey\Me quedó grande muchachos\TXTs\e277 The Adventure of Morse Code.txt','r')
P= a.readlines()

morse=P[0].strip()

print(morse)
"""
morse='--.--.---.......-..-.-.---.-..-......-..-.......-..-..-------.--.....-....-.-.....--..........-.-...-.-.-..-..-..-.--'

import re

# Morse code to character mapping
morse_dict = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z'
}

def morse_to_char(morse_code):
    """Convert Morse code to characters using the provided Morse code dictionary."""
    return morse_dict.get(morse_code, '')

def decode_morse_message(morse_message):
    """Decode a Morse message to a string of characters."""
    # Split Morse code chunks by double '1's indicating end of character
    morse_chars = morse_message.split('11')
    decoded_message = []
    
    for morse_char in morse_chars:
        # Remove trailing zeros (padding)
        morse_char = morse_char.rstrip('0')
        if morse_char:  # If it's not an empty string
            # Replace Morse code with characters
            decoded_message.append(morse_to_char(morse_char))
    
    return ''.join(decoded_message)

def prepare_reference_text(text):
    """Convert the reference text to a single lowercase string without punctuation."""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # Remove punctuation and non-alphabetic characters
    text = text.replace('\n', ' ')        # Replace newlines with spaces
    return text

def find_matching_text(reference_text, decoded_message):
    """Find the sequence of words in the reference text that matches the decoded message."""
    words = reference_text.split()
    decoded_message = decoded_message.strip()
    
    for i in range(len(words)):
        for j in range(i + 10, min(i + 13, len(words)) + 1):
            candidate = ' '.join(words[i:j])
            if candidate == decoded_message:
                return candidate
    
    return 'No match found'

# Input data
reference_text = """
may be very clever i said to myself but he is certainly
"""
morse_message = "--.--.---.......-..-.-.---.-..-......-..-.......-..-..-------.--.....-....-.-.....--..........-.-...-.-.-..-..-..-.--"

# Process
reference_text = prepare_reference_text(reference_text)
decoded_message = decode_morse_message(morse_message)
matching_text = find_matching_text(reference_text, decoded_message)

print(matching_text)