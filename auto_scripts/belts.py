import json
import os

def create_technique(display_name, tech_name):
    tech_id = tech_name.lower().replace(" ", "_")
    return {
        "name": display_name,
        "image": f"/images/techniques/{tech_id}/preview.png",
        "link": f"/techniques/technique.html?{tech_id}"
    }

def add_to_json(file_name='belts.json'):
    belts_info = [
        {
            "belt": "purple",
            "color": "#a020f0",
            "DisplayFalls": ["Ushiro Ukemi - Backward Breakfall"],
            "falls": ["ushiro_ukemi"],
            "DisplayStand": ["Koshi Guruma - Hip Wheel", "O Uchi Gari - Major Inner Reap"],
            "stand": ["koshi_guruma", "o_uchi_gari"],
            "DisplayPins": ["Kesa Gatame - Scarf Hold"],
            "pins": ["kesa_gatame"]
        },
        {
            "belt": "purple_yellow",
            "color": "#e5b62f",
            "DisplayFalls": ["Zenpo Ukemi - Forward Roll"],
            "falls": ["zenpo_ukemi"],
            "DisplayStand": ["O Goshi - Major Hip Throw", "Ippon Seoi Nage - One-Arm Shoulder Throw"],
            "stand": ["o_goshi", "ippon_seoi_nage"],
            "DisplayPins": ["Yoko Shiho Gatame - Side Four-Corner Hold"],
            "pins": ["yoko_shiho_gatame"]
        },
        {
            "belt": "yellow",
            "color": "#fdd835",
            "DisplayFalls": ["Yoko Ukemi - Side Breakfall"],
            "falls": ["yoko_ukemi"],
            "DisplayStand": ["O Soto Gari - Major Outer Reap", "Uki Goshi - Floating Hip Throw", "Morote Seoi Nage - Two-Arm Shoulder Throw", "Eri Seoi Nage - Lapel Shoulder Throw"],
            "stand": ["o_soto_gari", "uki_goshi", "morote_seoi_nage", "eri_seoi_nage"],
            "DisplayPins": ["Kata Gatame - Shoulder Hold", "Kami Shiho Gatame - Upper Four-Corner Hold"],
            "pins": ["kata_gatame", "kami_shiho_gatame"]
        },
        {
            "belt": "yellow_orange",
            "color": "#ffa500",
            "DisplayFalls": [],
            "falls": [],
            "DisplayStand": ["Tsuri Goshi - Lifting Hip Throw", "Tai Otoshi - Body Drop", "Ko Uchi Gari - Minor Inner Reap", "Kubi Nage - Neck Throw"],
            "stand": ["tsuri_goshi", "tai_otoshi", "ko_uchi_gari", "kubi_nage"],
            "DisplayPins": ["Kuzure Kesa Gatame - Scarf Hold (Modified)", "Gyaku Kesa Gatame - Reverse Scarf Hold"],
            "pins": ["kuzure_kesa_gatame", "gyaku_kesa_gatame"]
        },
        {
            "belt": "orange",
            "color": "#ff8c00",
            "DisplayFalls": [],
            "falls": [],
            "DisplayStand": ["Tsuri Komi Goshi - Lifting Pulling Hip Throw", "Soto Makikomi - Outer Winding Throw", "Harai Goshi - Sweeping Hip Throw", "De Ashi Barai - Advanced Foot Sweep", "Tomoe Nage - Circle Throw"],
            "stand": ["tsuri_komi_goshi", "soto_makikomi", "harai_goshi", "de_ashi_barai", "tomoe_nage"],
            "DisplayPins": ["Ushiro Kesa Gatame - Rear Scarf Hold", "Tate Shiho Gatame - Straddle Hold"],
            "pins": ["ushiro_kesa_gatame", "tate_shiho_gatame"]
        },
        {
            "belt": "orange_green",
            "color": "#32cd32",
            "DisplayFalls": [],
            "falls": [],
            "DisplayStand": ["Sumi Gaeshi - Corner Throw", "Ko Soto Gari - Minor Outer Reap", "Tsuri Komi Ashi Sazai - Lifting Pulling Foot Stop (Sazai)", "Uchi Mata - Inner Thigh Throw"],
            "stand": ["sumi_gaeshi", "ko_soto_gari", "tsuri_komi_ashi_sazai", "uchi_mata"],
            "DisplayPins": ["Mune Gatame - Chest Hold", "Kuzure Yoko Shiho Gatame - Side Four-Corner Hold (Modified)"],
            "pins": ["mune_gatame", "kuzure_yoko_shiho_gatame"]
        },
        {
            "belt": "green",
            "color": "#008000",
            "DisplayFalls": [],
            "falls": [],
            "DisplayStand": ["Hane Goshi - Springing Hip Throw", "Morote Gari - Double Leg Takedown", "Yoko Otoshi - Side Drop", "Kata Guruma - Shoulder Wheel", "Tani Otoshi - Valley Drop"],
            "stand": ["hane_goshi", "morote_gari", "yoko_otoshi", "kata_guruma", "tani_otoshi"],
            "DisplayPins": ["Kuzure Kami Shiho Gatame - Upper Four-Corner Hold (Modified)", "Mokure Kesa Gatame - Scarf Hold (Mokure)"],
            "pins": ["kuzure_kami_shiho_gatame", "mokure_kesa_gatame"]
        },
        {
            "belt": "green_blue",
            "color": "#0000cd",
            "DisplayFalls": [],
            "falls": [],
            "DisplayStand": ["Ashi Guruma - Foot Wheel", "O Guruma - Large Wheel", "Hiza Guruma - Knee Wheel", "O Soto Guruma - Large Outer Wheel", "Ko Soto Gake - Minor Outer Hook", "Okuri Ashi Barai - Accompanying Foot Sweep", "Uki Waza - Floating Technique"],
            "stand": ["ashi_guruma", "o_guruma", "hiza_guruma", "o_soto_guruma", "ko_soto_gake", "okuri_ashi_barai", "uki_waza"],
            "DisplayPins": ["Tate Senkaku Gatame - Triangular Stranglehold", "Kami Senkaku Gatame - Upper Triangular Stranglehold", "Kesa Gatame - Scarf Hold"],
            "pins": ["tate_senkaku_gatame", "kami_senkaku_gatame", "kesa_gatame"]
        },
        {
            "belt": "blue",
            "color": "#0000ff",
            "DisplayFalls": [],
            "falls": [],
            "DisplayStand": ["Sumi Gaeshi - Corner Throw", "Te Guruma - Hand Wheel", "Ushiro Goshi - Rear Hip Throw", "Sokuinage - Scoop Throw", "Ura Nage - Back Throw", "Yoko Gake - Side Hook", "Utsuri Goshi - Changing Hip Throw"],
            "stand": ["sumi_gaeshi", "te_guruma", "ushiro_goshi", "sokuinage", "ura_nage", "yoko_gake", "utsuri_goshi"],
            "DisplayPins": ["Yoko Gatame - Side Hold","Uki Gatame - Floating Hold"],
            "pins": ["yoko_gatame", "uki_gatame"]
        }
    ]

    # Check if the file exists, if not, create the structure
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
    else:
        data = {"belts": []}

    for belt_info in belts_info:
        belt = belt_info["belt"].replace("–", "-")
        belt_data = {
            "id": f"{belt}_belt",
            "name": f"{belt.capitalize().replace('_', '-')} Belt",
            "color": belt_info["color"],
            "footerImage": f"/images/footers/{belt}.png",
            "beltImage": f"/images/belts/{belt}.png",
            "techniques": {
                "Falls": [create_technique(display_name, tech_name) for display_name, tech_name in zip(belt_info["DisplayFalls"], belt_info["falls"])],
                "Standing Exercises": [create_technique(display_name, tech_name) for display_name, tech_name in zip(belt_info["DisplayStand"], belt_info["stand"])],
                "Pins": [create_technique(display_name, tech_name) for display_name, tech_name in zip(belt_info["DisplayPins"], belt_info["pins"])]
            }
        }
        # Add the new belt info to the data
        data["belts"].append(belt_data)

    # Write the updated data back to the file
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

add_to_json()
