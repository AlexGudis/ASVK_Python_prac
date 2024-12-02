import struct
import sys


def read_wav_header():
    try:
        f = sys.stdin.buffer
        riff, size, wave = struct.unpack("<4sI4s", f.read(12))

        if riff != b'RIFF' or wave != b'WAVE':
            return "NO"

        fmt, fmt_size, audio_format = struct.unpack("<4sI2s", f.read(10))

        if fmt != b'fmt ' or fmt_size != 16 or audio_format != b'\x01\x00':
                return "NO"

        channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack(
                "<HHIIH", f.read(14))

        data_chunk = f.read(4)
        while data_chunk != b'data':
            size_chunk = struct.unpack("<I", f.read(4))[0]
            f.seek(size_chunk, 1)
            data_chunk = f.read(4)

        data_size = struct.unpack("<I", f.read(4))[0]

        return f"Size={size}, Type=1, Channels={channels}, Rate={sample_rate}, Bits={bits_per_sample}, Data size={data_size}"

    except Exception as e:
        return "NO"

print(read_wav_header())
