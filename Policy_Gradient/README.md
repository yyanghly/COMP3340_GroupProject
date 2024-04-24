# Policy Gradient

This directory contains the implementation of Policy Gradient algorithm used in midterm report.

## Environment Installation

- Experiment environment:
  - Ubuntu 18.04
  - Python 3.9.7
  - torch 2.1.1
  - CUDA 12.1
  - GPU RTX-4090
  - Nvidia Driver Version 530.41.03
- Jupyter notebook environment is required to run our code.
- Run the notebook code block below or run them in terminal by removing the exclamation mark to install neccessary packages.

```python
# Create new conda environment
!conda create -n comp3340 python=3.9
!conda activate comp3340

# Install linux packages
!sudo apt-get install python3-opengl -y
!sudo apt-get install xvfb -y

# Install python packages
# `gym' does not support Windows platform. 
!pip3 install piglet
!pip3 install pyvirtualdisplay numpy torch torchvision torchaudio gymnasium tqdm matplotlib jupyter
!pip3 install ipywidgets widgetsnbextension
!pip3 install swig
!pip3 install gym[box2d]
!pip3 install box2d-py ipykernel ipywidgets widgetsnbextension
!pip3 install -q gymnasium[box2d]

# To add tensorboard visualization support
!pip3 install tensorboard
```

## Project Scripts

- `LunarLander-GradientPolicy.ipynb`: Project code of gradient policy algorithm.
- `LunarLander-DQN.ipynb`: Project code of DQN algorithm.
- The comments in the code file specified the model definition, training, and testing code.
- Simply executing all the code blocks in order will reproduce our experiment.
- **We use tensorboard to visualize and analyze experiment results. Corresponding logs can be found in 'runs' folder.**

## Tensorboard Logs

- Folder `runs` contains tensorboard logs of different experiment configurations.
- Log naming format: {model}-{net structure}-{optimizer}-{epochs}-{episodes per epoch}-{device}
- Experiment figures in our project report are exported from these logs.
- To visualize and check the logs:
  1. In terminal, change to this directory and run `tensorboard --logdir=runs` (make sure tensorboard is installed)
  2. Open `http://localhost:6006` in browser.
  3. The changes of rewards for different experimental configurations can be seen in the web page.
