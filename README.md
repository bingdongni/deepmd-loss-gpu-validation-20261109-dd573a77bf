# DeePMD loss schedule validation

The [GitHub Actions run](https://github.com/bingdongni/deepmd-loss-gpu-validation-20261109-dd573a77bf/actions/runs/42560524436) compares DeePMD-kit commit `7a7a13dfcb8e6c5f653852fcc4b26280f0932952` with upstream baseline `5485b3abccb221a304af5630545e02fd90d272f0`.

The `cuda-loss` job uses an NVIDIA GeForce RTX 4060 Laptop GPU for PyTorch loss and gradient checks and CPU for Paddle. An import adapter supplies a generated configuration and bypasses package initializers; no DeePMD native extension or end-to-end training is exercised in this job. The baseline had 74 failing PyTorch cases and 26 failing Paddle cases; the patch passed all 104 PyTorch and 36 Paddle cases.

The `linux-package` job builds and installs the project on Ubuntu, runs `dp --version`, and runs the same regression files on CPU without the import adapter. The [GPU log](gpu-validation.log) and [Linux log](linux-validation.log) contain the checks.
