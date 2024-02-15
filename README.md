# Knowledge Pro Captcha Solving Model

Knowledge Pro serves as the student profile management system utilized by Christ (Deemed to be University). The platform features a login page where users must input their username, password, and solve a captcha. This project aims to solve captcha challenges within Knowledge Pro by training a machine learning model. The project is only for learning purposes.

<p align="center"><img src="https://res.cloudinary.com/dgh9mcfxu/image/upload/v1708018249/Screenshot_258_wtet0n.png" alt="Alt text" width="800" height="400"></p>

<p align="center"><img src="https://res.cloudinary.com/dgh9mcfxu/image/upload/v1708018259/0c1d22_edptki.png" alt="Alt text" width="200" height="100"></p>

## Deployment

To deploy and run this project on your local system, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/anuragp787/KP-Captcha-Solving-Model.git
    ```
    
2. Install the following python libraries:
   
    ```bash
    pip install Flask
    pip install selenium
    pip install pillow
    pip install opencv-python-headless
    pip install tensorflow
    pip install mltu
    pip install numpy
    ```

3. Run Generate_Captcha.py file to generate 1000 Knowledge-Pro website captchas.

4. Run the train.py file to train the model on the generated dataset.

5. Run the inferenceModel.py to run an automated test on the dataset.

6. Run single_captcha_test.py file while referencing the test image through 'image_path' variable to test a single captcha.
