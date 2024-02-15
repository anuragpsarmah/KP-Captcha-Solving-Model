import os
from selenium import webdriver
from PIL import Image


def capture_page_screenshot(url, output_directory="captured_images", crop_params=None):
    # Use a webdriver (e.g., ChromeDriver) to interact with the page
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for some time to allow dynamic content to load (you may need to adjust this)
    driver.implicitly_wait(10)

    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Capture the screenshot of the loaded page
        screenshot_path = os.path.join(
            output_directory,
            f"captured_page_{len(os.listdir(output_directory)) + 1}.png",
        )
        driver.save_screenshot(screenshot_path)

        # Crop the screenshot based on provided parameters
        if crop_params:
            crop_and_save_image(screenshot_path, crop_params)
            # Remove the original captured image
            os.remove(screenshot_path)
        else:
            print(f"Page screenshot saved to {screenshot_path}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the webdriver
        driver.quit()


def crop_and_save_image(image_path, crop_params):
    # Open the captured image using Pillow (PIL) library
    image = Image.open(image_path)

    # Crop the image based on provided parameters (left, top, right, bottom)
    cropped_image = image.crop(crop_params)

    # Save the cropped image
    cropped_path = image_path.replace(".png", "_cropped.png")
    cropped_image.save(cropped_path)
    print(f"Cropped image saved to {cropped_path}")


def main():
    url = "https://kp.christuniversity.in/KnowledgePro/StudentLoginAction.do?method=studentLogoutAction"

    # Example crop parameters: (left, top, right, bottom)
    crop_params = (338, 370, 465, 415)

    for i in range(102,1000):
        capture_page_screenshot(url, crop_params=crop_params)


if __name__ == "__main__":
    main()
