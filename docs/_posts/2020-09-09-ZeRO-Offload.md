---
layout: single
title: "10x bigger model training on a single GPU with ZeRO-Offload"
excerpt: ""
categories: news
new_post: true
date: 2020-09-09 00:00:00
---

We introduce new technology called ZeRO-Offload to enable **10X bigger model training on a single GPU**.
ZeRO-Offload extends ZeRO-2 to leverage both CPU and GPU memory for training large models. Using a machine with **a single GPU**, our users now can run **models of up to 13 billion parameters** without running out of memory, 10x bigger than the existing approaches, while obtaining competitive throughput. This feature democratizes multi-billion-parameter model training and opens the window for many deep learning practitioners to explore bigger and better models. .

* Brief overview, see our [press release]( https://www.microsoft.com/en-us/research/?p=689370&secret=iSlooB ).
* Tutorial on how to use ZeRO-Offload, see our [ZeRO-Offload tutorial](https://www.deepspeed.ai/tutorials/zero-offload/).
* The source code for ZeRO-Offload can be found in the [DeepSpeed repo](https://github.com/microsoft/deepspeed).