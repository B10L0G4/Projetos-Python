>TODO - Step 1 - Escolher uma palavra aleatoria de uma lista e atribuir a palavra para a variavél - chosem_word ok

>TODO - Step 2 - pedir ao usuario para escolher uma letra e atribuir a resposta a variavel guess , lowercase

>TODO - Step 3 - vericar se a letra escolhida esta contida na letra escolhida (guess) é uma das letras na palavra contida em chosen_word

>TODO - Step 4 - Crear uma lista vazia chamada display.( para cada letra na variavel chosen_words deve ser add "_"
    >> # ao display)(se a palavra tiver 5 letras o display devera ter 5 espaços no display - ok

>TODO - Step 5 - Loop through each position in the chosen_word;
>>If the letter at that position matches 'guess' then reveal that letter in the display at that position.
>>e.g. If the user guessed "p" and the chosen word was "apple", then display should be `["_", "p", "p", "_", "_"]`. ok

>TODO - Step 6 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
>>Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3. ok

>TODO - step 7 -  Create a variable called 'lives' to keep track of the number of lives left.
>>Set 'lives' to equal 6.

>TODO - step 8: - If guess is not a letter in the chosen_word,
>>Then reduce 'lives' by 1.
>>#If lives goes down to 0 then the game should stop and it should print "You lose."