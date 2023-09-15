invalid_filename_chars = '<>:"/\\|?*\n\r\t'
invalid_filename_prefix = ' '
invalid_filename_postfix = ' .'
max_filename_part_length = 128

def sanitize_filename_part(text, replace_spaces=True):
    if text is None:
        return None

    if replace_spaces:
        text = text.replace(' ', '_')

    text = text.translate({ord(x): '_' for x in invalid_filename_chars})
    text = text.lstrip(invalid_filename_prefix)[:max_filename_part_length]
    text = text.rstrip(invalid_filename_postfix)
    return text
