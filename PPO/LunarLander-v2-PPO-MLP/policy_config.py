exp_config = {
    'type': 'ppo',
    'on_policy': True,
    'cuda': True,
    'action_space': 'discrete',
    'discount_factor': 0.99,
    'gae_lambda': 0.95,
    'epoch_per_collect': 10,
    'batch_size': 64,
    'learning_rate': 0.0003,
    'lr_scheduler': None,
    'weight_decay': 0,
    'value_weight': 0.5,
    'entropy_weight': 0.001,
    'clip_ratio': 0.2,
    'adv_norm': True,
    'value_norm': 'popart',
    'ppo_param_init': True,
    'grad_norm': 0.5,
    'n_sample': 512,
    'unroll_len': 1,
    'deterministic_eval': True,
    'model': {},
    'cfg_type': 'PPOFPolicyDict',
    'env_id': 'LunarLander-v2',
    'exp_name': 'LunarLander-v2-PPO-MLP'
}
