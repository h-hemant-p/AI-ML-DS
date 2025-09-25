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
* **NLP Pipeline**
