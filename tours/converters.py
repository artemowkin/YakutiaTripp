class DateConverter:
    """Converter for ISO format date"""

    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value: str) -> str:
        return value

    def to_url(self, value: str) -> str:
        return value
