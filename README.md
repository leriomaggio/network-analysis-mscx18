# Network Analysis Tutorial using Python & `networkx`

## MSCX Ph.D. Summer School, Salina (ME) - Italy

<img src="images/mscx_logo.png" width="25%" >

### Author: Valerio Maggio

### _PostDoc Data Scientist @ FBK/MPBA_

## Contacts:

<table style="border: 0px; display: inline-table">
    <tbody>
        <tr style="border: 0px;">
            <td style="border: 0px;">
                <img src="images/twitter_small.png" style="display: inline-block;" /> 
                <a href="http://twitter.com/leriomaggio" target="_blank">@leriomaggio</a>
            </td>
            <td style="border: 0px;">
                <img src="images/gmail_small.png" style="display: inline-block;" /> 
                <a href="mailto:vmaggio@fbk.eu">vmaggio_at_fbk_dot_eu</a>
            </td>
       </tr>
  </tbody>
</table>


## Get Started

### Binder

(Consider this option only if your WiFi is stable)

If you don't want the hassle of getting setup, you can use the Binder service to participate in the live tutorial. Just click on the button below:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/leriomaggio/network-analysis-mscx18/master)

## Set up the Environment

### 1. Clone this repo

<img src="images/github.jpg" />

```
git clone https://github.com/leriomaggio/network-analysis-mscx18.git
```

### 2. Install Requirements

This tutorial will use **Python 3**

This tutorial requires the following packages:

- Python version 3.6
    - Python 3.4+ should be fine as well
    - likely Python 2.7 would be also fine, but *who knows*? :P

- `matplotlib==2.2.3`
- `networkx==2.1`
- `pandas==0.23.0`
- `hiveplot==2017.10.17.21.7`
- `nxviz==0.5.0`
- `numpy==1.14.3`
- `jupyter==1.0.0`
- `scipy==1.1.0`
- `python-louvain==0.11`
- `bokeh==0.13.0`

#### Easiest way: Anaconda Distribution of Python

If you have the Anaconda distribution of **Python 3** installed on a Unix-like machine (Linux, macOS, etc.), then run `make conda`, which wraps the commands below.

1. `$ conda env create -f environment.yml`
2. `$ source activate nams`
3. `$ python checkenv.py`

If you do not have the Anaconda distribution, I would highly recommend getting it for 
[Windows][1], [Mac][2] or [Linux][3]. It provides an isolated Python computing environment 
that will not interfere with your system Python installation, and comes with a very 
awesome package manager (`conda`) that makes installation of new packages a single `conda 
install pkgname` away.

#### Alternative to Anaconda: `pip install`

For those who do not have the capability of installing the Anaconda Python 3 distribution on their computers, please follow the instructions below.

Run `make venv`, which wraps up the commands below. 

1. Create a virtual environment for this tutorial, so that the installed packages do not mess with your regular Python environment.
2. `$ pip install virtualenv`
3. `$ virtualenv mscx`
4. `$ source mscx/bin/activate`
5. `$ pip install matplotlib networkx pandas hiveplot numpy jupyter`

#### Check your environment:

1. `$ python checkenv.py`

### Run the Jupyter Notebook

    $ jupyter notebook
    

## Dataset References

1. [Divvy Data Challenge](https://www.divvybikes.com/datachallenge)
1. [Konect Network Analysis Datasets](http://konect.uni-koblenz.de/networks/)

## Resources

1. Jon Charest's use of Circos plots to visualize networks of Metal music genres. [blog post][5] | [notebook][6]
1. Gain further practice by taking this course online at [DataCamp](http://www.datacamp.com/)!
1. A gentle introduction to graph theory on [Vaidehi Joshi's website](https://dev.to/vaidehijoshi/a-gentle-introduction-to-graph-theory)

[1]: http://repo.continuum.io/archive/Anaconda3-4.0.0-Windows-x86_64.exe
[2]: http://repo.continuum.io/archive/Anaconda3-4.0.0-MacOSX-x86_64.pkg
[3]: http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh

    
 
