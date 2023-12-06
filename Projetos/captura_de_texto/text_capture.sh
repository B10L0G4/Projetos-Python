#!/bin/bash

# Variáveis
pagina_atual=261
arquivo_word="btth3.docx"

# Função para pegar o título da página
function get_titulo() {
    titulo=$(curl -s -L -H "Accept: text/html" "$1" | grep -o '<title>[^<]*</title>')
    echo "$titulo"
}
# Função para pegar o texto da página
function get_texto() {

    texto=$(curl -s -L -H "Accept: text/html" "$1" | grep -o '<p>[^<]*</p>')
    texto=$(curl -s -L -H "Accept: text/html" "$1" | grep -o '<p dir="ltr">[^<]*</p>')
    texto=$(curl -s -L -H "Accept: text/html" "$1" | grep -o '<span style="font-style: inherit; font-weight: inherit;">[^<]*</span>')
    texto=$(curl -s -L -H "Accept: text/html" "$1" | grep -o '<p style="text-align: justify;">[^<]*</p>')
    echo "$texto"
}


# Loop para pegar o título e o texto de cada página
while true; do

  # Pegar o título da página atual
  titulo=$(get_titulo "https://centralnovel.com/battle-through-the-heavens-capitulo-$pagina_atual/") 

  # Se o título for vazio, significa que a página não existe
  if [ -z "$titulo" ]; then
    break
  fi


  # Pegar o texto da página atual
  texto=$(get_texto "https://centralnovel.com/battle-through-the-heavens-capitulo-$pagina_atual/") 


  # Adicionar o título e o texto à página do Word
  echo -e "$titulo\n\n" >> $arquivo_word |sed -i -e 's/\| Central Novel//g' -e 's/<[^>]*>//g' $arquivo_word 
  echo -e "$texto\n\n" >> $arquivo_word |sed -i -e 's/<[^>]*>//g' -e 's/\&#8230;/.../g' -e 's/\&#8216;/\x27/g' -e 's/\&#8217;/\x27/g' -e 's/\&#8220;/"/g' -e 's/\&#8221;/"/g' -e 's/\&#8211;/-/g'  $arquivo_word 


  # Incrementar o número da página
  pagina_atual=$(($pagina_atual + 1))
#   sleep 1
#   break #apenas para tags diferentes 

done
