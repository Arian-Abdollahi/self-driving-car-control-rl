# Architecture and source integrity notes

## Source and preservation

The starting point was the user-provided `Self-Driving-Car-Control-RL--main (1).zip`. All original editable Python/C/C++/JavaScript code, XML, world, notebook and image assets were retained in their **original phase-relative locations**. The original short README was replaced by a more detailed repository README. Generated `.pyc` caches, platform-specific `.so` libraries, and the built radar tracker executable were omitted from Git because their corresponding source and build instructions exist.

No attempt was made to fabricate model files, weights, training results, success rates, or simulator test outcomes. One original script had a syntax error: the stray trailing `y` after `total_reward -= 10 * blue_distance` at `phase2_Resnet/vehicle_driver.py:403` was removed to make it parse. No other source algorithm was rewritten. The tests check syntax/structure, not runtime behavior.

## Core methods found in the code

- **Control policy**: `stable_baselines3.PPO` with `MlpPolicy` appears in all main learning stages.
- **Simulation**: `vehicle.Driver` and the Webots `controller` API are used in the phase scripts.
- **Image perception**: phase 1 and phase 2 CNN scripts load TensorFlow/Keras CNN models; ResNet scripts use `torchvision` ResNet-18 without its final classification layer.
- **Other sensing**: camera and GPS are initialized; LiDAR is present in later phase scripts; the final world uses distance sensors and supervisor control.
- **Action space**: phase 1 CNN uses one normalized action; later scripts define two-dimensional steering/speed actions with different bounds. Inspect each `WebotsEnv` for actual reward/transition logic.
- **Highway simulation**: phase 3 includes `.wbt` world, SUMO route/network XML, supervisor and overtaking controller, and robot-window components. Several included support files have Cyberbotics upstream notices.

## What was not provided

- PPO checkpoint `.zip` files saved by the scripts.
- CNN `.h5` files referenced by the training/test scripts.
- Original environment/version specifications or reproducible random seeds.
- Experiment logs or measured lane/obstacle/overtaking evaluation metrics.

### Known technical debt

1. The scripts instantiate Webots `Driver` and access devices at module load time, making direct offline unit testing difficult.
2. Stage-specific device names and file paths are mostly hardcoded.
3. Some dependencies use internal or older library APIs such as `keras.src.legacy` and `resnet18(pretrained=True)`.
4. The same perception/utilities logic is duplicated between phases. It can be modularized later with simulator-based regression tests, rather than risking unverified behavior changes now.
5. The included highway world and SUMO assets must be tested against a specific Webots/SUMO installation.
