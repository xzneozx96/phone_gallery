////         INSTALL PYTHON3          ////
1. sudo apt update
2. sudo apt install software-properties-common
3. sudo add-apt-repository ppa:deadsnakes/ppa
4. sudo apt update
5. sudo apt install python3.8


////         INSTALL PIP3          ////
1. sudo apt update
2. sudo apt install python3-pip


////         INSTALL VIRTUALENV          ////
1. sudo pip3 install virtualenv


////         RUN SERVER          ////
1. Redirect to server/code folder
2. Create virtual environment named "env" in this repo:

  virtualenv env

3. Start virtual environment

  ./venv/bin/activate

4. Install packages from requirements.txt to virtual environment

  pip3 install -r requirements.txt

5. Run server

  flask run
