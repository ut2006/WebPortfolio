# Portfolio Website - Django
Nhóm đề 10: Xây dựng Website cá nhân và Portfolio
## Hướng dẫn cài đặt & chạy

### 1. Tạo môi trường ảo và cài thư viện

```bash
cd WebPortfolio
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Tạo database và migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Tạo superuser (quản trị admin)

```bash
python manage.py createsuperuser (ko cần chạy, đã có user giabach)
```

### 4. Chạy server

```bash
python manage.py runserver
```

Truy cập:
- Trang chủ: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Dự án: http://127.0.0.1:8000/projects/
- Blog: http://127.0.0.1:8000/blog/

## Nhập dữ liệu qua Admin

1. Vào **Admin → Portfolio → Profile**: Tạo hồ sơ cá nhân (full_name, bio, career_goal, core_values, achievements)
2. Vào **Skill**: Thêm kỹ năng (name, level 1-100, category FE/BE/SOFT)
3. Vào **Project**: Thêm dự án, tick `is_featured` để hiển thị trang chủ
4. Vào **Blog**: Thêm bài viết, tick `is_featured` để hiển thị trang chủ
5. **Contact**: Xem tin nhắn đến từ form liên hệ

## Các module chức năng (6 × 0.5đ)

| Module | URL | Mô tả |
|--------|-----|-------|
| Profile | `/` | Hero, About, giới thiệu bản thân |
| Skill | `/#skills` | Skill bar frontend/backend, soft skill chips |
| Project | `/projects/` | Lọc theo category/type, search, phân trang |
| Blog | `/blog/` | Lọc theo category, search, phân trang |
| Contact | `/#contact` | Form liên hệ lưu vào DB, hiển thị trong admin |
| Admin | `/admin/` | Django Admin quản lý toàn bộ nội dung |
