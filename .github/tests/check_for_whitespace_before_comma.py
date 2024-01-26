import sys


def find_bad_lines(file_content):
    bad_lines = []

    for i, line in enumerate(file_content, start=1):
        if " ," in line:
            # Sonderfall mit allen Sonderzeichen ignorieren
            if not line.startswith("test_special_chars"):
                bad_lines.append(i)

    return bad_lines


if __name__ == "__main__":
    file_path = "live/global.ini"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
        bad_lines = find_bad_lines(content)
        if bad_lines:
            print("Folgende Zeilen bitte überprüfen")
            print(bad_lines)
            sys.exit(1)

    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
