from PIL import Image, ImageDraw
import random

def generate_art(emotion):
    width, height = 256, 256  # size of the image
    image = Image.new("RGB", (width, height))

    # set colors based on the emotion
    colors = {
        "happy": (255, 223, 0),  # yellow
        "sad": (0, 102, 204),    # blue
        "angry": (255, 0, 0),    # red
        "calm": (0, 153, 76),    # green
    }
    color = colors.get(emotion.lower(), (128, 128, 128))  # default gray

    draw = ImageDraw.Draw(image)

    # Draw random circles for an abstract art effect
    for _ in range(10):
        radius = random.randint(20, 60)
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)

    # Display the generated image
    image.show()
    print("Generated art displayed.")

def main():
    emotion = input("Enter an emotion (e.g., happy, sad, angry, calm): ")
    generate_art(emotion)

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
