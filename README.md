# Sistema de Recomendação de Filmes - Netflix

Este projeto implementa um sistema de recomendação de filmes utilizando técnicas de **Processamento de Linguagem Natural (NLP)** e **similaridade de cosseno** para medir a semelhança entre filmes com base nas categorias em que estão listados.

## Visão Geral

O sistema recomenda filmes semelhantes com base nas categorias (`listed_in`) presentes no dataset de títulos da Netflix. O processo envolve:

1. **Vetorização de Texto**: Utilizando a técnica **TF-IDF** (Term Frequency-Inverse Document Frequency) para transformar as categorias dos filmes em vetores numéricos.
2. **Cálculo de Similaridade**: Usando a **similaridade de cosseno** para medir a similaridade entre os filmes, com base nas categorias.
3. **Recomendação de Filmes**: Retorna os filmes mais semelhantes ao título informado.

## Tecnologias e Bibliotecas

- **Pandas**: Manipulação de dados.
- **Scikit-learn**: Implementação de algoritmos de aprendizado de máquina, incluindo a vetorização de texto com `TfidfVectorizer` e cálculo de similaridade com `cosine_similarity`.
- **NLP** (Processamento de Linguagem Natural): A técnica de **TF-IDF** utilizada neste projeto é uma abordagem popular de NLP para representar texto de maneira que um modelo de aprendizado de máquina possa entender.

## Arquivo de Entrada

O código espera um arquivo **Excel** chamado `netflix_titles.xlsx` contendo uma tabela com as seguintes colunas:

- **show_id**: ID único do show.
- **type**: Tipo de conteúdo (ex: Filme ou Série).
- **title**: Título do show.
- **director**: Diretor do show.
- **cast**: Atores principais.
- **country**: País de origem.
- **date_added**: Data de adição do título na plataforma.
- **release_year**: Ano de lançamento.
- **rating**: Classificação.
- **duration**: Duração (para filmes).
- **listed_in**: Categorias ou gêneros em que o show está listado.
- **description**: Descrição do show.

A coluna `listed_in` é usada para gerar as recomendações de filmes.

## Como Funciona?

### 1. Processamento de Texto (NLP)
O código utiliza a técnica **TF-IDF (Term Frequency-Inverse Document Frequency)** para transformar as categorias de filmes em representações numéricas. Essa técnica avalia a importância de cada palavra nas categorias em relação ao conjunto completo de dados, atribuindo maior peso às palavras mais relevantes.

### 2. Similaridade de Cosseno
Após a transformação das categorias em vetores numéricos, o código utiliza **similaridade de cosseno** para calcular a similaridade entre os filmes. A similaridade de cosseno mede o grau de similaridade entre dois vetores, sendo ideal para esse tipo de recomendação.

### 3. Recomendação de Filmes
A função `recomendar_filmes(titulo, top_n=5)` recebe o título de um filme e retorna os **top N filmes mais semelhantes** com base nas categorias em que estão listados.

### 3. Saída Esperada
O código retorna um DataFrame com os títulos e categorias dos filmes recomendados:

recomendados = recomendar_filmes("Naruto Shippuden the Movie: Blood Prison", top_n=5)

```bash
Filmes recomendados:
                               title                                           listed_in
0                         Movie 1                                Action, Adventure
1                         Movie 2                                Action, Drama
2                         Movie 3                                Adventure, Fantasy
3                         Movie 4                                Comedy, Action
4                         Movie 5                                Action, Thriller
