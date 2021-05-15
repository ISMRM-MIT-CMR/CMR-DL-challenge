# CMR Deep learning reconstruction

## Tutorials
- Image Denoising
  - Real-valued denoising (magnitude images) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ISMRM-MIT-CMR/CMR-DL-challenge/blob/master/tutorial_denoising_real.ipynb)
  - Complex-valued denoising, where real and imaginary part are stored in separate channels. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ISMRM-MIT-CMR/CMR-DL-challenge/blob/master/tutorial_denoising_2chreal.ipynb)
  - Complex-valued denoising, with complex convolutions and complex activations [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ISMRM-MIT-CMR/CMR-DL-challenge/blob/master/tutorial_denoising_complex.ipynb)
- Image Reconstruction with complex convolutions and complex activations  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ISMRM-MIT-CMR/CMR-DL-challenge/blob/master/tutorial_reconstruction_complex.ipynb)


- Complex Activation Functions [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ISMRM-MIT-CMR/CMR-DL-challenge/blob/master/tutorial_complex_activations.ipynb)

## Challenge: Deep Plug-and-Play Prior [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ISMRM-MIT-CMR/CMR-DL-challenge/blob/master/challenge_plug_and_play.ipynb)

Deep plug-and-play priors exploit the advantages of learning an advanced denoising scheme offline and plugging it into any optimization scheme to solve inverse problems, such as Magnetic Resonance Image Reconstruction.

The goal of this challenge is to find a way to reconstruct complex-valued MR images by using available denoisers. The plug-and-play prior challenge consists of two tasks:

1. Deploying a denoising model. If you plan to use available denoisers trained on real-valued images, you have to think about a way to apply them to the complex-valued images.
2. Definition of an optimization scheme. Inspiration can be found in the Suggested Reading section.
The code parts that have to be changed are marked with TODO.

The dataset `subject1.h5`, containing fully sampled k-space, can be used for quantitative and qualitative evaluation in the deployment phase. The results have to be generated for `subject2.h5`, which contains the undersampled k-space. The challenge will be evaluated quantitatively using the normalized root mean squared error (NRMSE), and based on the creativity and complexity to generate the solution.

We are looking forward to your creative submissions! Happy coding!

### Submission
**Deadline:** Wednesday 19th of May 2021, 11:59 UTC

**Template:** Please fill out the [template](https://ismrm-mit-cmr.github.io/template/ISMRM_MIT_CMR_ReconChallenge.potx) slide with

- Provide a short abstract (max. 150 words) about your solution
- Figure: Provide an overview figure of your solution

**Submission:** Please fill out the [submission form](https://docs.google.com/forms/d/e/1FAIpQLScwdz94oFSCMdp5QICPLu1E1ZyZuy0k1ahWJ1BBjGjCtnikvA/viewform?usp=sf_link) and upload in this form:

- Template: Containing your abstract and overview figure
- Results: Your Jupyter notebook as `*.ipynb` containing your solution

