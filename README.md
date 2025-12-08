# Tech Workshop Website

A Django-based website for an inter-university tech workshop.

## Features
- Home page with event details (name, date, location, description)
- Schedule section with time, duration, location, and descriptions
- Speakers section with name, title, topic, and organization
- Registration form that sends data to vnjagi05@gmail.com
- Payment page with MPESA integration simulation
- Contact section with email, phone, and Instagram links
- Modern responsive UI using Bootstrap 5

## Setup Instructions

1. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run database migrations:**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

4. **Create superuser for admin access:**
```bash
python3 manage.py createsuperuser
```

5. **Populate sample data (optional):**
```bash
python3 manage.py populate_data
```

6. **Run the development server:**
```bash
python3 manage.py runserver
```

7. **Access the application:**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Email Configuration

To enable email functionality for registration notifications:

1. Update the email settings in `Tech_Workshop/settings.py`:
   - Set `EMAIL_HOST_PASSWORD` to your Gmail app-specific password
   - Enable 2-factor authentication on your Gmail account
   - Generate an app-specific password from Google Account settings

2. For development without email, the system will still work but won't send emails.

## Admin Panel Usage

1. Log in to the admin panel with your superuser credentials
2. Add speakers under "Speakers" section:
   - Name, Title, Topic, Organization
3. Add schedule items under "Schedules" section:
   - Start time, Duration, Location, Description
4. View registrations under "Registrations" section

## Features Details

### Home Page
- Event name: "Inter-University Tech Workshop 2024"
- Date: December 15, 2024
- Location: University of Nairobi
- Time: 9:00 AM - 6:00 PM
- Event description and call-to-action buttons

### Registration Form
- Collects name and organization
- Optional email field
- Sends notification to vnjagi05@gmail.com
- Shows success confirmation

### Payment Page
- MPESA payment simulation
- Phone number validation
- Amount input
- Success confirmation with instructions

### Contact Information
- Email: vnjagi05@gmail.com
- Phone: 0727902188
- Instagram: https://www.instagram.com/v._irt

## Project Structure

```
Tech_Workshop/
├── Tech_Workshop/          # Main project settings
├── website/               # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   ├── templates/website/ # HTML templates
│   └── management/commands/ # Django management commands
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Customization

- Update event details in `home.html` template
- Modify contact information in `base.html`
- Add custom CSS in the base template
- Extend models for additional features
- Integrate real payment gateway for production

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```
