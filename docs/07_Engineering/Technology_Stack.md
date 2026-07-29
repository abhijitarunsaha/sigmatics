# Technology Stack

## Purpose

This document defines the approved technology stack for the Sigmatics platform.

The selected technologies align with the architectural principles documented throughout the project and support the long-term vision of building an AI-driven Decision Intelligence Platform.

---

# Guiding Principles

The technology stack shall:

- Support AI-first development.
- Enable rapid iterative delivery.
- Encourage modular architecture.
- Support web and mobile experiences.
- Minimize vendor lock-in.
- Prefer mature open-source technologies.
- Be cloud agnostic.
- Be container friendly.

---

# Backend

| Component | Technology |
|------------|------------|
| Language | Python 3.13+ |
| API Framework | FastAPI |
| Validation | Pydantic v2 |
| ORM | SQLAlchemy 2 |
| Database Migration | Alembic |
| Testing | pytest |

---

# Frontend

## Web

| Component | Technology |
|------------|------------|
| Framework | React |
| Language | TypeScript |
| Styling | Tailwind CSS |
| Charts | TradingView Lightweight Charts |
| Build Tool | Vite |
| State Management | React Context (initially) |

The web application shall be implemented as a Progressive Web App (PWA).

---

## Mobile

| Component | Technology |
|------------|------------|
| Framework | React Native |
| Language | TypeScript |

The mobile application shall consume the same backend APIs as the web application.

Business logic shall remain server-driven.

---

# Shared Libraries

The following shall be shared between Web and Mobile applications wherever practical:

- API Client
- DTOs
- Domain Models
- Validation Rules
- Utility Libraries
- Constants
- Theme Tokens

---

# Databases

## PostgreSQL

Primary relational database.

Stores:

- Users
- Preferences
- Decision Packages
- Notifications
- Portfolio
- Audit Logs
- Configuration

---

## TimescaleDB

Extension to PostgreSQL.

Stores:

- Market Snapshots
- Historical Indicators
- Confidence History
- Decision Timeline
- Market State History

---

## Redis

Stores:

- Active Recommendations
- Session Cache
- Market Cache
- Decision Guardian State
- Notification Queue
- WebSocket Pub/Sub

---

# Object Storage

Development:

- MinIO

Production:

- S3 Compatible Storage

---

# Authentication

JWT

Refresh Tokens

OTP Verification

Biometric Authentication (Mobile)

---

# Notifications

Web

- Browser Notifications

Android

- Firebase Cloud Messaging (FCM)

iOS

- Apple Push Notification service (APNs)

Notifications represent the live state of a Decision Package.

---

# AI & Intelligence

The Decision Engine shall remain framework independent.

AI Agents shall integrate through defined contracts.

Large Language Models shall be provider agnostic.

---

# DevOps

Containerization:

Docker

Local Development:

Docker Compose

CI/CD:

GitHub Actions

---

# Testing

- Unit Testing
- Integration Testing
- Contract Testing
- End-to-End Testing

---

# Mobile Strategy

The mobile application shall be implemented using React Native.

The web application shall be implemented as a Progressive Web App.

Both clients shall consume the same backend services.

---

# Future Evolution

The selected stack supports future integration with:

- AI Agent Ecosystem
- Portfolio Intelligence
- Decision Guardian
- Wealth Intelligence
- Native Mobile Features
- Multi-Broker Connectivity
- Cloud Deployment