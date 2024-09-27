def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            return file_content

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    except IOError as e:
        print(f"Error: Unable to read the file '{file_path}'. Reason: {str(e)}")
        return None


def wrap_with_dimensions(html_str, width=None, height=None):
    """
    Wraps the given HTML string in a div with optional width and height constraints.

    This function takes an HTML string and optionally wraps it in a div element with
    CSS style attributes to limit its width and/or height. If neither width nor height
    is provided, the original HTML string is returned without modification.

    Parameters:
    - html_str (str): The HTML content to be wrapped.
    - width (int, optional): The maximum width (in pixels) of the div. Defaults to None.
    - height (int, optional): The maximum height (in pixels) of the div. Defaults to None.

    Returns:
    - str: The original HTML string wrapped in a div with the specified dimensions, or
      the original HTML string if no dimensions are provided.

    Example:
    >>> wrap_html_with_dimensions('<p>Hello, world!</p>', width=100)
    '<div style="max-width: 100px; "><p>Hello, world!</p></div>'
    """
    if width is None and height is None:
        return html_str
    
    style = ""
    if width is not None:
        style += f"max-width: {width}px; "
    if height is not None:
        style += f"max-height: {height}px; "

    wrapped_html = f'<div style="{style}">{html_str}</div>'
    return wrapped_html

def write_file(file_path,content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully wrote content to '{file_path}'.")
    except IOError as e:
        print(f"Error: Unable to write to the file '{file_path}'. Reason: {str(e)}")
