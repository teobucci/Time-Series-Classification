![GitHub last commit](https://img.shields.io/github/last-commit/teobucci/Time-Series-Classification?logo=github)

# Time Series Classification

This project was developed for the course of **Artificial Neural Networks and Deep Learning** for the MSc. in Mathematical Engineering at Politecnico di Milano, A.Y. 2022/2023.

## Description

```
.
├── README.md
├── misc
│   ├── report_material
│   ├── submission_template
│   │   ├── metadata
│   │   ├── model.py
│   │   ├── model_aug.py
│   │   └── scaler.gz
│   └── training_histories
├── notebook
│   ├── final_model.ipynb
│   ├── utils
│   │   ├── augmentation.py
│   │   ├── datasets.py
│   │   ├── dtw.py
│   │   ├── helper.py
│   │   ├── input_data.py
│   │   ├── models.py
│   │   ├── nemenyi.py
│   │   └── prototype_selection.py
│   ├── x_train.npy
│   └── y_train.npy
├── report
│   ├── bibliography.bib
│   ├── report.pdf
│   └── report.tex
└── requirements.txt

7 directories, 49 files

```

- [`final_model.ipynb`](notebook/final_model.ipynb) is the main file that performs training of all the models and produces all the output images.
- [`report_material`](misc/report_material) and [`training_histories`](misc/training_histories) are folders containing additional images, namely the plots of the different training histories of the various models.
- [`submission_template`](misc/submission_template) contains the code used to submit the model in the competition.
- `x_train.npy` and `y_train.npy` are the given dataset.
- [`utils`](notebook/utils) contains the code to perform data augmentation.
- [`requirements.txt`](requirements.txt) contains the necessary packages for the environment.

## Authors

- Paolo Botta ([@ploki99](https://github.com/ploki99))
- Teo Bucci ([@teobucci](https://github.com/teobucci))
- Silvia Caresana ([@silviacaresana](https://github.com/silviacaresana))

## Output

Check out the final [`report.pdf`](./report/report.pdf).

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)