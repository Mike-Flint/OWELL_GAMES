class TwoLetterConverter:
    regex = '[a-zA-Z]{2}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value