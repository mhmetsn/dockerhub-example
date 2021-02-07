# DevOps

Software development and operations approach that enables faster development of new products and 
easier maintenance of existing deployments

## CI/CD Pipeline for simple Python Flask Service

This is a teaching app displaying name and message in different formats for the course of SBAT about
of Continuous Integration, Continuous Delivery and Continuous Deployment (DevOps) in WSB university.

### Technologies and platforms used:

1. [Python](https://www.python.org/) [[Flask](https://flask.palletsprojects.com/en/1.1.x/), [pytest](https://docs.pytest.org/en/stable/index.html)]
2. [Git](https://git-scm.com/)
3. [GitHub](https://github.com/)
4. [Travis-CI](https://travis-ci.com/)
5. [Docker](https://www.docker.com/)
6. [Docker-Hub](https://hub.docker.com/)

<!--
# 7. [Heroku](https://www.heroku.com/) (Not needed for students))
-->

## Web Service
### Python Web Service with Flask
- <b>(Optional)</b> In the project, if you want you can use a virtual environment to create a hermetic environment for the application:

  ```
  # create a hermetic environment for application libraries:
  $ python3 -m venv .venv

  # activating the hermetic environment
  $ source .venv/bin/activate
  ```
  
- Independently if you use a virtual environment (in that case continue after the previous commands) or the base one, you can
  install the libraries in the following way:
  ```
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # Check
  $ pip list
  ```

  Check out: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) and [flask library](http://flask.pocoo.org).

- Running the application:
  ```
  # as a regular program
  $ python main.py

  # or:
  $ PYTHONPATH=. FLASK_APP=app.py flask run
  ```
  
- By continuing to work with the project, activating and deactivating the hermetic environment for py application:
  ```
  # deactivation
  $ deactivate
  ```

## Continuous Integration
### Test Automation
- Running tests (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test --verbose -s
  
  # or:
  $ python3 -m pytest -v test/
  ```
  
  It should display something like:
  ```
  (base) user@pc:~/Projects/printerService$ python3 -m pytest -v test/
  ============================== test session starts ===========================================
  platform linux -- Python 3.8.3, pytest-6.2.1, py-1.9.0, pluggy-0.13.1
  rootdir: /home/Projects/printerService
  collected 7 items
  
  test/test_formater.py::Test_Formater::test_plain_uppercase PASSED                       [ 14%]
  test/test_formater.py::Test_Formater::test_plain_text PASSED                            [ 28%]
  test/test_formater.py::Test_Formater::test_get_formatted PASSED                         [ 42%]
  test/test_views.py::Test_Flask_Views::test_output PASSED                                [ 57%]
  test/test_views.py::Test_Flask_Views::test_outputs PASSED                               [ 71%]
  test/test_views.py::Test_Flask_Views::test_form PASSED                                  [ 85%]
  test/test_views.py::Test_Flask_Views::test_mult PASSED                                  [100%]
  ============================= 7 passed in 0.09s ==============================================
  ```

  ```
  ...
  ```

### Version Control System with git and GitHub
Create an account in [GitHub](https://github.com/) and a new remote repository in which you will be working. 

The following example URLs are specific for this repo, if you would like to work with your own repository 
you could substitute them for:
```
               https://github.com/[user_name]/[name_repo].git [branch_name]
```
Also note that you can use another protocol like ssh, instead of https.
#### Initialize repo
###### Initialize local repo from already created remote repo (GitHub)
To initialize a local repo from a remote repo we need to clone the remote repo.

```
git clone https://github.com/josejuanWSB/test_repo.git master
```

###### Initialize a remote repo from already created local project (in your pc)
To initialize a remote repo in GitHub from a local repo we need to: 

1. Create the repo in GitHub 
2. Initialize local repo
   ```
   git init
   ```
   
#### Push changes to remote repo
It makes all the changes in the local repo be in the remote repo in GitHub

1. Stage all the files:
   
   ```
   git add .
   ```
    _"." is a key for all the files in the directory_
   
2. Reflect the changes in the local repository (.git directory)
   
   ```
   git commit -m "First Commit"
   ```
   
3. Push the changes to the remote repository
   
    ```
    git push https://github.com/josejuanWSB/test_repo.git master
    ```

#### Pull changes
It synchronizes the remote repo in GitHub to the local repo, making available the last changes made in 
the remote repo to the local repo.

To try it you can change something in the remote repo by the GitHub editor (right corner inside a file)
or someone of your team can make changes and then you can make a pull.

```
git pull https://github.com/josejuanWSB/test_repo.git master
```
    
    
#### Git merge/solving conflicts

When two developers have introduced changes in the same line of code this can generate problems, 
called conflicts.

I. Try to pull:

```
git pull https://github.com/josejuanWSB/test_repo.git master
```


II. If it fails, then first you need to add and reflect the changes in your local repo and then try to pull again:
   ```
   git add .
   git commit -m "Committing on local repo"
   git pull https://github.com/josejuanWSB/test_repo.git master
   ```
<i>If meanwhile pulling it prompts the vi/unix command line editor, don't panic and press 
-> :wq (save and exit)</i>

III. If there is a conflict, that needs to be solved manually then:

1. Go to the file and delete the comments that have been generated by git, and the code that you 
   considered not needed.
2. Then push the changes again:
   ```
   git add .
   git commit -m "Conflict resolved"
   git push https://github.com/josejuanWSB/test_repo.git master
   ```
3. If the conflict has been solved, now when you try to git pull, it will display: <i>"Already up to date"</i>

### Continuous Integration with TravisCI:

1. Sign in [Travis-CI](https://travis-ci.com/) with GitHub account
2. Make a .travis.yml file in the base directory with a basic configuration like:
  ```
  language: python
  python:
    - "3.8"
  install:
  - pip install -r requirements.txt
  - pip install -r test_requirements.txt
  script:
  - python -m pytest -v
  ```
3. Trigger a build by pushing changes to the repo or manually by the button trigger build.
4. Check the build success and if the tests passed.

### Deployment with Docker:
  First you need to set the port of Flask to use a different port than the one by default
  main of your Flask service as follows:
  ```
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80)
  ```
  Build the image from the Dockerfile
  ```
  $ docker build -f Dockerfile -t name_img .
  ```
  Run the image -d = detach (run on background), -p = publish ports, image_name.
The app will accessible by the URL http://0.0.0.0:8000/
  ```
  $ docker run -p 8000:80 --name name_container name_img:latest
  ```
  In case that you will have problems, and you need to debug your app
  -ti = terminal interactive -> /bin/sh is a terminal that you can open inside the container
  ```
  $ docker container run -ti printer_local:latest /bin/sh
  ```

#### Containers cleaning
To additionally remove any stopped containers and all unused images (not just dangling images), 
add the -a flag to the command:
  ```
  $ docker system prune -a
  ```
Use the docker images command with the -a flag to locate the ID of the images you want to remove. This will show you every image, including intermediate image layers. When you’ve located the images you want to delete, you can pass their ID or tag to docker rmi:

List images to remove:
  ```
  $ docker images -a
  ```
Remove:
  ```
  $ docker rmi image_name
  ```
## Auxiliar Information
### A Note for Windows Users
This project was implemented from a Linux/UNIX based perspective, but everything can be made to work in 
Windows with very little effort.

- Unix Variables:
  ```
  export MY_VAR=test
  echo ${MY_VAR}
  ```

- Windows 10 Variables (powershell):
  ```
  $env:my_var = "test"
  Get-ChildItem Env:my_var
  ```

## Docker Installation
### Ubuntu

- Docker Installation: [docker howto](https://docs.docker.com/engine/install/ubuntu/)

### Windows10

On the Windows platform make sure that you are running in LinuxContainer mode.
- Docker Installation: [docker howto](https://docs.docker.com/docker-for-windows/install/)
### Others
- Docker Installation: [docker install](https://docs.docker.com/engine/install/)

### Centos

- Docker Installation:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```
