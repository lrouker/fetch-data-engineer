def text_to_list(string_to_parse):
    #Decision here to exclude punctutation.  With modules, I would import re or string and use either regex or string translate to strip out all punctuation
    punctuation_string = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punc_free_string = ""
    for character in string_to_parse:
        if character not in punctuation_string:
            punc_free_string += character
    return punc_free_string.split()