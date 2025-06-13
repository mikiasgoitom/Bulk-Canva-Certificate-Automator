import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
from dotenv import load_dotenv
import yagmail

# loading the .env file
load_dotenv()

sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_PASSWORD") 

# Check if environment variables were loaded correctly
if not sender_email or not app_password:
    print("Error: EMAIL_ADDRESS or EMAIL_PASSWORD not found in .env file.")
    exit()

print(f"Initializing email for {sender_email}...")
# Initialize yagmail
yag = yagmail.SMTP(sender_email, app_password)
print("Email client initialized.")

# --- SCRIPT LOGIC ---

# Load student data
df = pd.read_csv("student cert_canva_1.csv")

# Load certificate template
template_path = "./cert_template.png"
output_dir = "output"
font_path = "./fonts/Matangi/static/Matangi-Regular.ttf"
font_size = 75

# Create output directory
os.makedirs(output_dir, exist_ok=True)

for index, row in df.iterrows():
    name = row['name']
    email = row['email']
    # Generate the certificate
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    x = 147
    y = 355
    draw.text((x,y), name.upper(), fill="#40ad5d", font=font)
    cert_path = f"{output_dir}/{name.replace(' ', '_')}.png"
    image.save(cert_path,"png", resolution=100.0)
    print(f"Certificate saved to {cert_path}")

    # read the email template
    with open("email_template.txt", "r", encoding="utf - 8") as file:
        email_template = file.read()
    # personalize email
    personalized_email = email_template.replace("{name}", name)
    # Send via email using the correctly initialized 'yag' object from the top
    print(f"Sending certificate to {email}...")
    try:
        yag.send(
            to=email,
            subject="🎉 Congratulations on Completing the Beginners Track - Here's Your Certificate!",
            contents=personalized_email,
            
            attachments=cert_path
        )
        print(f"Email successfully sent to {email}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
 

print("__All certificates sent!__")
