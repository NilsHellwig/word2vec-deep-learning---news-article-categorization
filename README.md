# News classificator with Word2Vec (Deep-Learning algorithm)

## NPM Scripts

* 🔥 `start` - run development server
* 🔧 `serve` - run development server

## How does it work?

First all words from the vocabulary are loaded. Each word becomes an embedding (300 dimensions). The used vocabulary contains over one million words. The used vocabulary can be downloaded [here](https://deepset.ai/german-word-embeddings) (>1GB). From the training data (several thousand news article names) a separate vector is calculated for each news section (e.g. sports, business or finance). At the end of the calculations, the vector for the user input is also calculated. The vector of the news section that has the smallest angle compared to the user input is then assigned.
