---
title: 'Sion Neural Network Modelscope Text2Video 1 7B'
date: draft_Diff
permalink: /posts/draft_D/Diffusion-neural/
tags:
  - cool posts
  - category1
  - category2
---

Diffusion neural network ModelScope text2video 1.7B
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
 

Diffusion neural network ModelScope text2video 1.7B
===================================================




Before the AI community had time to recover from the LLM raid and the release of GPT-4, a new attack arrived — on March 19th, the Chinese…




---

### Diffusion neural network ModelScope text2video 1.7B — create a video according to a text description at home

Before the AI community had time to recover from the LLM raid and the release of GPT-4, a new attack arrived — on March 19th, the Chinese ModelScope text2video neural network from Alibaba was released, creating short videos based on a text description.

<https://habr.com/ru/articles/724284/>

![](https://cdn-images-1.medium.com/max/800/0*HEinwdh4tNyeR9tR.GIF)Gallery of examplesWhat are its predecessors?

Videos are created like Imagen, Phenaki and Make-a-Video. It takes the existing text2image model architecture (for example, diffusion type), which builds 2-dimensional images according to the description, and remakes it into a model that builds 2 + 1 dimensional images, where the new dimension is responsible for the connection in time. The model from Alibaba is not the first open source text2video model, before that it was CogVideo (again, from the Chinese).

![](https://cdn-images-1.medium.com/max/800/0*JIauRRBSj2a6xRzN.jpeg)An example of how CogVideo worksWhat is the key difference of this model?

in its minimalism. While CogVideo required at least an A100 with 40 GB of VRAM to run, this model can be run quite comfortably with 12 GB of VRAM, with 6–8 a little less comfortable, but tolerable. Although enthusiasts have already managed to fit it in just 4 GB.

![](https://cdn-images-1.medium.com/max/800/0*IaabkPeD5WYxj2yP.gif)A 24-frame video with a resolution of 192x192, created on a video card with 4 GB of video memory. I remember that habr-article “4.2 gigabytes or how to draw anything”, but only now it is applicable to the videoHow is this model arranged from the inside?

As described above, the model relies heavily on latent diffusion models, specifically Stable Diffusion. At the beginning, the request text is encoded into a vector that is responsible for its visual features using a pre-trained OpenCLIP neural network; the video recording is compressed and translated into latent space by the VQGAN network. Further, while the learning process is going on, first a noise is sequentially selected for the video recording, which will completely erase it into the normal distribution of pixel colors (Gaussian diffusion), and then ‘counter-noise’ is selected to restore it. I will not go into details here, you can read about how diffusion models work on Habré, for example, here <https://habr.com/en/post/713076/>. However, in this model, the noise reduction process is modified: a dependence is introduced for the noise applied to one of the frames on the state of the remaining video frames. At the end of the process, the video is returned to its original resolution using VQGAN.

  


![](https://cdn-images-1.medium.com/max/800/0*HmVx4mqxPIGweDa7.png)Illustration of the sampling processHow to run it?

The developers themselves presented the weight and demo of their model on the Huggingface website and the Google Colab laptop. In addition, due to the fact that this model is only a slightly modified Unet (Unet2d->Unet3d), within a day after the release of the article and the first tweets, a plugin for StableDiffusion WebUI from AUTOMATIC1111 appeared. Let’s use them.

Step 1.

We download weights from the official repository <https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis>. Remember to make sure you have loaded configuration.json in its text form via the raw button and not its html page. We put them in the ‘stable-diffusion-webui/models/ModelScope/t2v’ folder.

  


![](https://cdn-images-1.medium.com/max/800/0*_3Rpob0_dS-18eaV.png)Templates on the repository pageStep 2

Download StableDiffusion WebUI, if you don’t already have it <https://github.com/AUTOMATIC1111/stable-diffusion-webui>, go to the Extensions tab and select text2video in the ModelScope list.

  


![](https://cdn-images-1.medium.com/max/800/0*8-v7h0L0cWk5nuUL.png)Step 3

We enter a text query (here tiny cute green monster and the big flying UFO to match the spirit of Habr) and set the generation parameters, click Generate. We are waiting for some time (until the progress bar is filled in the command line and the green done is displayed)

![](https://cdn-images-1.medium.com/max/800/0*1mfdNi2bHbdl1sOB.png)Plugin Interface  


![](https://cdn-images-1.medium.com/max/800/0*DP7oqqyd3Wlz6U6s.png)command line outputClick on the ‘Click here….’ button and enjoy the result.

  


![](https://cdn-images-1.medium.com/max/800/0*CJJ7stchTHXpsAQD.png)Here is our alien in mp4 format, all that remains is to click on it (and convert it to gif to insert into habr, argh)

  


![](https://cdn-images-1.medium.com/max/800/0*FJyj7SEjBPwNW_V7.gif)Habr-UFO in the representation of a video neural network!So it goes. We are waiting for limitless video memes!  
Finally

Video memes have already begun, for example, on Reddit, using this program, people made a neural network sitcom with Joe Biden and Donald Trump, where the script was written by ChatGPT-4 <https://www.reddit.com/r/StableDiffusion/comments/11xzh08/presenting_joe_and_the_don_100_ai_generated_sitcom/>



[View original.](https://medium.com/p/a7f970541cf0)

Exported from [Medium](https://medium.com) on May 25, 2024.

