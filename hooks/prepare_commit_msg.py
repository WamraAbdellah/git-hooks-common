#!/usr/bin/env python3
import sys
import subprocess
import re
import shutil

def main():
    if len(sys.argv) < 2:
        print("ERREUR : Aucun fichier de message de commit fourni.", file=sys.stderr)
        sys.exit(1)

    commit_msg_file = sys.argv[1]
    commit_type = sys.argv[2] if len(sys.argv) > 2 else None

    # Ne rien faire si merge ou squash
    if commit_type in ("merge", "squash"):
        sys.exit(0)

    # Récupérer le nom de la branche
    try:
        branch_name = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            text=True
        ).strip()
    except subprocess.CalledProcessError as e:
        print(f"ERREUR : impossible de récupérer la branche git: {e}", file=sys.stderr)
        sys.exit(1)

    # Extraire ticket (ex: SOD-1234)
    match = re.search(r"[A-Z]{2,}-[0-9]+", branch_name)
    if not match:
        sys.exit(0)

    ticket_id = match.group(0)

    # Lire le contenu actuel du message de commit
    try:
        with open(commit_msg_file, "r", encoding="utf-8") as f:
            content = f.readlines()
    except Exception as e:
        print(f"ERREUR : impossible de lire le fichier de commit : {e}", file=sys.stderr)
        sys.exit(1)

    # Préfixer le ticket seulement si pas déjà présent
    if content and not content[0].startswith(ticket_id + ":"):
        # Sauvegarder une copie du fichier original
        shutil.copy2(commit_msg_file, commit_msg_file + ".bak")

        # Préfixer le message
        content[0] = f"{ticket_id}: {content[0]}"

        try:
            with open(commit_msg_file, "w", encoding="utf-8") as f:
                f.writelines(content)
        except Exception as e:
            print(f"ERREUR : impossible d’écrire dans le fichier de commit : {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
