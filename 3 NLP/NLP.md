## Natural Language Processing

NLP (Natural Language Processing) is a part of Artificial Intelligence that helps computers understand, read, write, and talk like humans.
In short, NLP allows machines to process human language jaise ki English, Hindi, etc. instead of Os and 1s.

* **Approaches of NLP**

  1. Rule Base Approach(Old School NLP)
     * Early method of solving NLP using handwritten rules and grammar logic.
     * You write rules manually to process and understand language.
     * These rules can define grammar, speling corrections, sentence structure, etc.
     * Example: A rule like: "If sentence contains 'not good', mark it as negative sentiment."
     * Used for: Grammar checkers, Spell check, Simple keyword-based chatbots
     * Limitation:
       * Can't handle complex, ambiguous, or new patterns
       * Not scalable for large data
  2. Statistical (Machine Learning) Approach
     * Language is treated like data, and algorithms learn patterns from it.
     * Use of models like:
       * Naive Bayes
       * Logistic Regression
       * SVM (Support Vector Machines)
     * Requires text to be converted into numbers using techniques like Bag of Words, TF-IDF, etc.
     * Example: Train a model on 10,000 product reviews. It learns which words indicate positive or negative sentiment and predicts for new reviews.
     * Used for:
       * Sentiment analysis
       * Spam detection
       * Text classification
     * Limitation:
       * Loses context of words (like sarcasm or sequence of words)
         * Example - "Yeah, because staying up all night debugging is exactly what I dreamed of."
         * ML Thinks: "dreamed", "exactly" > sounds like passion
         * Reality: It's a painful dev life moment.
  3. Deep Learning-Based Approach (Modern NLP)
     * Uses neural networks to automatically learn complex patterns and context from text.
     * Models can understand meaning, context, word order, and more.
     * Popular architectures:
       * RNN (Recurrent Neural Networks)
       * LSTM (Long Short-Term Memory)
       * GRU (Gated Recurrent Units)
       * Transformers (BERT, GPT, T5, etc.)
     * Even in deep learning, we have to convert text into numbers but we don't use traditional techniques like Bag of Words or TF-IDF. Instead, we use more advanced methods like Word Embeddings (Word2Vec, Glove) or Token IDs with Embedding Layers, which actually capture the meaning and context of words.

  * **NLP Pipeline/Workflow** : Collect → Preprocess → Represent → Train → Evaluate → Deploy → Improve
    1. **Geathering Data**

       * Public build  data from kaggle etc.
       * Web scrapping
       * Third party api
       * Manual collection / crowdsourcing
    2. **Data Preprocessing/Cleaning**

       1. Lowercasing
       2. Remove Punctuation
          * Remove symbols like ., !? @ # $ % ^ & * ( ) etc.
          * They don't add meaning in ML context.
          * In deep learning-based NLP (especially with models like BERT, GPT, T5), punctuation can carry meaning, and we usually keep it during preprocessing.
       3. Remove Numbers
          * Remove digits from the text (optional - - depends on task).
          * "I bought 5 phones" →> you may or may not need the number.
       4. Remove URLs / Links
          * Remove any links in the text (very common in social media data)
       5. Remove HTML Tags
          1. If scraping from web, remove things like `<div>`, `<p>`, etc.
       6. Remove Emojis & Special Characters
          * Emojis might break vectorization if not removed or handled
       7. Remove Stopwords
          * Remove common words like "is", "the", "was", "and","in", etc.
          * These don't help in understanding the meaning.
       8. **Stemming/Lemmatization:** Reduce words to their root form.
          * Stemming: `"running"` → `"run"`
          * Lemmatization: `"better"` → `"good"`
       9. (Optional) Spelling Correction
          * Fix spelling mistakes using TextBlob or other libraries
    3. **Vectorization**

       * **Vectorization** is the process of converting raw data (like text, images, or signals) into **numerical vectors (arrays of numbers)** that machine learning models can understand and process.
         1. **Text Data Vectorization:**
            * Words or sentences → numerical vectors.
            * [Methods](https://github.com/h-hemant-p/AI-ML-DS/blob/main/3%20NLP/VectorizationTechniques.md):

              * **[Bag of Words (BoW)](https://github.com/h-hemant-p/AI-ML-DS/blob/main/3%20NLP/VectorizationTechniques.md):** Counts word frequencies.
              * **[TF-IDF](https://github.com/h-hemant-p/AI-ML-DS/blob/main/3%20NLP/VectorizationTechniques.md):** Weights words based on importance in documents.
              * **Word Embeddings:** Word2Vec, GloVe, FastText.
              * **Contextual Embeddings:** BERT, GPT embeddings (capture meaning from context).
            * Example:

              * Sentence: *"Machine learning is fun"*
              * Vectorized (BoW): `[1, 1, 1, 0, 0, ...]` (shows word presence/absence or count).
         2. **Image Vectorization:**
            * An image is already a grid of pixels, but can be vectorized (flattened) into a  **1D vector** .
            * Example: A `28x28` MNIST digit image → vector of length `784`.
         3. **Audio Vectorization:**
            * Raw waveform signals can be vectorized into frequency-domain features like **MFCCs** or spectrograms.
    4. Feature Engineering(POS tags, NER, Sentiment, etc.)
    5. Models Training
    6. Evaluation(Accuracy, F1, BLEU, ROUGE)
    7. Deployment (API, App, Chatbot, Search System)
    8. Continuous Monitoring & Retraining

---

* **Terminologies**

  1. **Corpus** : Collection of texts. dataset of texts.
  2. **Sentence :** A group of words that forms a meaningful statement.
  3. **Teken :** Each individual word or symbol in a text is called as a token.
  4. **Tokenization:** The process of splliting text into tokens is called tokenization.
  5. **Document -** A document in NLP is just a single piece of text inside your dataset. dataset. It can be one sentence, one paragraph, or even a full article depends on your project. If your corpus has 100 movie reviews, then each review is called one document.
  6. **Vocabulary -** A vocabulary in NLP means the list of all unique words present in your corpus.
