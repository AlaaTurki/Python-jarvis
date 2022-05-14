import os
import json


with open("train-v2.0.json", 'r', encoding="utf-8") as f:
    data = json.load(f)

    for title in data["data"]:

        with open("dataset\\" + title["title"].strip() + ".yml", 'w+',encoding="utf-8") as f2:
            f2.write("categories:" + "\n")
            f2.write("- " + title["title"].strip() + "\n")
            f2.write("conversations:" + "\n")

            for conv in title["paragraphs"]:
                for question in conv["qas"]:
                    if len(question["answers"])>0:
                        f2.write("- - " + question["question"].strip().replace("\"","") + "\n")
                        f2.write("  - " + question["answers"][0]["text"].strip() + "\n")


    