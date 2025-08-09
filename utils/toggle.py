def toggle(content, off_state, on_state):
    modified_content = None

    if on_state in content:
        modified_content = content.replace(on_state, off_state)
    elif off_state in content:
        modified_content = content.replace(off_state, on_state)

    return modified_content
