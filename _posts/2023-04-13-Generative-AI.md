---
title: 'Generative Ai Composer The Next Level Of Stable Diffusion'
date: 2023-04-13
permalink: /posts/2023-04/Generative-AI/
tags:
  - cool posts
  - category1
  - category2
---

Generative AI models coupled with relevant text/image data can be used to oeuvre arts, poems, and creative programming codes

### Generative AI, Composer — the Next Level of Stable Diffusion

Coupled with relevant text/image data, generative AI models can be used to oeuvre arts, poems, and creativity programming codes. However, addressing these challenges efficiently with AI is a challenge. Amount many cases, only the best model, SOTA (State Of The Art), can change to overcome the limitations of a given application. Let’s analyze the power of the [Composer](https://arxiv.org/abs/2302.09778) as a new level of Stable Diffusion and check how it can bring benefits.

![](https://cdn-images-1.medium.com/max/800/1*uY0uexkrfQyBdRTNURAnfQ.jpeg)Starting from exampling the Composer's foundation model or public ones, such as Stable Diffusion, it is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input, cultivates autonomous freedom to produce incredible image, and empowers billions of people to create stunning arts within seconds.

A vital question for any model is what kind of tasks it can handle. With its potential applications in image synthesis for artistic or entertainment purposes, the Composer also has practical applications in architecture and interior design. The ability to specify conditions for generating images of buildings or interior spaces could be a valuable tool for architects and designers. Below is the example list of the tasks with illustrations the Composer tested. However, these just are part of the examples; users can create cases based on the Composer.

* *Palette-based colorization:* the Composer to colorize an image *x* according to palette *p* entails conditioning the sampling process on the grayscale version of *x* and *p*.

![](https://cdn-images-1.medium.com/max/800/0*nfaJzIhjEUwNRAfL.jpg)* *Style transfer:* The Composer roughly disentangles the content and style representations, which allows transferring the style of image *x1* to another image *x2* by simply conditioning the style representations of *x1* and the content representations of *x2*. Also it’s possible to control the transfer strength by interpolating style representations between the two images.

![](https://cdn-images-1.medium.com/max/800/0*FscDsu37XHLX7Bwb.jpg)* *Image translation:* Image translation refers to transforming an image to a variant with content unchanged but style converted to match a target domain. It can be used for all available representations of an image to depict its content, with a text description to capture the target domain.

![](https://cdn-images-1.medium.com/max/800/0*hVzu0Qwn_2h4Jo07.jpg)* *Pose transfer:* The CLIP embedding of an image captures its style and semantics, enabling Composer to modify the pose of an object without compromising its identity. The Composer uses the object's segmentation map to represent its pose and the image embedding to capture its semantics, then leverage the reconfiguration to modify the object's pose.

![](https://cdn-images-1.medium.com/max/800/0*9_0uTHIq0wY3j_xt.jpg)* *Virtual try-on:* Given a garment image *x1* and a body image *x2*, the Composer can mask the clothes in *x2*, then condition the sampling process on the masked image *m2* along with the CLIP image embedding of *x1* to produce a virtual try-on result. Despite the moderate quality, the results demonstrate the possibilities of Composer to cope with complex problems with one unified framework.

![](https://cdn-images-1.medium.com/max/800/0*lkQHWklNEbkCpeI7.jpg)* *Compositional Image Generation:* By conditioning the Composer on a combination of visual components from different sources, it is possible to produce an enormous number of generation results from a limited set of materials.

![](https://cdn-images-1.medium.com/max/800/0*QdrrSz0wZEUFJDr4.jpg)* *Text-to-Image Generation:* The Composer uses sampling steps of 100, 50, and 20 for the prior, base, and 64 × 64 to 256 × 256 upsampling models, respectively, and a guidance scale of 3.0 for the primary and base models. Despite its multi-task training, the Composer achieves a competitive FID score of 9.2 and a CLIP score of 0.28 on [COCO](https://cocodataset.org/#home), comparable to the best-performing models.

![](https://cdn-images-1.medium.com/max/800/0*I1BCoFeRlQ88UHi-.jpg)More examples related to composer model results can be found [here](https://damo-vilab.github.io/composer-page/), and the composer model can be tested on ModelScope via this [link](https://modelscope.cn/studios/damo/Composer/summary).



---

### Composer: Creative and Controllable Image Synthesis with Composable Conditions

The above examples greatly inspired the author, but how about the technologies behind them? The paper "[Composer: Creative and Controllable Image Synthesis with Composable Conditions](https://arxiv.org/abs/2302.09778)" — proposes a new method for image synthesis that allows for greater control over the generation process. The Composer method uses a series of composable conditions that can be combined and manipulated to generate images with specific characteristics. It offers a new generation paradigm that allows flexible output image control, such as spatial layout and palette while maintaining the synthesis quality and model creativity. With *compositionality* as the core idea, we decompose an image into representative factors and then train a diffusion model with all these factors as the conditions to recompose the input.

Many traditional image generation and manipulation models have the limitations of existing image synthesis methods, such as the inability to control specific attributes of the generated images. The Composer addresses this issue by allowing users to specify conditions that the generated images must meet, such as the presence of certain objects or the use of particular colors.

One of the unique aspects of Composer is its ability to allow users to specify conditions at different levels of abstraction. For example, a user can specify a condition at a high level, such as "generate an image of a beach," and then add more specific conditions, such as "the beach should have palm trees." This allows for a flexible and customizable image synthesis process that can meet a wide range of needs.

Implementing the Composer is conceptually simple and easy. It's surprisingly powerful, enabling encouraging performance on both traditional and previously unexplored image generation and manipulation tasks, including but not limited to *text-to-image generation, multi-modal conditional image generation, style transfer, pose transfer, image translation, virtual try-on, interpolation and image variation from various directions, image reconfiguration by modifying sketches, depth or segmentation maps, colorization based on optional palettes*, and more.

### How the Composer Works

The Composer consists of two main components: a set of predefined conditions and a neural network that generates images based on these conditions. The conditions can be combined by using Boolean logic, allowing for complex specifications customized to meet specific needs. The neural network is trained on a dataset of images that meet the specified conditions and generates new images that meet the same conditions.

The Composer uses sampling algorithms such as Denoising Diffusion Implicit Models (DDIM), a class of generative models used for image and data denoising. DDIM is a recent development in the field of generative models, and it has gained a lot of attention due to its state-of-the-art performance on image-denoising benchmarks.

DDIM is a diffusion-based generative model that models the noisy data's joint probability density function (PDF) and a noise-free image. The model is trained by learning the conditional distribution sequence that maps the noisy image to the noise-free image over a sequence of diffusion steps. The conditional distributions are known implicitly through a denoising function, which maps the noisy image to the noise-free image at each diffusion step.

The DDIM model consists of a diffusion process that models the transition from the noisy data to the noise-free image. The diffusion process is modeled using a stochastic differential equation (SDE) that describes the evolution of the data over time. The diffusion process starts with a noisy image and iteratively refines the image over a sequence of diffusion steps. The data is perturbed by Gaussian noise at each diffusion step with a decreasing variance.

The denoising function used in DDIM is learned implicitly by minimizing the difference between the predicted and ground truth noise-free images. The denoising function is parameterized using a deep neural network, which inputs the noisy image and noise level and outputs the noise-free image.

One of the critical advantages of DDIM over other generative models is its ability to generate high-quality images with realistic textures and fine details, even in the presence of high noise levels. This is because DDIM uses a diffusion process to model the image generation process, allowing it to capture the fine-grained details of the image.

![](https://cdn-images-1.medium.com/max/800/0*gwD9VvJY7qQjqgEB.jpg)The Composer is a multi-conditional diffusion model with a U-Net backbone. The U-Net network model is a famous deep-learning architecture commonly used in image segmentation tasks. It was initially proposed for biomedical image segmentation but has been applied to other domains since then. In this architecture, the network is composed of two main parts: a contracting path that extracts features from the input image and an expanding path that generates the segmentation mask.

The contracting path of the U-Net network consists of several convolutional layers with max pooling operations that gradually reduce the spatial resolution of the input image while increasing the number of channels. This helps to extract high-level features from the input image while keeping the computation efficient. Each convolutional layer is typically followed by a rectified linear unit (ReLU) activation function, which introduces non-linearity to the model.

The expanding path of the U-Net network consists of several convolutional layers with upsampling operations that gradually increase the spatial resolution of the feature maps while reducing the number of channels. This path helps to recover the spatial details of the segmentation mask from the features extracted by the contracting path. A ReLU activation function also follows each convolutional layer in the expanding path.

One of the main strengths of the U-Net architecture is its skip connections, which connect the corresponding layers of the contracting and expanding paths. These skip connections help preserve the input image's spatial information, essential for accurate segmentation. The skip connections also help mitigate the vanishing gradient problem, a common issue in deep neural networks.

The Composer supports reconfiguring an image by altering its representations, such as sketch and segmentation maps, using CLIP unCLIP, and GLIDE, which refers to attaching and detaching a tool or accessory to a power tool. This mechanism is commonly used in power drills, saws, and sanders.

**CLIP**: The CLIP (Contrastive Language-Image Pre-Training) is a small metal or plastic piece holding the tool or accessory. It is usually located near the chuck of the power tool and can be released with a simple push.

**unCLIP**: Unclipping releases the clip to detach the tool or accessory from the power tool.

**Glide**: Glide is the smooth and effortless movement of the tool or accessory into and out of the power tool. It ensures the instrument or accessory is securely attached and does not come loose during use.

The CLIP unCLIP GLIDE mechanism is essential in power tools as it allows for quick and easy tool changes or accessories, improving efficiency and productivity. It also reduces the risk of injury as it eliminates the need to tighten and loosen screws or bolts manually.

The mechanism is common in cordless power tools, which are becoming increasingly popular due to their portability and convenience. The ability to quickly change tools or accessories is beneficial in cordless power tools as it allows for uninterrupted work, even when a specific tool or accessory is required.

After knowing the Composer the base technologies, let's go over the pros and cons.

#### Advantages

The Composer model has several advantages over other image synthesis methods:

* **Controllability:** The Composable Conditions framework allows users to control the image generation process by specifying the desired conditions. This makes it easier to generate images that match specific requirements.
* **Flexibility:** The Composer model is flexible and can accommodate different types of conditions. Users can specify a wide range of conditions, such as the presence or absence of particular objects, textures, or colors.
* **Creativity:** The Composer model can generate creative, diverse images satisfying user-specified conditions. This is achieved by composing multiple partial generators that capture different aspects of the image.

#### Disadvantages

Despite its advantages, the Composer model also has some limitations:

* **Complexity:** The Composable Conditions framework is complex and requires a significant amount of computational resources. This can make it challenging to use for some applications.
* **Training Data:** The Composer model requires a large amount of training data to learn the underlying patterns in the images. This can be a limitation in some domains with limited data available.

### Summary

In summary, the Composer model is a promising approach to image synthesis that offers several advantages over existing methods. The Composable Conditions framework allows for greater control and flexibility in generating images that satisfy user-specified conditions. However, the model's complexity and training data requirements may be a limitation for some applications. Overall, the Composer model is a significant step forward in the field of image synthesis and has the potential to be used in a wide range of applications.

We look forward to seeing the code and model based on the Composer.



By [Dr. Farruh](https://medium.com/@k-farruh) on [April 13, 2023](https://medium.com/p/d7e3cb8a2a35).

[Canonical link](https://medium.com/@k-farruh/generative-ai-composer-the-next-level-of-stable-diffusion-d7e3cb8a2a35)

Exported from [Medium](https://medium.com) on May 25, 2024.

