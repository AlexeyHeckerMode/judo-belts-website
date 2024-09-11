import json
import re

# List of names
names = [
    "Ushiro Ukemi",
    "Koshi Guruma",
    "O Uchi Gari",
    "Zenpo Ukemi",
    "O Goshi",
    "Ippon Seoi Nage",
    "Yoko Ukemi",
    "O Soto Gari",
    "Uki Goshi",
    "Morote Seoi Nage",
    "Eri Seoi Nage",
    "Tsuri Goshi",
    "Tai Otoshi",
    "Ko Uchi Gari",
    "Kubi Nage",
    "Tsuri Komi Goshi",
    "Soto Makikomi",
    "Harai Goshi",
    "De Ashi Barai",
    "Tomoe Nage",
    "Sumi Gaeshi",
    "Ko Soto Gari",
    "Sasae Tsurikomi Ashi",
    "Uchi Mata",
    "Hane Goshi",
    "Morote Gari",
    "Yoko Otoshi",
    "Kata Guruma",
    "Tani Otoshi",
    "Ashi Guruma",
    "O Guruma",
    "Hiza Guruma",
    "O Soto Guruma",
    "Ko Soto Gake",
    "Okuri Ashi Barai",
    "Uki Waza",
    "Te Guruma",
    "Ushiro Goshi",
    "Sukui Nage",
    "Ura Nage",
    "Yoko Gake",
    "Utsuri Goshi",
    "Kesa Gatame",
    "Yoko Shiho Gatame",
    "Kata Gatame",
    "Kami Shiho Gatame",
    "Kuzure Kesa Gatame",
    "Gyaku Kesa Gatame",
    "Ushiro Kesa Gatame",
    "Tate Shiho Gatame",
    "Kuzure Yoko Shiho Gatame",
    "Mune Gatame",
    "Kuzure Kami Shiho Gatame",
    "Mokure Kesa Gatame",
    "Tate Senkaku Gatame",
    "Kami Senkaku Gatame",
    "Uki Gatame"
]

# List of video IDs
video_ids = [
    "_g7rvsxTkz8",
    "SU7Id6uVJ44",
    "0itJFhV9pDQ",
    "GcgPdqjgXbU",
    "yhu1mfy2vJ4",
    "FQnOlCxo4oI",
    "JCwK1Ia4jsc",
    "c-A_nP7mKAc",
    "bPKwtB4lyOQ",
    "zIq0xI0ogxk",
    "zIq0xI0ogxk",
    "51Htlp7xEvE&t=16s",
    "4x6S3Q-Ktv8",
    "3Jb3tZvr9Ng",
    "F-4fyNwx52w",
    "McfzA0yRVt4",
    "bWG9O1BVKtQ",
    "qTo8HlAAkOo",
    "4BUUvqxi_Kk",
    "880WbHvHv6A",
    "5VhduA5xkbA",
    "jeQ541ScLB4",
    "699i--pvYmE",
    "iUpSu5J-bgw",
    "M9_7De6A1kk",
    "BHLQS4K85bs",
    "MnNG67pF_a0",
    "cnHRhSy8yi4",
    "3b9Me3Fohpk",
    "ROeayhvom9U",
    "SnZciTAY9vc",
    "JPJx9-oAVns&t=21s",
    "92KbCm6pQeI",
    "8b6kY4s4zH4",
    "nw1ZdRjrdRI",
    "weVOpJ63gII",
    "P-4HUgB_rK4",
    "ORIYstuxYT8",
    "vU6aJ2kFxoI",
    "Fgi9b8DJ5sQ",
    "tP1Sj1uDfSo",
    "4pQd_bEnlf0",
    "NDaQuJOFBYk",
    "TT7XJVSEQxA",
    "zQR3IOXxO_Q",
    "HFuMjOv0WN8",
    "Q2fb9jaoUFQ",
    "HvGdf1ht_5M",
    "SBapox2M2dE",
    "55-rFmBx53g",
    "54fQM7dYz0M",
    "lIt5vywPBF0",
    "YUrogQWdwiY",
    "e5HrhANfDcU",
    "None ID",
    "None ID",
    "e_lAjik1SUM",

]

# Load your JSON template
template = {
    "title": "Other Technique",
    "videoId": "other-video-id",
    "slides": [
        {
            "image": "images/other/step1.jpg",
            "description": "Step 1: Start by positioning yourself in the correct stance."
        },
        {
            "image": "images/other/step2.jpg",
            "description": "Step 2: Secure your grip and prepare to execute the technique."
        },
        {
            "image": "images/other/step3.jpg",
            "description": "Step 3: Complete the technique with a precise movement."
        }
    ]
}

# Function to format name
def format_name(name):
    # Convert to lowercase and replace spaces with underscores
    formatted_name = re.sub(r'\s+', '_', name).lower()
    return formatted_name

# Create a list of JSON objects with updated titles, video IDs, and image paths
updated_json_list = []

for name, video_id in zip(names, video_ids):
    # Create a copy of the template
    updated_template = json.loads(json.dumps(template))  # Deep copy

    # Update title
    updated_template['title'] = name

    # Update videoId
    updated_template['videoId'] = video_id

    # Update image paths
    for slide in updated_template['slides']:
        step_number = slide['image'][-5]  # Extract the step number from the image path
        slide['image'] = f"images/techniques/{format_name(name)}/step{step_number}.png"

    updated_json_list.append(updated_template)

# Optionally, write the updated JSON data to a file
with open('updated_techniques.json', 'w') as f:
    json.dump(updated_json_list, f, indent=4)

print("Updated JSON file created successfully.")
