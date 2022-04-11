# A minimal starting point for rapid prototyping interactive Human-AI tools

Just a quick connection of the huggingface pipeline for sentiment analysis (see [here](https://github.com/huggingface/transformers#quick-tour-of-pipelines)) with a 
small visual interface made with [D3js](https://d3js.org/).

by [Hendrik Strobelt](http://hendrik.strobelt.com) ([MIT-IBM Watson AI Lab](https://mitibmwatsonailab.mit.edu/))

<div style="text-align:center"><img src="sentimenter.gif" width=400/></div>


## Perequisits
Create new Conda environment:
```
conda create -n hugging python=3.6
conda activate hugging
```

install flask:
```
conda install -c anaconda flask
```

install huggingface (and pytorch):
```
conda install pytorch -c pytorch
pip install transformers
```

## Run

```
conda activate hugging
python server.py
```

visit [http://localhost:8888](http://localhost:8888)
