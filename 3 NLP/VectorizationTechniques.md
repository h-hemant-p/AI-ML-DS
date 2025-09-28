## Vectorization Techniques

##### 1. Bag of Words

It creates a list of all the unique words in your dataset (called vocabulary), and then for each sentence, it counts how many times each word appears. It doesn’t care about grammar or the order of words only the word frequency matters. That’s why it’s called a "bag" jumbled, unordered collection of words.

Results in a **sparse matrix***
*A **sparse matrix** is a matrix where  **most of the elements are zero** .

* **Steps in BoW**

  1. **Build Vocabulary**

     * Collect all unique words across the dataset.
     * Example:
       * Corpus = `["NLP is fun", "Machine learning is fun"]`
       * Vocabulary = `[NLP, is, fun, Machine, learning]`
  2. **Vectorize Documents**

     * Represent each document as a vector of word counts (or presence/absence).
     * Example:
       * "NLP is fun" → `[1, 1, 1, 0, 0]`
       * "Machine learning is fun" → `[0, 1, 1, 1, 1]`

     **Final Result in sparce matrix**

     | Document | fun | is | learning | Machine | NLP |
     | -------- | --- | -- | -------- | ------- | --- |
     | Doc1     | 1   | 1  | 0        | 0       | 1   |
     | Doc2     | 1   | 1  | 1        | 1       | 0   |
* Pros

  1. Easy to implement
  2. Fixed size of vector in sparce matrix
  3. Works well for small datasets.
* Cons

  1. Leads to **sparse vectors** (many zeros).
  2. Ignores word order (no context).
  3. Ignores semantics (meaning of words).
  4. Vocabulary size grows quickly →  **high dimensionality** .
* Application

  * Text Classification (spam detection, sentiment analysis).
  * Information Retrieval (search engines).
  * Document Similarity (comparing word distributions).
* Vocabularies

  1. **Uni-Gram** : uses a single word in vocabulary for a word.
     * Like in unigram "Very" and "Good" both will be considered as different individual words.
  2. **N-Gram** : uses combination of 2 or more words to create an unique single word for vocabulary.
     * But in if we combine "Very" and "Good" together and consider "Very Good" as an induvidual word then it will considered in BiGram(N-Gram).
     * N-Grams can increase symentic meanings (Pro)
     * It increases dimantionality (Con)
* Source Code

  ```python
  from sklearn.feature_extraction.text import CountVectorizer

  documents = [
      "NLP is fun",
      "Machine learning is fun"
  ]

  # I is an stopword so vectorizer will automatically remove it

  vectorizer = CountVectorizer()

  # If using n-gram
  # vectorizer = CountVectorizer(ngram_range=(1,2)) # can be from how many words, to how many words to consider

  x = vectorizer.fit_transform(documents)
  print("Vocabulary : ", vectorizer.get_feature_names_out())
  print("Feature matrix : \n", x.toarray())
  ```

---

##### 2. TF IDF

TF = Term Frequency
IDF = Inverse Doc Frequency

$$
\text{TF} = \frac{\text{No. of occurrences of Term in Document}}{\text{Total no. of Terms in Document}}
$$

$$
\text{IDF} = \log_e\left( \frac{\text{Total no. of Documents in Corpus}}{\text{Number of Documents containing the Term}} \right)
$$

$$
\text{TFIDF Score} = \text{TF}*\text{IDF}
$$

* Source Code

  ```python
  from sklearn.feature_extraction.text import TfidfVectorizer

  documents = [
      "NLP is fun",
      "Machine learning is fun"
  ]

  vectorizer = TfidfVectorizer()
  x = vectorizer.fit_transform(documents)
  print("Vocabulary : ", vectorizer.get_feature_names_out())
  print("Feature matrix : \n", x.toarray())
  ```
  **Final Result**

  | Document | fun              | is              | learning              | Machine              | NLP              |
  | -------- | ---------------- | --------------- | --------------------- | -------------------- | ---------------- |
  | Doc1     | TFIDF Score(fun) | TFIDF Score(is) | TFIDF Score(learning) | TFIDF Score(Machine) | TFIDF Score(NLP) |
  | Doc2     | TFIDF Score(fun) | TFIDF Score(is) | TFIDF Score(learning) | TFIDF Score(Machine) | TFIDF Score(NLP) |

  | Document | fun        | is         | learning   | Machine    | NLP        |
  | -------- | ---------- | ---------- | ---------- | ---------- | ---------- |
  | Doc1     | 0.50154891 | 0.50154891 | 0          | 0          | 0.70490949 |
  | Doc2     | 0.40993715 | 0.40993715 | 0.57615236 | 0.57615236 | 0          |
