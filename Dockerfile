# বেস ইমেজ হিসেবে একটি পাইথন ইমেজ ব্যবহার করুন
FROM python:3.10-slim

# কাজের ডিরেক্টরি সেট করুন
WORKDIR /app

# প্রয়োজনীয় টুলস এবং Chromium ব্রাউজার ইনস্টল করুন
# --no-install-recommends ব্যবহার করে অপ্রয়োজনীয় প্যাকেজ ইনস্টল করা থেকে বিরত থাকুন
RUN apt-get update && apt-get install -y \
    chromium \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt ফাইলটি কপি করুন এবং লাইব্রেরিগুলো ইনস্টল করুন
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# আপনার প্রজেক্টের বাকি ফাইলগুলো কপি করুন
COPY . .

# অ্যাপ্লিকেশন চালানোর জন্য কমান্ড দিন
CMD ["python", "app.py"]
