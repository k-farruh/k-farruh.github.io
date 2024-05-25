---
title: 'Led Explanation Of Bert Gpt Pre Training Model'
date: draft_Deta
permalink: /posts/draft_D/Detailed-explanation/
tags:
  - cool posts
  - category1
  - category2
---

Detailed explanation of bert GPT pre-training model
 \* {
 font-family: Georgia, Cambria, "Times New Roman", Times, serif;
 }
 html, body {
 margin: 0;
 padding: 0;
 }
 h1 {
 font-size: 50px;
 margin-bottom: 17px;
 color: #333;
 }
 h2 {
 font-size: 24px;
 line-height: 1.6;
 margin: 30px 0 0 0;
 margin-bottom: 18px;
 margin-top: 33px;
 color: #333;
 }
 h3 {
 font-size: 30px;
 margin: 10px 0 20px 0;
 color: #333;
 }
 header {
 width: 640px;
 margin: auto;
 }
 section {
 width: 640px;
 margin: auto;
 }
 section p {
 margin-bottom: 27px;
 font-size: 20px;
 line-height: 1.6;
 color: #333;
 }
 section img {
 max-width: 640px;
 }
 footer {
 padding: 0 20px;
 margin: 50px 0;
 text-align: center;
 font-size: 12px;
 }
 .aspectRatioPlaceholder {
 max-width: auto !important;
 max-height: auto !important;
 }
 .aspectRatioPlaceholder-fill {
 padding-bottom: 0 !important;
 }
 header,
 section[data-field=subtitle],
 section[data-field=description] {
 display: none;
 }
 

Detailed explanation of bert GPT pre-training model
===================================================




In recent years, due to the vigorous development of pretrained models (Pretrained Models, PTMs), “pretraining (pretrain) + fine-tuning…




---

### Detailed explanation of bert GPT pre-training model

In recent years, due to the vigorous development of pretrained models (Pretrained Models, PTMs), “pretraining (pretrain) + fine-tuning (finetune)” has become a standard paradigm in the field of AI model development. The role of the pre-training model can be imagined. It greatly promotes the implementation of AI, allowing the development of AI models to move from the manual workshop mode to the factory mode, and quickly adapt to the customization needs of the AI ​​market. But it is by no means an airborne artifact. The research on pre-training originated from migration learning. The core idea of ​​transfer learning is to use existing knowledge to learn new knowledge. Generally speaking, a pre-trained model is reused in another task. The early pre-training models were mainly based on labeled data. The first wave of pre-training models occurred in the CV field, benefiting from the powerful visual information in the ImageNet[1] dataset, which contains millions of images. Thousands of categories of pictures cover various objects in daily life. Models pre-trained on ImageNet (such as ResNet50) are widely used in various downstream tasks in the image field, and have achieved excellent progress. In the NLP field, due to the diversity of downstream tasks and the complexity of data labeling, it is impossible to obtain a large-scale labeled data like ImageNet, so the NLP field tries to use self-supervised learning methods to obtain pre-training models, self-supervised The main idea of ​​learning is to use the intrinsic relationship between texts as a supervisory signal. Through self-supervised learning, a large amount of unlabeled text data can be exploited to capture general language knowledge. The NLP models in the early NLP field were mainly research on word embedding, such as word2Vec[2], Glove[3], etc., which still play an important role in various NLP tasks. The Transformer structure [4] that appeared in 2017 has brought great breakthroughs to the development of pre-training models in the NLP field. The success of Transformer has also induced the CV field to join the track of self-supervised pre-training models. Nowadays, self-supervised pre-training has become the focus of current artificial intelligence research. Almost all the latest PTMs use Transformer-like structures and self-supervised learning methods. Next, we will introduce more representative self-supervised pre-trained language models.

![](https://cdn-images-1.medium.com/max/800/0*Ks3TSK9_ph1cmD4t.png)### 2. Model structure

The key to the success of PTM is self-supervised learning and Transformer. This section starts with Transformer, the dominant neural architecture. Then two landmark Transformer-based PTMs, GPT[6] and BERT[7], are introduced. All subsequent PTMs are basically variants of these two models.

### 2.1 Transformers

Transformer is a sequence-to-sequence (seq2seq) architecture consisting of an encoder and a decoder. Speaking of Transformer, we have to mention its attention mechanism (Attention). For the principle analysis of the attention mechanism, please refer to [5]. Here we mainly summarize the three attention mechanisms that exist in the transformer:

1. Self-attention: Exists in the attention layer in the encoder, using the output of the previous layer as Q, K, V. Given a word, self-attention computes its attention score with all words in the input sequence to represent how much other words contribute to the given lexical feature representation.
2. Mask-attention: It exists in the decoder stage. Through the mask, the calculation process of controlling the attention score only participates in the words on the left side of the current vocabulary. Because the decoder is a process of word-by-word generation from left to right.
3. Cross-attention: It also exists in the decoder stage, using the output of the previous layer as Q, and using the output of the encoder as K, V. The main role of the cross-attention mechanism is to use the information of its input sequence in the process of generating words, which is especially important in seq2seq tasks such as machine translation and text summarization.

![](https://cdn-images-1.medium.com/max/800/0*oQA7LEHQxVVHViVj.png)### 2.2 GPT

GPT is the first PTM to apply self-supervised learning objectives on the Transformer structure. It only uses the Transformer’s decoder as the basic structure. Due to the self-supervised learning, the cross-attention layer is deleted. GPT is a standard autoregressive language model. Its learning goal is to predict the next word based on the above, so it is often more suitable for natural language generation tasks.

![](https://cdn-images-1.medium.com/max/800/0*iJ0MMHT7IlRLz151.png)Figure 4 The difference between BERT and GPT [5]

### 2.3 BERT

BERT is based on a bidirectional Transformer structure and only uses the Transformer’s encoder structure. The two-way here is mainly achieved through its pre-training goal. BERT designed a masked language modeling (MLM) pre-training task to predict masked vocabulary according to the context. “Two-way” is reflected in the fact that when performing attention calculations, BERT will also consider the influence of words around the masked word on it. BERT is a self-encoding language model that is more suitable for natural language understanding tasks.

### 2.4 Rising star

After GPT and BERT, there have been many variants based on them. Figure 5 lists the main members of the current pre-training model family. Part of the work is dedicated to improving the model architecture and exploring new pre-training tasks; part of the work is dedicated to exploring the richness of data, such as multilingual and multimodal PTMs; and part of the work is dedicated to exploring models with more parameters and PTM computational efficiency Optimization.

![](https://cdn-images-1.medium.com/max/800/0*VBja0NUI0kWeM-gh.png)Figure 5 Pre-training model family [5]

### 3. Pre-training tasks

The main goal of the pre-training model is how to use unlabeled corpus to obtain general knowledge for rapid migration to various downstream tasks. The design of the pre-training task, i.e. the learning objective, is crucial. The previous article also mentioned the pre-training tasks Autoregressive language modeling and masked language modeling of GPT and BERT. They are also pre-training tasks that cannot be replaced by auto-regressive language models and auto-encoded language models respectively. New pre-training tasks explored in some subsequent PTMs Tasks are added on this basis. Some common pre-training tasks are summarized in the table below. For single-resource data input (single-language plain text), new pre-training tasks are often designed by mining the inner relationship between words, sentences, and texts between texts; for multi-resource data input, such as multi-language and multi-modal pre-training models, Designing new pre-training tasks is often considered from how to construct a unified feature representation of different languages ​​and different modalities.

![](https://cdn-images-1.medium.com/max/800/0*7sYNRaxMj8PEkhBo.png)### 4. Summary

This article introduces the origin and development of the pre-training model as a whole. Most of the content of the article comes from the paper [5]. On this basis, some summary and sorting are made. If you are interested, you can read the original text. The development of pre-training models has undoubtedly promoted the implementation of AI. In recent years, as the neural network structure design technology gradually matures and tends to converge, and the scale of data and model parameters continues to increase, the industry has also set off an upsurge of “refining large models”, and is committed to building the cornerstone model in the AI ​​​​field. For the application of the pre-training model, in addition to “pretrain+finetune”, a new paradigm “pretrain+prompt+predict” has gradually become popular, which is dedicated to reconstructing different downstream tasks and creating a unified multi-task model. In the final analysis, everyone is actually solving the same problem: “how to quickly and effectively develop AI models”, which is also an important topic of research in the field of AI.

  




[View original.](https://medium.com/p/9dd8c14aa877)

Exported from [Medium](https://medium.com) on May 25, 2024.

