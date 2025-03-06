# initialize Selenium support in our conda selenium environment (with Python 3.11)

1. create an anaconda env named "selenium" with python v3.10
   conda create --name selenium python=3.10 -y

   Fallback:
    a. Deactivate the environment (if it is currently activated): 
       conda deactivate

    b. Delete the environment:
       conda remove --name selenium --all -y

2. activate selenium environment
   conda activate selenium

3. pip install -r requirements.txt 
   
   If wanting to automate the y answer:
   powershell -Command "echo y | pip install -r requirements.txt"

4. If wanting to support pytest:
   powershell -Command "echo y | pip install -r pytest-requirements.txt"

5. After resolving all dependencies, Generate the updated requirements.txt file:
   pip freeze > all-requirements.txt


Misc - 
1. Update pip and setuptools 
   python.exe -m pip install --upgrade pip setuptools


2. Installing Anaconda env on ubuntu (WSL)
   a. wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh
   b. bash Anaconda3-2024.06-1-Linux-x86_64.sh
   c. Update ~/.bashrc with 'conda init' command
   d. source ~/.bashrc
   e. Verify the Installation
      conda --version
   f. Update Anaconda
      conda update conda && conda update anaconda

