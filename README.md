# ViT
Image Classification with Vision Transformer

## Introduction:
Image classification is a fundamental task in computer vision that involves identifying the contents of an image and assigning it to one of several predefined categories. Traditional approaches to image classification, such as convolutional neural networks (CNNs), have shown excellent performance on many tasks. However, recent research has shown that a new approach, called Vision Transformer (ViT), can achieve state-of-the-art performance on many benchmark datasets.



## What is Vision Transformer?
Vision Transformer is a type of neural network architecture that applies the transformer model, which was originally designed for natural language processing (NLP) tasks, to image classification tasks. In traditional convolutional neural networks (CNNs), the image is processed by a series of convolutional layers and pooling layers, followed by a fully connected layer for classification. However, in Vision Transformer, the image is first divided into small patches, which are then flattened and fed into a transformer network for classification.

<img width="546" alt="image" src="https://github.com/raviteja1234567/ViT/assets/20350567/1491d73d-ade1-407b-bc86-f98ba7d75598">

## Dataset used
- Name: Gameplay images (Bingsu/Gameplay_Images)
- Length: 10000
- Data fields: A PIL image and Classification label

![image](https://github.com/raviteja1234567/ViT/assets/20350567/644885df-3a91-4054-9e1d-9504a49d0b6d)
![image](https://github.com/raviteja1234567/ViT/assets/20350567/b68caf80-52b7-429d-8e8a-de764931aa89)
![image](https://github.com/raviteja1234567/ViT/assets/20350567/487b16ab-ab18-426b-8637-bab3a56bf350)

## Training
Pre-trained model used: google/vit-base-patch16-224-in21k

Training parameters:

- Epochs=4
- Training steps=100
- Evaluation steps=100
- Learning rate=2e-4

## Conclusion
- ViT offers scalability, computational efficiency, transferability, and interpretability over CNN.

- ViT's attention mechanism allows it to capture long-range dependencies.

- ViT has lesser number of computations.

- Pretrained ViT models for image classification tasks requires less number of iterations.

- ViT > VGG16.

## How to run the code
1) Run the python notebook file: vit.ipynb
2) The trained model will be saved on the desired path: vit-base-beans
3) Run the app.py with the help of command: streamlit run app.py
4) The web app will run on your local host where you can upload any gameplay image and get the name of the gameplay

   In order to change the dataset you can just use any data of yours and load it in the vit.ipynb file using load_dataset() command.
