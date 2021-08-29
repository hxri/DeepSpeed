from deepspeed.utils import RepeatingLoader
from deepspeed.runtime.dataloader import DeepSpeedDataLoader
import torch
import deepspeed
from common import distributed_test
from simple_model import SimpleModel, args_from_dict, random_dataset


def test_repeating_loader():
    loader = [1, 2, 3]
    loader = RepeatingLoader(loader)

    for idx in range(50):
        assert next(loader) == 1
        assert next(loader) == 2
        assert next(loader) == 3


def test_dataloader_drop_last(tmpdir):
    config_dict = {
        "train_batch_size": 1,
        "steps_per_print": 1,
    }
    args = args_from_dict(tmpdir, config_dict)
    hidden_dim = 10

    model = SimpleModel(hidden_dim)

    @distributed_test(world_size=[1])
    def _test_dataloader_drop_last(args, model, hidden_dim):
        optimizer = torch.optim.AdamW(params=model.parameters())
        batch_size = model.train_micro_batch_size_per_gpu()
        model, _, _, _ = deepspeed.initialize(args=args,
                                              model=model,
                                              optimizer=optimizer)
        train_dataset = random_dataset(total_samples=50,
                                       hidden_dim=hidden_dim,
                                       device=model.device,
                                       dtype=torch.half)
        data_loader = DeepSpeedDataLoader(train_dataset,
                                          batch_size=batch_size,
                                          dataloader_drop_last=True)
        for n, batch in enumerate(data_loader):
            loss = model(batch[0], batch[1])
            model.backward(loss)
            model.step()

    _test_dataloader_drop_last(args=args, model=model, hidden_dim=hidden_dim)
