# Instructions to Run Airflow In WSL2

# Update Packages
```
sudo apt update
```
# Install Pip
```
sudo apt install python3-pip
```
# Create Python Virtual Environment and activate

```
sudo apt install python3.10-venv

python3 -m venv airflow_env

source airflow_env/bin/activate
```
# Airflow Setup 

```
mkdir airflow

vi ~/.bashrc

#add following #AIRFLOW_HOME=/mnt/c/Users/username/Documents/airflow	

export AIRFLOW_HOME= <Wsl airflow path >

cd $AIRFLOW_HOME

pip3 install apache-airflow 

airflow db init

mkdir dags

airflow users create --username airflow --password airflow --firstname your_first_name --lastname your_last_name --role Admin --email your_email@some.com

airflow users list

```

# To Install Airflow and run scheduler ,open new terminal and  run following commands

```
source airflow_env/bin/activate

cd $AIRFLOW_HOME

airflow scheduler 
```

# To run webserver Open Another terminal and run following commands

```
source airflow_env/bin/activate

cd $AIRFLOW_HOME

airflow webserver
```
 
