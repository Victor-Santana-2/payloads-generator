class SSTIPayloads:
    def generate(self):
        return {
            "Jinja2": "{{ 7*7 }}",
            "Twig": "{{ 7*7 }}",
            "Smarty": "{7*7}",
            "ERB (Ruby)": "<%= 7*7 %>"
        }