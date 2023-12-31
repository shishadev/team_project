def find_first_index(text_list, text_to_find) -> int | None:
    """Finds first index of an entry that contains required text"""

    return next(
        (index for index, text in enumerate(text_list) if text is not None and text_to_find in str(text)),
        None
    )
