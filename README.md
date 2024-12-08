This project has won the cs50x fair award

# BetterTherapy

BetterTherapy helps psychologists by analyzing emotions from a therapy session video using three deep learning models. It detects the intensity of emotions by analyzing facial expressions, tone of voice, and spoken words. The system identifies and stores emotionally intense moments (both audio and text) as sensitive moments. Additionally, it generates a sentiment graph to visualize the emotional trends throughout the session.  

The models used in this project were sourced from GitHub repositories, and you can find them at the following links:  
- [Model for persian sentiment analysis](<https://github.com/kasrahabib/persian-sentiment-analysis>)

The main goal of this project is to create a tool useful for psychologists, but it can be applied to any video.


فیلم جلسه تراپی گرفته و با سه مدل یادگیری عمیق احساسات را تحلیل میکند و می تواند میزان این احساسات (احساسات در صورت و لحن صحبت کردن و جمله های گفته شده) را تشخیص دهد و لحظاته اوج احساسی را به عنوان لحظات حساس ذخیره میکند (به صورت صدا و متن) و همچنین نمودار احساسات جلسه ی مشاوره را نشان میدهد 

# how to use
py main.py -c yourclip

# output
a graph and sensetive moments
<img width="477" alt="Screenshot (26)" src="https://user-images.githubusercontent.com/62204940/163457819-2c337e3b-40a3-421c-804c-f69ace819617.png">

all_sensetive_moment.txt :  
Sad__1:13_1:24  : من تو کل سال تحصیل هیچ وقت نمی شود رابطه خوب نتونستم معلم داشته باشم و

Happy__0:27_0:37  : صندلی و صندلی رفت عقب و خوردن همه بچه ها با هم خندید
