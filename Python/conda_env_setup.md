conda create -n ml-env python=3.8
conda activate ml-env
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install numpy pandas scikit-learn pytorch-lightning optuna tensorboard matplotlib seaborn

<!-- Additional action -  -->
From the image and the %PATH% environment variable you've shared, I can see that several paths may contain libiomp5md.dll based on the locations you've provided and the files on your system.

Here are the potential paths in %PATH% where libiomp5md.dll could be located:

Paths from %PATH% containing potential conflicts:
C:\Users\nafta.conda\envs\py38\Library\bin
This path is directly listed in your %PATH% and contains a version of libiomp5md.dll as shown in your image.

C:\ProgramData\anaconda3\Library\bin
This is another directory where a libiomp5md.dll might be present, depending on the base environment setup. You should check the C:\ProgramData\anaconda3\Library\bin folder.

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
While this folder typically contains CUDA-specific libraries, it’s possible that additional runtime libraries like libiomp5md.dll could also be loaded.

C:\Program Files (x86)\Microsoft Visual Studio...
The Microsoft Visual Studio directories often contain runtime libraries, including OpenMP runtimes like libiomp5md.dll.

C:\Users\nafta\AppData\Roaming\Python\Python311\site-packages\torch\bin
This folder is shown in the image you provided and contains a version of libiomp5md.dll.

To resolve potential conflicts:
Identify the Active libiomp5md.dll: You can use a tool like Process Explorer to see which libiomp5md.dll is actually being loaded when you run your Python script. This will help you identify if there are conflicting versions being loaded.

Remove Duplicates from %PATH%:

You can temporarily remove some of the conflicting paths that contain libiomp5md.dll from your %PATH% variable. For instance, removing paths like C:\ProgramData\anaconda3\Library\bin or C:\Users\nafta\.conda\envs\py38\Library\bin and testing which one works without conflict.
You can modify your %PATH% variable to ensure only the required version of libiomp5md.dll is loaded. For example, temporarily unset these paths from your command line using:
bash
Copy code
set PATH=C:\ProgramData\anaconda3\Scripts;%PATH%
Try the Environment Variable Fix: As mentioned previously, setting the environment variable KMP_DUPLICATE_LIB_OK=TRUE may allow your program to proceed without crashing, though it’s a workaround.

Let me know if you need further clarification or assistance with this!


a. Save the Current Environment
    conda env export --name ml_env > ml_env.yml

b. Duplicate the Environment
    conda env create --name ml_env_copy --file ml_env.yml

c. Clone the Environment Directly
    conda create --name ml_env_copy --clone ml_env

d. To remove the ml_env_copy environment, you can use the following command:
    conda env remove --name ml_env_copy

e. To log both standard output (stdout) and error output (stderr) to the same file while running the command:
    Linux:
    conda create --name ml_env_copy --clone ml_env |& tee output.txt

    CMD:
    conda create --name ml_env_copy --clone ml_env > output.txt 2>&1
