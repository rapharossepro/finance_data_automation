#!/bin/bash

# Cria estrutura de pastas se não existir
mkdir -p data
mkdir -p reports

# Cria arquivos .gitkeep para garantir versionamento das pastas
touch data/.gitkeep
touch reports/.gitkeep

echo "Estrutura criada com sucesso!"
