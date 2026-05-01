Harika bir proje! Dosyalarınızı incelediğimde, projenin hem bir **Streamlit (Python)** uygulaması (`app.py`) hem de bir **Node.js/Express** backend yapısı (`server.js` ve `index.html` tabanlı frontend) içerdiğini görüyorum. Bu proje, öğrencilere kişiselleştirilmiş ders programları sunan ve LLM (Claude/Llama) modellerini kullanan gelişmiş bir **AI Eğitim Koçu**.

İşte projeniz için hazırladığım kapsamlı **README.md** dosyası:

---

# 🎓 LearnerAI Coach - Kişisel Eğitim Asistanı

**LearnerAI Coach**, öğrencilerin sınıf seviyelerine, hedeflerine ve çalışmak istedikleri derslere göre kişiselleştirilmiş haftalık çalışma planları oluşturan, interaktif bir yapay zeka asistanıdır.

## 🌟 Öne Çıkan Özellikler
* **Kişiselleştirilmiş Onboarding:** Sınıf seviyesi, ders tercihleri ve hedeflerinize göre özelleştirilmiş başlangıç süreci.
* **Haftalık Akıllı Planlama:** AI tarafından oluşturulan, günlere bölünmüş detaylı ders programı.
* **Detaylı Ders Analizi:** Her konu için "Isınma", "Ana Çalışma" ve "Değerlendirme" gibi aşamalardan oluşan saatlik kırılımlar.
* **AI Koçluk Paneli:** Ders çalışırken sorularınızı sorabileceğiniz, teşvik edici ve yol gösterici AI sohbet asistanı.
* **Modern Arayüz:** Karanlık mod destekli, "Plus Jakarta Sans" tipografisiyle güçlendirilmiş kullanıcı dostu tasarım.

## 🛠️ Teknolojiler
* **Frontend:** HTML5, CSS3 (Custom Glassmorphism), JavaScript (Vanilla), Lucide Icons.
* **Backend / Framework:** * **Python:** Streamlit (Hızlı prototipleme ve dashboard için).
    * **Node.js:** Express.js (API ve sunucu yönetimi için).
* [cite_start]**AI Modelleri:** Groq (Llama 3.3 70B), Anthropic (Claude)[cite: 2].

## 🚀 Kurulum

### 1. Gereksinimler
* Node.js (v18+)
* Python (3.9+)
* [cite_start]API Anahtarları (Groq veya Gemini/Anthropic) [cite: 1]

### 2. Ortam Değişkenleri
[cite_start]Projenin kök dizininde bir `.env` dosyası oluşturun ve anahtarlarınızı ekleyin[cite: 1]:
```env
GEMINI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

### 3. Uygulamayı Çalıştırma

#### Streamlit (Dashboard) Versiyonu için:
```bash
pip install streamlit groq
streamlit run app.py
```

#### Web/Express Versiyonu için:
```bash
npm install
npm start
```

## 📂 Proje Yapısı
* `app.py`: Streamlit tabanlı ana uygulama ve dashboard logic'i.
* `index.html`: Web tabanlı giriş ekranı ve onboarding süreci.
* `dashboard.js`: Planlama ve AI asistanı etkileşimlerini yöneten script.
* `detail.js`: Konu bazlı detaylı çalışma planı oluşturma motoru.
* `server.js`: API isteklerini ve LLM entegrasyonunu sağlayan sunucu dosyası.
* [cite_start]`api.js`: AI modelleri ile iletişimi sağlayan yardımcı fonksiyonlar[cite: 2].

## 📝 Notlar
* Uygulama tamamen **Türkçe** dil desteğine sahiptir.
* AI modelleri için `llama-3.3-70b-versatile` kullanılacak şekilde optimize edilmiştir.

---

**LearnerAI Coach** ile öğrenme sürecini daha verimli ve motive edici hale getirin! ✨
