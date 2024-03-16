import os,sys, json
import jinja2
# from jinja2 import Template

books = ["Chapter 1 - Sainya-Darśana (Observing the Armies on the Battlefield)",
"Chapter 2 - Sāṅkhya Yoga (The Yoga of Analysis)",
"Chapter 3 - Karma Yoga (The Yoga of Action)",
"Chapter 4 - Jñāna Yoga (The Yoga of Knowledge)",
"Chapter 5 - Karma Sannyāsa Yoga (The Yoga of the Renunciation of Action)",
"Chapter 6 - Dhyāna Yoga (The Yoga of Meditation)",
"Chapter 7 - Jñāna-Vijñāna Yoga (The Yoga of Knowledge and Realisation)",
"Chapter 8 - Tāraka-Brahma Yoga (The Yoga of the Supreme)",
"Chapter 9 - Rāja Guhya Yoga (The Yoga of the Greatest Secret)",
"Chapter 10 - Vibhūti Yoga (The Yoga of Divine Splendour)",
"Chapter 11 - Viśvarūpa Darśana Yoga (The Yoga of the Universal Form)",
"Chapter 12 - Bhakti Yoga (The Yoga of Devotion)",
"Chapter 13 - Prakṛti-Puruṣa Viveka Yoga (The Yoga of Differentiation)",
"Chapter 14 - Guṇa-Traya Vibhāga Yoga (The Yoga of Understanding the Three Modes of Material Nature)",
"Chapter 15 - Puruṣottama Yoga (The Yoga of the Supreme Person)",
"Chapter 16 - Daivāsura Sampad Vibhāga Yoga (The Yoga of Discretion-Pious and Impious Natures)",
"Chapter 17 - Śraddhā-Traya Vibhāga Yoga (The Yoga Explaining Three Types of Faith)",
"Chapter 18 - Mokṣa Yoga (The Yoga of Supreme Perfection)"]
from collections import defaultdict 
class GenerateHtml:
    def __init__(self):
        with open("gita.json", "r") as fp:
            self.data = json.load(fp)
        
        self.new_data = defaultdict(list)
        self.chapter = '1'
        self.line = '1'


        for i in range(len(self.data)):
            if self.data[i]["author_id"] == 17:
                chapter_line=self.data[i]["description"].split('।।')[1]
                # print(chapter_line)
                if ' ' in chapter_line:
                    print('-'*100, chapter_line) 
                    continue
                self.chapter, self.line = chapter_line.split('.')
            if self.data[i]["author_id"] == 18:
                self.new_data[self.chapter].append(self.data[i]["description"])
        self.create_html_file()

    def load_template(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        return templateEnv.get_template('chapter.html')

    def create_html_file(self):
        template = self.load_template()
        for key, value in self.new_data.items():
            # create a chapter eg: 1/1.html 
            filedata = template.render(
                chapter = books[int(key)-1],
                verses = value
            )
            html_dir = 'site' #,f"chapter_{key}.html"))
            if not os.path.exists(html_dir):
                os.makedirs(html_dir)
            fname = f'{html_dir}/chapter_{key}.html'
            if key =='1':
                fname = f'{html_dir}/index.html'
            
            if os.path.isfile(fname):
                print('Chapter already exist')
            else:
                fp = open(fname, 'w')
                fp.write(filedata)

if __name__=='__main__':
    c=GenerateHtml()