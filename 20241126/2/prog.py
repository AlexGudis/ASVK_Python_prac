import sys

def decode_cp1251_to_utf8(data):
    try:
        latin1_decoded = data.encode('latin1', errors='replace')
        result = latin1_decoded.decode('cp1251')
    except UnicodeDecodeError:
        result = latin1_decoded.decode('cp1251', errors='replace')
    return result

input_text = sys.stdin.read()
output_text = decode_cp1251_to_utf8(input_text)
sys.stdout.write(output_text)