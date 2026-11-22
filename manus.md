# Group 6 — Text Mining Results

Team: Haru, Marcus, and Sashe.

Speaking script for the presentation; target length is about four minutes.

## Slide 1 — Group 6: From movie reviews to data

Hi, we are Group 6: Haru, Marcus, and Sashe. We used spaCy to tokenize the first 20 IMDB reviews and label their parts of speech.

## Slide 2 — 01 · The sample: What went in?

The full dataset has 50,000 reviews. We used the first 20: ten are labelled positive and ten are labelled negative.

## Slide 3 — 02 · Loading the dataset: Getting the reviews

We downloaded the dataset with KaggleHub and CSV file. Then pandas loaded it into a table called `imdb`, so we could inspect the shape and the first few rows.

## Slide 4 — 03 · Tokenization: A review becomes pieces

Tokenization splits text into smaller parts. For example, “One of the other reviewers” becomes five separate tokens, and punctuation is also counted.

## Slide 5 — 04 · Processing the reviews: How spaCy produces the results

We selected the first 20 reviews and used spaCy's `nlp.pipe` to process them in a batch. We then stored each token together with its general and detailed POS tags.

## Slide 6 — 05 · Token count results: Review length overview

Across all 20 reviews, spaCy found 3,708 tokens. The shortest review had 38 tokens, while the longest had 461.

## Slide 7 — 06 · Review lengths: Review lengths vary

The average review contains 185.4 tokens. This large range shows that the reviews are very different in length.

## Slide 8 — 07 · Displaying the results: From processed text to tables

We used pandas to show the review numbers and token counts. We also printed the first 20 tags for each review, while the complete tagged text stayed stored in the notebook.

## Slide 9 — 08 · Part-of-speech tagging: Words get grammar labels

Part of speech means the grammatical role of a word. For example, spaCy labels “reviewers” as a noun and “mentioned” as a verb.

## Slide 10 — 09 · POS tag sets: Counting Universal and Penn tags

This code counts both Universal and Penn POS tags. Universal tags give broader categories, while Penn tags are more detailed.

## Slide 11 — 10 · POS frequency results: Universal and Penn tag frequencies

Across the 20 reviews, nouns are the most common Universal tag. Under the Penn system, common nouns, determiners, and prepositions are the most frequent tags.

## Slide 12 — 11 · Example notebook output: What the word tags look like

This screenshot shows the printed output.
Frequency

## Slide 11 — 10 · What we learned: Useful first step, not the final answer

example.

## Slide 12 — 11 · screenshot

NUM (Numeral - one,1,20) and 
CD (Cardinal number, one, 1) 
and not ordinal number (1st, 2nd)

## Slide 13 — 12 · 3q

Entity recognition.