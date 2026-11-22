# Group 6 — Text Mining Results

Team: Haru, Marcus, and Sashe.

Speaking script for the eleven-slide deck; target length is about four minutes.

## Slide 1 — Group 6: From movie reviews to data

Hi, we are Group 6: Haru, Marcus, and Sashe. We used spaCy to split the first 20 IMDB reviews into tokens and label their parts of speech. We will show the code briefly and focus on what it produced.

## Slide 2 — 01 · The sample: What went in?

The full dataset contains 50,000 reviews. We selected the first 20 rows; ten have positive labels and ten have negative labels. Those sentiment labels already exist in the dataset. Our task is to organize the text, not predict the sentiment.

## Slide 3 — 02 · Loading the dataset: Getting the reviews

This screenshot shows how we load the data. KaggleHub downloads the dataset, and the code finds its CSV file. pandas reads the CSV into a table called `imdb`. Finally, `shape` shows the table dimensions and `head()` displays the first rows so we can inspect what we loaded.

## Slide 4 — 03 · Tokenization: A review becomes pieces

Tokenization breaks text into pieces. For example, “One of the other reviewers” becomes five separate tokens. The notebook reports 20 reviews processed and 359 tokens in review one. Across all 20 reviews, there are 3,708 tokens. A token can also be punctuation, not just a word.

## Slide 5 — 04 · Processing the reviews: How spaCy produces the results

In this screenshot, we load spaCy’s English model and select the first 20 reviews using `iloc[:20]`. The `nlp.pipe` function processes them in a batch. We then store the token text separately, as well as a tuple containing each token’s text, general part-of-speech label, and detailed tag. The final print statements report the number of reviews and the token count for the first review.

## Slide 6 — 05 · Token count results: Tokens in each review

This table lists the token count for every review. Review one has 359 tokens; review ten has only 38, while review thirteen has 461. The index starts at zero, while the review numbers start at one. This makes it easy to compare the lengths without reading every review.

## Slide 7 — 06 · Displaying the results: From processed text to tables

This screenshot shows how the results are displayed. First, pandas builds the review-number and token-count table we just saw. Then a loop prints the first 20 tagged tokens for each review. The complete tagged reviews remain stored in `pos_tagged_reviews`; the printed output is only a shorter preview.

## Slide 8 — 07 · Review lengths: A quick range check

On average, a review contains 185.4 tokens. The shortest has 38 and the longest has 461. The range matters because an average alone hides how much the review lengths differ. Longer reviews naturally provide more tokens, which matters when comparing raw counts.

## Slide 9 — 08 · Part-of-speech tagging: Words get grammar labels

PoS means part of speech. For example, spaCy labels “reviewers” as a noun and “mentioned” as a verb. Across all 20 reviews, the output contains 608 nouns, 409 punctuation tokens, and 366 verbs. These counts describe the sample; they do not tell us whether the reviews are positive or negative.

## Slide 10 — 09 · Example notebook output: What the word tags look like

This screenshot shows the printed output. Each tuple contains the token, its general PoS label, and a more detailed tag. For example, the first tuple labels “One” as NUM and gives it the detailed tag CD. The screenshot is a preview, not the complete tagged text for each review.

## Slide 11 — 10 · What we learned: Useful first step, not the final answer

We converted 20 raw reviews into tokens and grammatical labels, then measured and displayed the results. This prepares text for further analysis, but it does not by itself predict sentiment or fully understand a review. A possible next step is to compare patterns in positive and negative reviews.
