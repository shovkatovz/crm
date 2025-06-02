# Python bazaviy imiji
FROM python:3.10-slim

# Ishchi katalog yaratish
WORKDIR /app

# Talablar faylini nusxalash va o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani konteynerga nusxalash
COPY . .

# Django porti
EXPOSE 8000

# Django serverni ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]