# Getting started with the Webots driving experiments

## What the source needs

This project was designed to run **inside Webots**. It imports `vehicle.Driver` and `controller` APIs from the simulator. Simply running the scripts with a normal Python installation will not provide those modules. Set Webots' preferred Python executable to an environment where the dependencies listed in `requirements.txt` are available.

For phase 3, the included Webots world also includes SUMO-related controller code and road/network configuration. Configure a compatible SUMO installation, including `SUMO_HOME` if required by the version of the supervisor, and check the controller names in the world before running.

No simulator version, model checkpoint, or tested dependency lockfile was supplied in the source archive. Compatibility with the newest releases is **not guaranteed**. In particular, some scripts call `keras.src.legacy.saving.legacy_h5_format` and `torchvision.models.resnet18(pretrained=True)`, which can require version-specific adjustments.

## By phase

| Entry point | What to configure | What the source shows |
| --- | --- | --- |
| `phase1_CNN.py` | Webots vehicle controller; CNN at `../small_cnn_model.h5` relative to working directory | Creates PPO `MlpPolicy` and trains for 10,000 timesteps. |
| `phase1_Resnet/vehicle_driver.py` | Webots vehicle controller; pretrained ResNet-18 weights | Loads a PPO checkpoint if present, otherwise creates a PPO agent, then trains. |
| `phase2_CNN/CNN_Model_Generater.ipynb` | Jupyter environment, image files in `phase2_CNN/images` | Explores/exports a CNN model. The generated `.h5` file itself was **not** in the archive. |
| `phase2_CNN/train.py` | Webots vehicle controller; `small_cnn_model.h5` | Camera + LiDAR observations, PPO training; saves a policy named `mlp_model_phase2_ppo_policy`. |
| `phase2_CNN/test.py` | Saved model and Webots controller | Loads `mlp_model_phase2_ppo_policy` and evaluates/runs the policy. |
| `phase2_Resnet/vehicle_driver.py` | Webots controller; pretrained ResNet-18 weights | Uses two action dimensions and PPO. |
| `phase3_Resnet/worlds/highway_overtake.wbt` | Webots + SUMO; Python and native controller resources | Highway overtaking simulation world with supervisor, sensors, robot windows and controller source. |

> The paths and training counts above describe **existing source-code defaults**, not verified performance or recommended experiment budgets.

## Suggested local workflow

1. Install a compatible Webots version, and SUMO if using the highway/overtaking stage.
2. Create a virtual environment and install `requirements.txt` in the interpreter Webots will use.
3. Open the supplied phase 3 `.wbt` world to inspect device and controller configuration, or set up a suitable Webots vehicle world for earlier phases.
4. Generate/provide CNN `.h5` features or fetch appropriate ResNet weights as required by the chosen script.
5. Run the script through the **Webots controller runtime**. Verify camera, GPS, LiDAR and emitter/receiver names and their enable intervals before attempting learning.
6. Collect stable-baselines checkpoints, episode rewards, safety events, and seeds into an ignored experiment-results directory for reproducibility.

For buildable native plugins, see the `Makefile` files under `phase3_Resnet/plugins/` and `phase3_Resnet/controllers/radar_target_tracker/`. Prebuilt `.so`/executable outputs and Python bytecode were intentionally omitted from Git.

## Static checks

`python -m unittest discover -s tests -v`

This is a source-integrity check only. It does not require Webots or large ML frameworks.
