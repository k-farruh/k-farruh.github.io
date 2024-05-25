---
title: 'Latest Aop Net An All In One Perception Network For 3D Detection And Panoramic Segmentation'
date: draft_Noah
permalink: /posts/draft_N/Noah-latest/
tags:
  - cool posts
  - category1
  - category2
---

Noah latest! AOP-Net: An All-in-One Perception Network for 3D Detection and Panoramic Segmentation
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
 

Noah latest! AOP-Net: An All-in-One Perception Network for 3D Detection and Panoramic Segmentation
==================================================================================================




Introduction: This paper proposes a LiDAR-based multi-task framework, All-in-One Perceptual Network (AOP-Net), which combines 3D detection…




---

### Noah latest! AOP-Net: An All-in-One Perception Network for 3D Detection and Panoramic Segmentation

**Introduction:** This paper proposes a LiDAR-based multi-task framework, All-in-One Perceptual Network (AOP-Net), which combines 3D detection and panoptic segmentation. The paper develops a dual-task 3D backbone to extract panoramic and detection-level features from input LiDAR point clouds. In addition, a new 2D backbone is designed to interweave multi-layer perceptron (MLP) and convolutional layers to further improve detection task performance. Finally, a novel module is proposed to guide the detection head by recovering useful features discarded during the downsampling operation in the 3D backbone. This module utilizes the estimated instance segmentation mask to recover detailed information from each candidate object. AOP-Net achieves state-of-the-art performance on the nuScenes benchmark for 3D object detection and panoptic segmentation tasks. Furthermore, experiments show that our method is easily adaptable to any BEV-based 3D object detection method and significantly improves its performance

### Summary

LiDAR-based 3D detection and panoramic segmentation are two key tasks in autonomous vehicle and robotic perception systems. In this paper, we propose a LiDAR-based multi-task framework, All-in-One Perceptual Network (AOP-Net), which combines 3D detection and panoptic segmentation. The paper develops a dual-task 3D backbone to extract panoramic and detection-level features from input LiDAR point clouds. In addition, a new 2D backbone is designed to interweave multi-layer perceptron (MLP) and convolutional layers to further improve detection task performance. Finally, a novel module is proposed to guide the detection head by recovering useful features discarded during the downsampling operation in the 3D backbone. This module utilizes the estimated instance segmentation mask to recover detailed information from each candidate object. AOP-Net achieves state-of-the-art performance on the nuScenes benchmark for 3D object detection and panoptic segmentation tasks. Furthermore, experiments show that our method is easily adaptable to any BEV-based 3D object detection method and significantly improves its performance.

In summary, the main contributions of the paper are as follows:

* A multi-task framework for LiDAR-based 3D object detection and panoptic segmentation is proposed. In this approach, performance gains can be achieved for both tasks as they benefit from each other;
* Deep and efficient 2D backbone, hybrid MLP and convolutional layers for 3D detection;
* The IFR module enhances the detection head and recovers useful discarded multi-scale features based on panoptic segmentation estimation;
* Experiments show that each new component provides effective performance gain, and the proposed framework is easily adaptable and improves the performance of any BEV-based 3D object detection method.

### related work

### 3D detection

Efficient 3D detection methods quantify 3D space using small voxel grids and operate on the BEV plane. Features are then extracted to encode each voxel. VoxelNet [1] designed a learnable Voxel Feature Encoder (VFE) layer to encode the point cloud within each voxel, and then utilized 3D CNN to extract features across voxel grids. SECOND [12] proposes a 3D sparse convolutional layer to reduce the computation of 3D convolutions by exploiting the sparsity of the voxel grid. PointPillars [2] further improves the inference speed by reducing the number of voxels along the height dimension to 1 and using a 2D CNN to process the generated fake images. CenterPoint [10] is an anchor-free object detection method that solves the challenges brought by anchor-based methods. CenterPoint designed a center-based detection head to detect the center of the 3D box in the BEV plane. This approach significantly improves detection accuracy since it does not require fitting an axis-aligned box to a rotated object.

### 3D panorama segmentation

3D panoptic segmentation methods are often extended from RV-based semantic segmentation networks with the additional mechanism of grouping foreground point clouds into clusters, each cluster representing a segmented instance. LPSAD [7] uses a shared encoder with two decoders, where the first decoder predicts semantic labels and the second decoder predicts the center offset of each foreground point cloud, which subsequently uses external algorithms such as BFS and HDBSCAN [14]) clusters nearby shifted point clouds into the same cluster. Panoster [13] uses a learnable clustering method to assign instance labels to each point cloud. CPSeg [6] is a cluster-free panorama segmentation method that segments objects by columnarizing point clouds based on learned embeddings and finding connected pillars through pairwise embedding comparisons.

### 3D multitasking perception

Few attempts have been made to exploit the complementarity of segmentation and detection tasks. PointPainting [27] and FusionPainting [38] append semantic class scores from pre-trained segmentation networks to point clouds before feeding to 3D detection models. A similar approach to the paper’s framework was recently introduced [30], where a panoptic segmentation model and an object detection model are jointly trained. Its cascaded feature fusion module fuses BEV and RV features from detection and panoptic segmentation backbones, respectively. Its class-wise foreground attention module embeds predicted foreground semantic scores into detection features. In [30], although panoptic segmentation is used to improve object detection, the two tasks are not mutually beneficial.

### method

### overview

The paper proposes a framework that jointly implements 3D detection and panoramic segmentation, as shown in Figure 1. In this multi-task approach, the BEV-based 3D detection model and the RV-based 3D panorama segmentation model are deeply integrated, so the performance of both tasks can be significantly improved. Due to its real-time performance and high accuracy, the paper develops a simplified version of CPSeg [6], a U-Net architecture with two task-specific decoders, for panoptic segmentation. For object detection, the paper relies on the detection head of CenterPoint [10] for superior performance.

![](https://cdn-images-1.medium.com/max/800/0*bod-lfC4rJfSKLrF.png)To integrate these two tasks into a unified framework, the paper proposes a dual-task 3D backbone to extract multi-scale features from voxelized point clouds. These features are compressed and projected to the RV plane, fused with a set of features extracted directly from the RV projected point cloud via three convolutional Bottleneck Attention Modules (CBAM) [22], and fed to the panorama head. This lightweight operation effectively enhances the detection-level features of the panoramic head. To introduce panoptic-level features into detection, the paper utilizes the cascaded feature fusion and class-wise foreground attention modules in [30], as shown in the multi-view feature fusion in Figure 1.

The lowest-resolution voxel features from the dual-task 3D backbone are projected to BEVs for the detection task. In addition to detection-level information, these features encode instance- and semantic-level information. Furthermore, inspired by [15], a more efficient 2D backbone is proposed, which mixes MLP with convolutional layers to process the features of detection heads. Furthermore, the novel IFR module enhances the detection head by exploiting the predicted instance masks to recover relevant object features lost during the downsampling operation in the dual-task 3D backbone.

### Dual-tasking 3D backbone

As shown in Figure 2, the 3D backbone used in our method is responsible for extracting features from 3D voxels.

![](https://cdn-images-1.medium.com/max/800/0*q1XaLJVD3_4p2XAh.png)In order to efficiently transfer features from the 3D backbone to the object detection task, the paper follows [1], [12], [10] and uses the coarsest resolution

![](https://cdn-images-1.medium.com/max/800/0*2I3GQRYbfrGqQVTS.png)3D features are mapped to BEVs, which in turn are fed to a 2D backbone. Unlike previous methods, however, the detailed object information embedded in two sets of higher-resolution voxel features will be recovered later in the IFR module. In addition, three sets of higher-resolution voxel features are projected to RV, fused with features extracted directly from the RV projected point cloud via corresponding CBAM, and processed by the RV encoding block of CPSeg. These multi-scale voxel-based features enhance the RV-based panoramic head. At the same time this enhancement also strengthens the 3D backbone to develop a richer set of semantic and instance-level features.

### Simplified ConvMLP (SC) Backbone

Recently MLP-based vision backbones have received more attention due to their competitiveness or even better performance than fully convolutional backbones in dense vision prediction tasks [17], [18], [19], [16], [15] ].

Inspired by the ConvMLP [15] used in the image domain, the paper proposes a simplified version of this architecture to process BEV projected features from a 3D backbone, which are then fed to the detection head. The simplified ConvMLP (SC) block and the proposed 2D backbone architecture are shown in Fig. 3. Compared to the original ConvMLP block, the last MLP layer is removed and skip connections are added on the convolutional layers to further simplify the gradient flow. In this architecture, the MLP block realizes the interaction of features in each spatial location, while the subsequent depthwise convolution realizes the effective spatial interaction. Successive Conv blocks (each block consisting of a convolutional layer, followed by BN and ReLU) are first applied in the backbone to enhance feature interactions over space. Then, the generated features are sent through the first set of SC blocks, downsampled, and fed to another set of SC blocks. The outputs of these two sets of SC blocks are then matched and concatenated into the final set of 2D features, which is fed to the detection head.

![](https://cdn-images-1.medium.com/max/800/0*V4ZOqdyspC1xwo5u.png)Compared with conventional 2D backbones in [2], [10], the proposed 2D backbone improves detection performance without greatly increasing model complexity. More specifically, SC blocks require 54.6% less memory and 54.8% less FLOPs than regular 3x3 convolutional layers. Therefore, by replacing regular convolutions with lighter SC blocks, more consecutive convolutions can be built in a single resolution, leading to larger receptive fields without further downsampling. Furthermore, unlike other CNNs that use a single 1x1 convolutional layer for channel depth adjustment, this architecture makes extensive use of MLP blocks to emphasize feature extraction within each BEV plane location.

### Instance-based Feature Retrieval (IFR)

To enhance the coarse-scale features extracted by the SC backbone, the features discarded during the downsampling operation in the dual-task 3D backbone can be effectively utilized. The IFR module is proposed for this purpose, as shown in Figure 4. This module is derived from the dual task 3D backbone

![](https://cdn-images-1.medium.com/max/800/0*ffJbHRal-pNuigRm.png)and high-resolution feature maps to recover the multi-scale detailed features of each candidate object. A new set of features is then constructed to enhance the detection head.

![](https://cdn-images-1.medium.com/max/800/0*CGc8zOeATSIxC1UQ.png)First, to reduce computational complexity, at all BEV plane locations, the voxel features along the height dimension are averaged to form an average voxel feature. Then, a selection strategy based on instance masks for panoramic head estimation is proposed to select average voxels. Specifically, given the lth scale of the same scale on the BEV plane

![](https://cdn-images-1.medium.com/max/800/0*7CVVTDbvw1lz9Wwg.png)Average voxel features and instance masks, compute the average X and Y coordinates for each instance. This will give the centroid location for each instance. Then, from all the BEV positions representing each instance, select the one closest to the centroid of each instance

![](https://cdn-images-1.medium.com/max/800/0*hr1M3DSM4lfzfEtZ.png)average voxel.

After sampling the Ksl average voxel of each instance, the relative coordinates of each sampled average voxel to its instance centroid on the x-axis and y-axis are calculated and concatenated to the corresponding feature vector as the relative position embedded. This allows the IFR module to understand the geometry of the sampled average voxel for each instance. These feature vectors are successively passed through the VFE [1] and MLP layers. Then, the resulting feature vectors for each instance are combined using a max and average pooling layer and concatenated. The following equation illustrates this:

![](https://cdn-images-1.medium.com/max/800/0*-1uI9OtVQJrflnPm.png)Each generated single eigenvector

![](https://cdn-images-1.medium.com/max/800/0*k8-ISQAu7xlQGumM.png)The sampled average voxel features of its corresponding i-th instance are encoded and aggregated. A cascade connection is used to combine the higher resolution

![](https://cdn-images-1.medium.com/max/800/0*wim2uCshry7A2Gmv.png)The extracted features of an instance in , are concatenated with the per-sample average voxel-wise feature vectors of that instance in lower resolutions. This makes the lower resolution of the instance

![](https://cdn-images-1.medium.com/max/800/0*eW3VoP3fy8IW905Z.png)Averaging voxels is able to exploit higher resolution encoded features of the same instance. Finally, the resulting encoded feature vectors for each instance at different resolutions are concatenated and distributed to all BEV locations corresponding to that instance according to the coarse-scale instance mask. Then, this new set of feature maps is concatenated to the output features from the 2D backbone and fed to the detection head. By doing so, we effectively enhance the detection head by recovering and processing multi-scale information unique to each instance and usually lost before the 2D backbone.

### experiment

### data set

The paper conducts experiments on nuScenes and Waymo datasets.

### result

**1) 3D detection:** In Table I and Table II, the paper compares the evaluation results of the proposed method and CenterPoint on the nuScene and Waymo validation sets. AOP-Net is based on the first phase of CenterPoint. As shown, the proposed method significantly outperforms CenterPoint in mAP and NDS scores of nuScenes, and significantly outperforms CenterPoint in mAP and mAPH scores of Waymo. As elaborated in Ablation, the SC backbone and IFR module can improve the detection ability of large and small objects, respectively.

![](https://cdn-images-1.medium.com/max/800/0*Tq-qyfbgWJENFeYD.png)![](https://cdn-images-1.medium.com/max/800/0*N7Hr9OQtUJBixR06.png)The comparison between AOP-Net and other published state-of-the-art 3D object detection methods on the nuScene test set is shown in Table III. As can be seen, both speed (mAVE) and attribute (mAAE) in terms of NDS and all five error metrics representing the quality of object box estimation. This improvement can be attributed to the guidance provided by the panoptic segmentation module, both direct (leverage panoptic segmentation prediction in IFR) and indirect (backpropagation of panoptic loss in the backbone).

![](https://cdn-images-1.medium.com/max/800/0*Z0-xYXV3P1Vp5g6r.png)**2) 3D Panoramic Segmentation:** In Table IV, comparing AOP-Net with other state-of-the-art published methods on the nuScene test set, the paper verifies that AOP-Net obtains a higher average PQ. Compared with the second row, which is an independent simplified version of CPSeg originally included in AOP-Net, AOP-Net accepts additional input of multi-scale detection level features, which leads to significantly better panoptic performance.

![](https://cdn-images-1.medium.com/max/800/0*SbCjsIhFA3SQZ1TU.png)In Fig. 5, the benefit of a unified multi-task framework for panoptic segmentation is evident. In example (a), CPSeg alone has difficulty predicting the semantics of distant point clouds, resulting in three false positives and one false negative. In (b), CPSeg is below the segment on the left and above the segment near the top because it is less confident about the less visible regions behind the bulk of the point cloud. In both cases, the dual-task 3D backbone in AOP-Net provides efficient multi-scale 3D features to prevent these errors.

![](https://cdn-images-1.medium.com/max/800/0*6eEBfULlVr2bjPTx.png)### Ablation experiment

**1) The effect of each module** : The contribution of the AOP-Net module is shown in Table V. It can be seen that each and combination of these modules fit the baseline well and provide strong performance gains.

![](https://cdn-images-1.medium.com/max/800/0*mq6rUaShLEUgKkAq.png)Specifically, as can be seen in Table VI, combining the dual-task 3D backbone significantly improves the performance of both tasks. In particular, the improvement of AOP-Net in panoptic segmentation is mainly attributed to this module. Since the 3D backbone depends on two tasks, the learned features are enriched and provide additional cues about foreground objects. Furthermore, the 3D backbone captures features without the occlusion or scale change issues common to feature extraction in the RV plane. When projected to RV and fused with already extracted RV-based features, these feature sets are more reliable and useful in segmenting occluded and distant objects. These factors lead to significant improvements in mIOU and PQ.

In Table VII, the paper demonstrates that the improvement in large class object detection can be attributed to the enlarged receptive field and wider channel-like feature extraction from the SC backbone.

![](https://cdn-images-1.medium.com/max/800/0*HshSmzJboSkJWvw1.png)In Table VIII, it can be seen that IFR plays an important role in better detection of small isolated objects. This is because IFR affects the detection head to pay more attention to multi-scale features related to foreground objects. By reintroducing information lost during downsampling in the 3D backbone, the detection head improves both precision (by refining possible candidates) and recall (retrieving lost objects better detected in RV panoptic segmentation).

![](https://cdn-images-1.medium.com/max/800/0*f_mpxAK5LKMP2rND.png)**2) Variants of the ConvMLP backbone** : In Table IX, similarly sized networks (according to #parameters) using the original ConvMLP have fewer consecutive layers and lower performance. Furthermore, comparing rows 2–4 with 5 and 10 SC blocks gives the best trade-off in terms of performance and complexity.

![](https://cdn-images-1.medium.com/max/800/0*KG_-wDP6U25k-t7r.png)**3) Other BEV-based 3D object detectors in the proposed framework** : In order to demonstrate that AOP-Net can also work with anchor-based detection methods, the paper adapts AOP-Net to PointPillars[2] and SECOND[12 ]conducted an experiment. The results of these experiments are shown in Table X. In addition, the paper increases the model complexity of PointPillars and SECOND and names them Complex PointPillar and Complex SECOND. It can be seen that by simply increasing model complexity, performance gains are either non-existent or limited. However, mAP and NDS are significantly improved under the proposed framework. Figure 6 shows the general effect of the proposed framework. It can be seen that in examples (a) and (b), PointPillars cannot detect small objects due to the loss of fine-scale features during downsampling. On the other hand, in the proposed method, these objects are identified by the RV-based segmentation module, and their fine-scale features are recovered by the IFR module, allowing their detection. Furthermore, in example (b), PointPillars produced two false positives from a distance, while AOP-Net was correctly guided by panoptic-level information and avoided these errors.

![](https://cdn-images-1.medium.com/max/800/0*Fhg1VuUGfA0JODwC.png)### in conclusion

The paper proposes AOP-Net, an all-in-one perception framework for LiDAR-based joint 3D detection and panoramic segmentation. In this framework, the paper designs a dual-task 3D backbone to simultaneously consider the semantic and instance-level information of the scene, thereby enhancing the BEV-based detection head and the RV-based panoramic head. Furthermore, the multi-scale 3D voxel features produced by this backbone are used to enhance single-scale RV feature maps in the panoptic segmentation task. Furthermore, based on the simplified ConvMLP (SC) block, a deep and efficient 2D backbone is proposed, which facilitates the detection improvement. Finally, to recover the features lost during the downsampling operation in the dual-task 3D backbone, a novel instance-based feature retrieval (IFR) module is proposed, which relies on the predicted instance masks and restores features to enhance the detection backbone. . Experimental results on nuScenes and Waymo datasets show significant improvements in both 3D panoptic segmentation and object detection tasks under the proposed framework, and also show that the performance of any BEV-based 3D object detection can be improved using the proposed strategy. Detection accuracy.

### refer to

[1] AOP-Net: All-in-One Perception Network for Joint LiDAR-based 3D Object Detection and Panoptic Segmentation

The original WeChat public account [Autopilot Heart]: a community focusing on autonomous driving and AI ( <https://mp.weixin.qq.com/s/NK-0tfm_5KxmOfFHpK5mBA> )



[View original.](https://medium.com/p/ef115e48e975)

Exported from [Medium](https://medium.com) on May 25, 2024.

