def get_marker_index(signal: str, marker_length):
    for i in range(len(signal) - marker_length):
        word = signal[i:i + marker_length]
        if len(set(word)) == marker_length:
            return i + marker_length
    return None


def get_start_of_packet_index(signal):
    return get_marker_index(signal, 4)


def get_start_of_message_index(signal):
    return get_marker_index(signal, 14)