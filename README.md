# Image Resampling Using Bilinear Interpolation in Python (NumPy &amp; SciPy)

<b><em>Task</em></b>

Input the RGB values for a downsampled image and the downsampling coefficient (N). Given the size of the original image, restore the original image.

<b><em>Input Format</em></b>

The first line contains 3 space-separated integers, r (the number of rows in the downsampled image), c (the number of columns in the downsampled image) and N (the downsample coefficient), respectively.

The second line contains 2 space-separated integers, R and C, representing the respective numbers of rows and columns in the original image.

The R subsequent lines describe the 2D grid representing the pixel-wise values from the images (which were originally in JPG or PNG formats).
Each line contains C pixels, and each pixel is represented by three comma-separated values in the range from 0 to 255 denoting the respective Blue, Green, and Red components. There is a space between successive pixels in the same row.

No input test case will exceed 3MB in size. This is the size of the RGB test matrix, NOT the original image from which it was generated. 

<b><em>Output Format</em></b>

A 2D grid of pixel values describing the upsampled image. The output will follow the same format as the grid received as input.
