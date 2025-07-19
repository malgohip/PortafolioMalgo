def decode_variable_length_bytes(byte_sequence):
    total_duration = 0
    current_value = 0
    for byte in byte_sequence:
        if byte == 0:
            break
        current_value = (current_value << 7) | (byte & 0x7F)
        if (byte & 0x80) == 0:  # MSB is 0, end of the current value
            total_duration += current_value
            current_value = 0
    return total_duration

# Example input
input_data = "147 52 178 231 178 94 158 169 82 149 192 3 195 129 57 167 166 157 114 182 36 238 160 189 178 33 163 211 203 141 53 215 149 180 26 53 64 0"

# Convert input data to a list of integers
byte_sequence = list(map(int, input_data.split()))

# Calculate the total duration
total_duration = decode_variable_length_bytes(byte_sequence)

# Output the result
print(total_duration)