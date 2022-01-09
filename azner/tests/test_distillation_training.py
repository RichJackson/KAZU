import tempfile

from azner.tests.utils import TEST_ASSETS_PATH, BERT_TEST_MODEL_PATH
from azner.modelling.distillation.train import start

DATA_DIR = TEST_ASSETS_PATH.joinpath("tinybern")


def test_stage_2_tinybert_distillation(override_kazu_test_config):
    with tempfile.TemporaryDirectory() as f:
        cfg = override_kazu_test_config(
            overrides=[
                f"DistillationTraining.model.student_model_path={BERT_TEST_MODEL_PATH}",
                f"DistillationTraining.model.teacher_model_path={BERT_TEST_MODEL_PATH}",
                f"DistillationTraining.model.data_dir={DATA_DIR}",
                f"DistillationTraining.save_dir={f}",
                "DistillationTraining.training_params.max_epochs=2",
            ],
        )

        start(cfg)
