_hidden_size = 200
_code_len = 200
_save_path = 'save/model/baseline_524'
_max_epoch = 10

source_encoder_hparams = {
    "encoder_minor_type": "UnidirectionalRNNEncoder",
    "encoder_minor_hparams": {
        "rnn_cell": {
            "type": "GRUCell",
            "kwargs": {
                "num_units": _hidden_size,
            },
        },
    },
    "encoder_major_type": "UnidirectionalRNNEncoder",
    "encoder_major_hparams": {
        "rnn_cell": {
            "type": "GRUCell",
            "kwargs": {
                "num_units": _hidden_size,
            },
        }
    }
}

target_encoder_hparams = {
    "rnn_cell": {
        "type": "GRUCell",
        "kwargs": {
            "num_units": _hidden_size,
        },
    }
}

opt_hparams = {
    "optimizer": {
        "type": "AdamOptimizer",
        "kwargs": {
            "learning_rate": 0.001,
        }
    },
    "learning_rate_decay": {
        "type": "inverse_time_decay",
        "kwargs": {
            "decay_steps": 1600,
            "decay_rate": 0.8
        },
        "start_decay_step": 0,
        "end_decay_step": 16000,
    },
}