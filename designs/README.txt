APPLICATION IS NOT INTENDED FOR DEVICES USING TENSORFLOW CPU, 
RECOMMENDED TO HAVE GPU(NVIDIA) IN ORDER TO RUN THE APPLICATION WITHOUT PROBLEMS. 


Creating an executable file wasn't possible.Therefore,
you have to create a virtual environment with python version 3.5

I will list the steps assuming you have python and anaconda installed on your device (TENSORFLOW CPU):

1. Open command prompt 
2. Conda create -n environment_name python=3.5	#Creates virtual environment with python version needed 
3. activate environment_name			#Activates virtual environment
4. pip install -r requirements.txt     		#Contains all packages needed to run the applicatio, only has to be done once 
5. python implem.py 				#Runs the application


These are the steps to installing tensorflow CPU however this will cause the application to be extremely slow and the application might not work at times. 
Downloading TENSORFLOW-GPU instead will get rid of these problems. The application was created with the intentions of being utilised by the GPU not CPU.


This video will help you install the required extra packages for tensorflow GPU: https://www.youtube.com/watch?v=KZFn0dvPZUQ

If the video has been followed correctly, 

replace step 4 with pip install -r requirements-gpu.txt


