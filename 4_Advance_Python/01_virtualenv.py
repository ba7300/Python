
                # ** Virtual Environment **
'''
*) Def : 
    An environment which is same as the system interpretor but is isolated from other python 
    environments on the system.
        
*) Installation :

- To use Virtual Environment, we write:

    "pip install virtualenv"                   ---> # Install the Package

- We create new environment using : 

    "virtualenv myprojectenv"                 ----> # create a new Virtual environment


- The new step after creating virtual environment is to activate it.
    #for Linux users  : source myprojectenv/bin/activate

    #for Windows users  : .\myprojectenv\Scripts\activate.ps1 


- We can now use this virtual environment as a separate python installation.


*) "pip freeze" command :
- 'pip freeze' retrurns all the packages installed in a given python environment along with the versions.

- " pip freeze > .\requirements.txt "
  The above command creates a file named 'requirements.txt' in the same directory containing the output of pip freeze.


- We can distribute this file to other users and they can recreate the same evironment using : 
    " pip install -r .\requirements.txt "

'''
 