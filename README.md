Text_Processing_U.She
=========================
**Text Processing which is based on the class in the University of Sheffield.**

[toc]



<img src="./pictures/NLP-wordcloud.png" alt="logo" style="zoom: 50%;" />

![](/Users/doheras/Desktop/Text Processing/Text_Processing_U.She/pictures/University-of-Sheffield-2010.jpg) 

# 1.Enviroment Configuration

## 1.1 How to quickly import the Anaconda environment

1. Move to your directory where the `$directory` you want to install and copy the `textprocessing.yml` and `requirement.txt` from the `anaconda` folder into your current terminal path. Then, follow the instruction below: 
```shell
$ conda env create -f textprcessing.yml
$ pip install -r requirement.txt
```
2. If you wish to use your own name for your env, follow these instruction below:
```shell
$ conda create --name <YOUR ENVIRONMENT NAME> --clone textprocessing
# Please make sure you don't have env with same name
$ conda remove --name textprocessing --all
```


##1.2 Build Your Customized Jupyter Notebook Env by Anaconda

1.Install ipykernel on your env

```shell
$ conda install -n <YOUR ENVIRONMENT Name> ipykernel
```
2.Activate and Enter the env

```shell
$ source ~/.bash_profile
$ source activate <YOUR Environment Name>
```
3.Write the environment to the kernel of the Jupyter Notebook

```shell
(<env name>)> python -m ipykernel install --user --name <env name> --display-name "<display env name>"
```
4.Open the Jupyter Notebook

```
(<env name>)> jupyter notebook
```

# 2 Repository File Structure

|-- Text Processing
    |-- .DS_Store
    |-- README.md
    |-- directoryList.md
    |-- Assignment
    |   |-- Document_Retrieval_Assignment_1920.pdf
    |   |-- Document_Retrieval_Assignment_Files.zip
    |   |-- Report.docx
    |   |-- assignment_ipynb.zip
    |   |-- Document_Retrieval_Assignment_Files
    |   |   |-- cacm_gold_std.txt
    |   |   |-- documents.txt
    |   |   |-- eval_ir.py
    |   |   |-- example_results_file.txt
    |   |   |-- index_nostoplist_nostemming.txt
    |   |   |-- index_nostoplist_withstemming.txt
    |   |   |-- index_withstoplist_nostemming.txt
    |   |   |-- index_withstoplist_withstemming.txt
    |   |   |-- ir_engine.py
    |   |   |-- my_retriever.py
    |   |   |-- queries.txt
    |   |   |-- queries_nostoplist_nostemming.txt
    |   |   |-- queries_nostoplist_withstemming.txt
    |   |   |-- queries_withstoplist_nostemming.txt
    |   |   |-- queries_withstoplist_withstemming.txt
    |   |   |-- result.txt
    |   |   |-- script.sh
    |   |   |-- show.txt
    |   |   |-- __pycache__
    |   |       |-- my_retriever.cpython-37.pyc
    |   |-- Form_doc
    |       |-- Scheme.docx
    |-- Exercise
    |   |-- Lab1
    |   |   |-- NEWS.zip
    |   |   |-- compare.py
    |   |   |-- lab1.pdf
    |   |   |-- stop_list.txt
    |   |-- Lab2
    |   |   |-- training_data.txt
    |   |   |-- POSTAG_DATA.zip
    |   |   |-- lab2.pdf
    |   |   |-- postagger_STARTER_CODE.py
    |   |   |-- test_data.txt
    |   |-- Lab3
    |       |-- lab3.pdf
    |       |-- lab3.py
    |       |-- mobydick.txt
    |       |-- pic1.png
    |       |-- pic2.png
    |       |-- pic3.png
    |-- pictures
        |-- NLP-wordcloud.png
        |-- University-of-Sheffield-2010.jpg








