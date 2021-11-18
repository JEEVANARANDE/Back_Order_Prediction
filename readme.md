create env
```bash
conda create -n Back_Order python=3.7 -y
```
activate env
```bash
conda activate Back_Order
```
created a req file

install the req
```bash
pip install -r requirements.txt
```
```bash
git init
```
```bash
dvc init
```
To track our data
```bash 
dvc add data_given/data_BackOrder_cassandra.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
```bash
git remote add origin https://github.com/JEEVANARANDE/Back_Order_Prediction.git
```
```bash
git add . && git commit -m "Update_Readme.md" && git push -u origin main
```