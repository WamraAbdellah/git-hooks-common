#!/bin/sh

# $1 = chemin vers le fichier du message de commit
# $2 = type de commit (optional) : message, merge, squash, etc.

# Ne rien faire si le commit est un merge ou squash
if [ "$2" = "merge" ] || [ "$2" = "squash" ]; then
  exit 0
fi

# Récupérer le nom de la branche
branch_name=$(git rev-parse --abbrev-ref HEAD)

# Extraire un éventuel ticket du nom de la branche (ex: SOD-1234)
ticket_id=$(echo "$branch_name" | grep -oE '[A-Z]{2,}-[0-9]+')

# Si un ticket est trouvé, préfixer le message de commit
if [ -n "$ticket_id" ]; then
  sed -i.bak "1s/^/$ticket_id: /" "$1"
fi
