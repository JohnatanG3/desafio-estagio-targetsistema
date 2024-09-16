# Desafio Target Sistemas

## 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

## Código do problema com a solução.

## 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

## IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

## Código do problema com a solução.

## 3) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

## Ao final do processamento, qual será o valor da variável SOMA?

## Resposta da questão 3 = 77

## 4) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, 9

b) 2, 4, 8, 16, 32, 64, 128

c) 0, 1, 4, 9, 16, 25, 36, 49

d) 4, 16, 36, 64, 100

e) 1, 1, 2, 3, 5, 8,13

f) 2,10, 12, 16, 17, 18, 19, 20

## 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

### Estratégia para identificar os interruptores:
### a) Preparação inicial
- Ligue o primeiro interruptor e espere alguns minutos. Esse tempo é suficiente para que a lâmpada controlada por esse interruptor aqueça. Após esse tempo, desligue o primeiro interruptor e ligue o segundo interruptor.

### b) Primeira ida à sala das lâmpadas
- Ao chegar à sala das lâmpadas, você observará três possíveis situações:

- A lâmpada acesa estará conectada ao segundo interruptor, que foi o último a ser ligado.
- A lâmpada apagada e quente será a que estava conectada ao primeiro interruptor, que foi ligado inicialmente e depois desligado.
- A lâmpada apagada e fria será a que está conectada ao terceiro interruptor, que não foi ligado em nenhum momento.

## Desse modo, com essa sequência de ações, é possível identificar com clareza qual interruptor controla cada lâmpada utilizando apenas duas idas à sala.