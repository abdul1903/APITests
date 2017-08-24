from functional_tests.css_selectors import CSS_SELECTORS


def get_css_selector_key(css_selector):
    def key_paths(nested_dict):
        for key, value in nested_dict.iteritems():
            if isinstance(value, dict):
                for sub_key, sub_value in key_paths(value):
                    yield [key] + sub_key, sub_value
            else:
                yield [key], value

    reverse_dict = {}
    for key_, value_ in key_paths(CSS_SELECTORS):
        reverse_dict.setdefault(value_, []).append(key_)

    return ' > '.join(reverse_dict[css_selector][0]) if css_selector in reverse_dict else css_selector


