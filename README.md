# Problem Description

The input is sets of images containing 5 types of fruit. Create a model using Tensorflow to categorize image.

The dataset has 5 types of fruit:
- Ambarella
- Grapefruit
- Jackfruit
- Orange
- Starfruit

This dataset was collected by hand by my friend - Tran Tien Duc Bo

# Instruction
To run `notebook.ipynb`:
- Install [Tensorflow](https://www.tensorflow.org/install/pip#windows-native).
- Matplotlib
- Scipy

If you need the model, you have to run codeblocks in:
- Library
- Data Preparation
- Checkpointing
, this will create a best model.

# Serving

After creating a best model, we need to serve it.

## Convert h5-Keras to TF model

**Important:** Change variable to your best model name in convertKerasToTF.py

To convert it, open CMD and `python deploy/TF_Image/convertKerasToTF.py`

To check input and output of the model, open your cmd and type `saved_model_cli show --dir . --tag_set serve --signature_def serving_default > saved_model_cli.txt`

Check `saved_model_cli` at `deploy/model/saved_model_cli.txt`.

## Containerize

```sh
cd deploy/TF_Image
docker build -t capstone1_model .
docker run -it --rm -p 8500:8500 capstone1_model
```

To run prediction, go to `deploy/TF_Image/test_prediction.ipynb`

