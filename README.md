# coreference_resolution_api : Production Ready Code


## About  
This is a project developed to create a code template for coreference resolution production ready api.    
Please note that model training is not done in this project.We've just used coreferee library and processed it's output.   


The basic code template for this project is derived from my another repo <a href="https://github.com/sarang0909/Code_Template">code template</a> 


### Requirement

Create coreference resolution api which accepts text data and resolves coreferences among entities.   
   
 
### Inference   
There are 2 ways to deploy this application.   
1. API using FastAPI.
2. Streamlit application

### Testing     
Unit test cases are written   

### Deployment 
Deployment is done locally using docker.   


## Code Oraganization   
Like any production code,this code is organized in following way:   
1. Keep all Requirement gathering documents in docs folder.       
2. Write and keep inference code in src/inference.   
3. Write Logging and configuration code in src/utility.      
4. Write unit test cases in tests folder.<a href="https://docs.pytest.org/en/7.1.x/">pytest</a>,<a href="https://pytest-cov.readthedocs.io/en/latest/readme.html">pytest-cov</a>    
5. Write performance test cases in tests folder.<a href="https://locust.io/">locust</a>     
6. Build docker image.<a href="https://www.docker.com/">Docker</a>  
7. Use and configure code formatter.<a href="https://black.readthedocs.io/en/stable/">black</a>     
8. Use and configure code linter.<a href="https://pylint.pycqa.org/en/latest/">pylint</a>     
9. Use Circle Ci for CI/CD.<a href="https://circleci.com/developer">Circlci</a>    
 
Clone this repo locally and add/update/delete as per your requirement.   
 
## Project Organization


├── README.md         		<- top-level README for developers using this project.    
├── pyproject.toml         		<- black code formatting configurations.    
├── .dockerignore         		<- Files to be ognored in docker image creation.    
├── .gitignore         		<- Files to be ignored in git check in.    
├── .circleci/config.yml         		<- Circleci configurations       
├── .pylintrc         		<- Pylint code linting configurations.    
├── Dockerfile         		<- A file to create docker image.    
├── environment.yml 	    <- stores all the dependencies of this project    
├── main.py 	    <- A main file to run API server.    
├── main_streamlit.py 	    <- A main file to run API server.  
├── src                     <- Source code files to be used by project.    
│       ├── inference 	        <- model output generator code   
│       ├── training 	        <- model training code  
│       ├── utility	        <- contains utility  and constant modules.   
├── logs                    <- log file path   
├── config                  <- config file path   
├── docs               <- documents from requirement,team collabaroation etc.   
├── tests               <- unit and performancetest cases files.   
│       ├── cov_html 	        <- Unit test cases coverage report    

## Installation
Development Environment used to create this project:  
Operating System: Windows 10 Home  

### Softwares
Anaconda:4.8.5  <a href="https://docs.anaconda.com/anaconda/install/windows/">Anaconda installation</a>   
 

### Python libraries:
Go to location of environment.yml file and run:  
```
conda env create -f environment.yml
```

 

## Usage
Here we have created ML inference on FastAPI server with dummy model output.

1. Go inside 'coreference_resolution_api' folder on command line.  
   Run:
  ``` 
      conda activate coreference_resolution_api  
      python main.py       
  ```
  Open 'http://localhost:5000/docs' in a browser.
![alt text](docs/fastapi_first.jpg?raw=true)
 
2. Or to start Streamlit application  
5. Run:
  ``` 
      conda activate coreference_resolution_api  
      streamlit run main_streamlit.py 
  ```  


 
### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
      pytest --cov-report html:tests/cov_html --cov=src tests/ 
  ```
 
### Performance Testing
1. Open 2 terminals and start main application in one terminal  
  ``` 
      python main.py 
  ```

2. In second terminal,Go inside 'tests' folder on command line.
3. Run:
  ``` 
      locust -f locust_test.py  
  ```

### Black- Code formatter
1. Go inside 'coreference_resolution_api' folder on command line.
2. Run:
  ``` 
      black src 
  ```

### Pylint -  Code Linting
1. Go inside 'coreference_resolution_api' folder on command line.
2. Run:
  ``` 
      pylint src  
  ```

### Containerization
1. Go inside 'coreference_resolution_api' folder on command line.
2. Run:
  ``` 
      docker build -t myimage .  
      docker run -d --name mycontainer -p 5000:5000 myimage         
  ```


### CI/CD using Circleci
1. Add project on circleci website then monitor build on every commit.




## Contributing
Please create a Pull request for any change. 

## License


NOTE: This software depends on other packages that are licensed under different open source licenses.

