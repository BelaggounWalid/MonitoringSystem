#!/bin/bash
# Afficher tous les utilisateurs connectés
who | cut -f1 -d' ' | sort | uniq


