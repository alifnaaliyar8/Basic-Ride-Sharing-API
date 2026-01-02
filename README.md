#Basic Ride Sharing API (Django REST Framework)

#Features
- User registration and login
- JWT authentication
- Create ride requests
- Ride matching (driver accepts ride)
- Ride status updates (started, completed, cancelled)
- Real-time ride tracking (simulation)
- Class-based ViewSets

#Authentication
- POST /api/auth/register/
- POST /api/auth/login/
- GET /api/auth/user/
- POST /api/auth/logout/
#Rides
- POST /api/rides/
- GET /api/rides/
- GET /api/rides/{id}/
- POST /api/rides/{id}/accept_ride/
- PATCH /api/rides/{id}/update_status/
- PATCH /api/rides/{id}/track/