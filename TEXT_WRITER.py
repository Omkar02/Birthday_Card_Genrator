from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from helper import quotes,font_size_sort
import random
import os
import csv




def Card_Prep(person_name,card_no,quote,font_path):
    img = Image.open("All_cards/"+str(card_no)+".jpg")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font_path, font_size_sort[font_path])
    draw.text((100, 2170), f'Dear {person_name},\n{quote}\n     '
                           f'                                -From GPTW Team.',(0, 0, 0), font=font)
    img.save(f'output/{person_name}.jpg')
    print(f'{person_name} saved!')






path, dirs, files = next(os.walk("All_cards"))
file_count = len(files)



path1, dirs1, files1 = next(os.walk("All_font"))
file_count1 = len(files1)
# rand_font = random.randint(0,file_count1)


with open("names.txt", "r") as f:
    all_name = [row for row in csv.reader(f,delimiter=',')]



for names in all_name[0]:
    rand_quotes = random.randint(1, len(quotes))
    rand_card = random.randint(1, file_count)
    rand_font = random.randint(0, file_count1-1)
    # rand_font = 'All_font/Great Wishes.otf'
    # print(names)
    print(names, rand_card, rand_quotes, files1[rand_font])
    Card_Prep(names.title(), rand_card, quotes[rand_quotes], path1 + '/' + files1[rand_font])
    # print(names, rand_card, rand_quotes, rand_font)
    # Card_Prep(str(names), rand_card, quotes[rand_quotes], rand_font)
    print(f'Done for {names.title()}')
#

