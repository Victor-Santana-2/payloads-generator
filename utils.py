import json

def save_to_file(payloads, filename):
    if filename.endswith(".txt"):
        with open(filename, "w") as f:
            for payload in payloads:
                f.write(f"{payload}\n")
    elif filename.endswith(".json"):
        with open(filename, "w") as f:
            json.dump(payloads, f, indent=4)
    else:
        print("[!] Formato não suportado. Use .txt ou .json")