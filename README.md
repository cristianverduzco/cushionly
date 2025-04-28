# `cushionly`
> A SaaS budget tracking app designed to help users grow their financial cushion — one smart decision at a time.

---

## 🚀 About Cushionly
Cushionly is a full-stack SaaS application that empowers users to track their budgets, manage expenses, and build better financial habits.  
Users can start for free, and upgrade to premium features for deeper analytics and unlimited budget tracking.

Built with a modern tech stack — React, FastAPI, PostgreSQL, and Stripe — Cushionly is optimized for real-world performance and scalability.

---

## 🛠 Tech Stack
- **Frontend**: React.js (Vite or Create React App) + Tailwind CSS
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Authentication**: JWT (JSON Web Tokens)
- **Payments**: Stripe (Checkout and Billing)
- **Hosting**: Render (backend) + Vercel (frontend)

---

## ✨ Features
- User authentication (signup/login/logout)
- Create and manage budgets
- Track expenses within budgets
- Freemium model with premium upgrades via Stripe
- Dashboard with visual spending analytics (charts and graphs)
- Role-based permissions (free vs premium users)
- Responsive design (mobile and desktop)
- Secure API endpoints with JWT authentication

---

## 🔒 Authentication System Overview

Cushionly features a full-stack authentication system built with FastAPI, PostgreSQL, SQLAlchemy, and JWT.

### 📚 Features
- **Secure User Signup**: Users register with a securely hashed password.
- **User Login**: Authenticated users receive a JWT access token.
- **JWT Token-Based Authentication**: Stateless and secure session management.
- **Protected Routes**: Endpoints like `/auth/profile` are protected and require valid tokens.
- **Password Hashing**: Passwords are encrypted with bcrypt via Passlib.

### 🔥 Auth Flow Diagram

```plaintext
[User Signup] ---> [Password hashed] ---> [Stored securely in PostgreSQL]

[User Login] ---> [Password verified] ---> [JWT access token issued]

[User Access /auth/profile] ---> [JWT validated] ---> [User info returned if authenticated]

```

---

### 🗺 Roadmap
- [ x ] User authentication (signup/login/logout)
- [ x ] JWT-Protected API endpoints
- [ x ] PostgreSQL database integration
- [ ] Basic budget/expense management
- [ ] Stripe subscription integration
- [ ] Advanced analytics (category breakdowns, monthly reports)
- [ ] Email notifications for budget summaries
- [ ] Mobile PWA version
- [ ] Admin dashboard for managing users and plans