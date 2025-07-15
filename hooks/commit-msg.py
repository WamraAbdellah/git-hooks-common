#!/usr/bin/env python3
import re
import sys

ticket_commit_regex = r"^[A-Z]{2,}-[0-9]+: .+$"

def main():
    if len(sys.argv) < 2:
        print("ERREUR : Aucun fichier de message de commit fourni.", file=sys.stderr)
        sys.exit(1)

    commit_msg_file = sys.argv[1]
    try:
        with open(commit_msg_file, "r", encoding="utf-8") as f:
            commit_message = f.read().strip()
    except Exception as e:
        print(f"ERREUR : Impossible de lire le fichier {commit_msg_file}: {e}", file=sys.stderr)
        sys.exit(1)

    if re.match(ticket_commit_regex, commit_message):
        print("Format du commit valide (Ticket ID trouvé).")
        sys.exit(0)
    else:
        RED = "\033[31m"
        GREEN = "\033[32m"
        RESET = "\033[0m"
        print(f"{RED}ERREUR : Le format de votre message de commit est invalide.{RESET}", file=sys.stderr)
        print("Il doit obligatoirement commencer par un ID de ticket suivi de ':', d'un espace, puis de votre message.", file=sys.stderr)
        print("")
        print(f"{GREEN}Exemple valide : SOD-1010: Ajout de la fonctionnalité de connexion{RESET}", file=sys.stderr)
        print("")
        sys.exit(1)

if __name__ == "__main__":
    main()
