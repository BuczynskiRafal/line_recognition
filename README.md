# Endpoint Position Prediction on Images using Convolutional Neural Networks

## Project Description
This project involves the use of convolutional neural networks (CNNs) to detect the coordinates of the starting and ending points of lines in images. We train a CNN model to generate heat maps indicating the positions of these points, and then process these heat maps to obtain the exact coordinates of the points.

The images used in the project are 64x64 grayscale images, with two points marked on each image to represent the start point and end point.

## Methods
The project uses a convolutional neural network (CNN). It starts with an input layer that takes 64x64 grayscale images. The model has an encoder part with three convolutional layers (with 32, 64, and 128 filters), each followed by a max pooling layer. After encoding, the model decodes the information using two upsampling layers each followed by a convolutional layer (with 64 and 32 filters). The final output layer is a 1x1 convolutional layer with a sigmoid activation function. The model predicts a 64x64 heatmap for each image, where the heatmap represents the likelihood of each pixel being part of the start or end point of a line.

The model was trained using the binary cross-entropy loss, and its performance was evaluated using accuracy and the Area Under the Curve (AUC) for the receiver operating characteristic curve. Additionally, we used the Adam optimizer for training.

For predictions, the trained model was used to generate heatmaps for new images. The Scikit-image library's label and regionprops functions were used to identify clusters on the heatmaps, from which we obtained the coordinates of the two most prominent points, corresponding to the start and end points.

## Saving and loading the model
After the training phase, the model is saved to disk for later use. The model is saved in the "model/saved" directory. The saved model can be loaded at any time for forecasting, further training or model analysis. To load a saved model, use the following command:
```python
loaded_model = load_model(os.path.join(BASE_DIR, 'model', 'saved'))
```

## Results
The trained model was evaluated on a test set consisting of 999 samples. The evaluation was carried out using MAE, MSE, and R2 score as performance metrics. 

The following results were obtained from the evaluation:
* Mean Absolute Error (MAE): 9.63
* Mean Squared Error (MSE): 20.31
* R2 Score: 0.94

These results show that the model performs fairly well in predicting the start and end points of the lines in the images, with a good R2 score indicating a high degree of correlation between the predicted and actual coordinates. However, there is still some room for improvement, as indicated by the non-zero values for MAE and MSE.

## Image Generator
This project utilizes a custom image generator that produces 64x64 grayscale images. Each image features a line drawn between two randomly generated points. The coordinates of these points also serve as labels for supervised learning. 

The ImageGenerator class is responsible for generating and saving the synthetic images. The class is designed in such a way that the generated points ensure the image always contains a line. The randomness ensures the diversity of the images, and having the line coordinates in the image file name allows for an easy way to create labels for supervised learning tasks.

Here is an example of how to use the ImageGenerator class:
```python
if __name__ == "__main__":
    for i in range(5000):
        generator = ImageGenerator(r"data\dataset")
        generator.run()
```
In the code above, we create an instance of ImageGenerator and call the run method to generate and save a synthetic image. This is done in a loop to create multiple images. In this case, given 5,000 the generator will create 10,000 files, the start and end coordinates are swapped.