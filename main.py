import nltk
from nltk import pos_tag
from newspaper import Article
import string




url  = '' # Web Url'si
 
article = Article(url) # haberin url'si
article.download() # haberin indirilmesi
article.parse() # haberin içeriği çekildi
metin = article.text # metin değişkenine haberin içeriği atandı

nltk.download('punkt') # nltk kütüphanesinden punkt indirildi
cumleler = nltk.sent_tokenize(metin) # metin değişkenindeki metin cümlelere ayrıldı


# for cumle in cumleler:print("Cümle: ",cumle) # cümleler ekrana yazdırıldı

temizMetin = metin.translate(str.maketrans('', '', string.punctuation)) # metindeki noktalama işaretleri temizlendi
genelKelimeler = nltk.word_tokenize(temizMetin) # metin değişkenindeki metin kelimelere ayrıldı

# for kelime in genelKelimeler:print(kelime) # kelimeler ekrana yazdırıldı

fd = nltk.FreqDist(genelKelimeler) # kelimelerin frekansları hesaplandı
result = fd.most_common(30) # en çok geçen 10 kelime ekrana yazdırıldı

nltk.download('averaged_perceptron_tagger') # nltk kütüphanesinden averaged_perceptron_tagger indirildi
tagged_sent = pos_tag(genelKelimeler) # kelimelerin cümle içindeki rolleri belirlendi

# for kelime in taggent_sent:print(kelime) # kelimelerin rolleri ekrana yazdırıldı

result = [word for word, pos in tagged_sent if pos == 'CD'] # kelimelerin rolleri belirlendi

print(result) # kelimelerin rolleri ekrana yazdırıldı


