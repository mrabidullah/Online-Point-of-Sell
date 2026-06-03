# Django POS (Point of Sale)

Professional POS web app built with Django + Tailwind CSS (CDN).
Features:
- Email/username signup & login (Django auth)
- Storefront with product catalog & search
- Shopping cart (session-based)
- Checkout with **Cash on Delivery**
- Admin dashboard: products CRUD, orders management, sales stats
- Django admin panel at /admin/

## Quick Start

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

- Storefront: `/`
- Login: `/accounts/login/`
- Signup: `/accounts/signup/`
- Staff dashboard: `/dashboard/` (requires staff user — use the superuser)
- Django admin: `/admin/`

Tailwind is loaded via CDN (no Node build step required).
