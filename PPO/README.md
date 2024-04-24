# PPO - MLP / LSTM for LunarLander-v2
The followings show the environment settings for the group project of COMP3340 by group 9

## System Specifications
The 2 notebooks are tested and trained on `windows 11` with `python 3.10` and `cuda 11.8` using RTX2080Ti. 

## Requirements
```shell
## must run this command first
conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia

## using requirements.txt
pip install -r requirements.txt

## manual install
pip install numba
pip install DI-engine
pip install gym==0.25.1
pip install gym[box2d]
pip install stable-baselines3
pip install sb3-contrib
pip install opencv-python
```

## How to Run
1. download the weights and logs from [here](https://connecthkuhk-my.sharepoint.com/:f:/g/personal/u3578889_connect_hku_hk/EpS52-lNoQBIkpBVz1k4dVkB3KfoI6DL0uKJMugykMXb0Q?e=KzESuY). $~~~$ [Remarks 1]
2. place the downloaded files like the following:
<pre>
project root
|- LunarLander-v2-PPO-LSTM
    |- ckpt
        |- manual_final.zip
    |- log/train
        |- log.txt
        |- progress.csv
    |- policy_config.py
|- LunarLander-v2-PPO-MLP
    |- ckpt
        |- manual_final.pth.tar
    |- log/train
        |- training.log
    |- policy_config.py
|- ppo_lstm.ipynb
|- ppo_mlp.ipynb
</pre>
3. run ppo_mlp.ipynb to test the mlp performance.
4. run ppo_lstm.ipynb to test the lstm performance and compare with that of the mlp. 

## Expected Results
With the random seed set to 0, the average rewards of 20 episodes were:
- PPO-MLP: $~~~~$ 247.93246, $~~~~$ from `ppo_mlp.ipynb` for midterm result
- PPO-LSTM: $~~~$ 211.54303, $~~~~$ from `ppo_lstm.ipynb` for final presentation result $~~~$ [Remarks 2]

## Remarks
1. Both scripts were trained for 6+ hours and required about 6GB VRAM. If you want to retrain the models, set `NO_TRAINING` to `True` in the first cell of each notebook.
2. In training phase, the average rewards were around 180.