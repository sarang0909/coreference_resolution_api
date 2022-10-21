"""A module to get coreference resolved text"""

import coreferee, spacy

nlp = spacy.load("en_core_web_trf")
nlp.add_pipe("coreferee")


def get_coref_resolution(text):
    """A method to return coreference resolved text

    Args:
        text (str): Input text

    Returns:
        output: resolved_text
    """

    doc = nlp(text)
    # Get token list
    tok_list = list(token.text_with_ws for token in doc)
    for index, _ in enumerate(tok_list):
        # Check resolution of each token
        if doc._.coref_chains.resolve(doc[index]):
            new_token = ""
            # If it is not None,then replcae token with resolved/original entity
            for resolved_token in doc._.coref_chains.resolve(doc[index]):
                new_token = new_token + resolved_token.text + " "
            tok_list[index] = new_token
    resolved_text = "".join(tok_list)
    return resolved_text
