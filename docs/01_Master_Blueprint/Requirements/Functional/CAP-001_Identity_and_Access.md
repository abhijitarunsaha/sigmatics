## CAP-001 — Identity & Access (IAM)

---

## Overview

The Identity & Access capability establishes the foundational identity of every Sigmatics user. It governs authentication, authorization, user profiles, compliance acknowledgements, trading preferences and session management.

Every user interacting with Sigmatics shall possess a unique Sigmatics identity independent of any connected brokerage account.

---

# Functional Area 1 – User Registration

### FR-IAM-001

**Capability:** CAP-001 – Identity & Access (IAM)

**Category:** CORE

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall provide each user with a unique Sigmatics account that serves as the primary identity for accessing all platform capabilities, preferences, reports, portfolios and linked brokerage accounts.

**Acceptance Criteria**

- Every registered user receives a unique immutable Sigmatics User ID.
- Sigmatics identity remains independent of brokerage accounts.
- One Sigmatics account may be linked with multiple supported brokerage accounts.
- User identity persists even if no brokerage account is linked.

**Traceability**

Business Capability:
- CAP-001

Related ADRs:
- ADR-002
- ADR-004
- ADR-005 (Proposed)

---

### FR-IAM-002

**Category:** CORE

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall support user registration using either a verified email address or a verified mobile number.

**Acceptance Criteria**

- Registration supports email-based verification.
- Registration supports mobile OTP verification.
- Duplicate registrations using the same verified identity are prevented.

---

### FR-IAM-003

**Category:** SEC

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall verify the ownership of the supplied email address or mobile number before activating a Sigmatics account.

---

### FR-IAM-004

**Category:** CORE

**Priority:** High

**Status:** Approved

**Description**

The platform shall allow users to complete their profile during registration or at a later time.

---

# Functional Area 2 – Authentication

### FR-IAM-005

**Category:** SEC

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall authenticate users before granting access to protected resources.

---

### FR-IAM-006

**Category:** SEC

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall support authentication using email/mobile number and password.

---

### FR-IAM-007

**Category:** SEC

**Priority:** High

**Status:** Approved

**Description**

The platform shall allow users to securely reset forgotten passwords using OTP verification.

---

### FR-IAM-008

**Category:** SEC

**Priority:** High

**Status:** Approved

**Description**

The mobile application shall support authentication using a user-defined 6-digit PIN after the initial successful login.

---

### FR-IAM-009

**Category:** SEC

**Priority:** Medium

**Status:** Approved

**Description**

The mobile application shall support biometric authentication (Fingerprint or Face ID) on compatible devices.

---

# Functional Area 3 – Session Management

### FR-IAM-010

**Category:** SEC

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall create an authenticated user session upon successful login.

---

### FR-IAM-011

**Category:** SEC

**Priority:** High

**Status:** Approved

**Description**

The platform shall automatically terminate inactive sessions after the configured timeout period.

---

### FR-IAM-012

**Category:** SEC

**Priority:** High

**Status:** Approved

**Description**

The platform shall allow users to explicitly sign out of active sessions.

---

### FR-IAM-013

**Category:** SEC

**Priority:** Medium

**Status:** Approved

**Description**

The platform shall invalidate all active sessions immediately following a successful password reset.

---

# Functional Area 4 – Compliance & Consent

### FR-IAM-014

**Category:** CMP

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall require users to accept the latest Terms of Service before enabling trading functionality.

---

### FR-IAM-015

**Category:** CMP

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall require users to acknowledge the Risk Disclosure before enabling trading functionality.

---

### FR-IAM-016

**Category:** CMP

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall require users to acknowledge the AI Recommendation Disclaimer before displaying trading recommendations.

---

### FR-IAM-017

**Category:** CMP

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall record the version, timestamp and user identity for every accepted legal or compliance document.

---

### FR-IAM-018

**Category:** CMP

**Priority:** High

**Status:** Approved

**Description**

The platform shall require users to accept updated versions of mandatory legal documents before continuing to use affected platform capabilities.

---

# Functional Area 5 – User Profile & Trading Preferences

### FR-IAM-019

**Category:** CORE

**Priority:** High

**Status:** Approved

**Description**

The platform shall maintain a user profile containing personal information, platform preferences and trading preferences.

---

### FR-IAM-020

**Category:** CORE

**Priority:** High

**Status:** Approved

**Description**

The platform shall allow users to configure Trading Preferences including:

- Preferred Index (NIFTY, BANKNIFTY, SENSEX)
- Default Trading Capital
- Default Risk Percentage
- Default Broker
- Theme Preference
- Notification Preferences

---

### FR-IAM-021

**Category:** UI

**Priority:** Medium

**Status:** Approved

**Description**

The platform shall provide users with the ability to update their profile and trading preferences at any time.

---

# Functional Area 6 – Linked Brokerage Accounts

### FR-IAM-022

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall allow users to link one or more supported brokerage accounts to their Sigmatics account through the broker's official authentication mechanism.

---

### FR-IAM-023

**Category:** INT

**Priority:** High

**Status:** Approved

**Description**

The platform shall maintain the connection status of every linked brokerage account.

---

### FR-IAM-024

**Category:** INT

**Priority:** High

**Status:** Approved

**Description**

The platform shall allow users to disconnect previously linked brokerage accounts without affecting their Sigmatics account.

---

# Functional Area 7 – Audit & Security

### FR-IAM-025

**Category:** SEC

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall maintain immutable audit records for authentication, authorization, profile updates and compliance acknowledgements.

---

### FR-IAM-026

**Category:** REP

**Priority:** Medium

**Status:** Approved

**Description**

The platform shall allow users to review their login history and compliance acknowledgement history.

---

## Capability Summary

| Functional Area | Requirements |
|-----------------|-------------:|
| User Registration | 4 |
| Authentication | 5 |
| Session Management | 4 |
| Compliance & Consent | 5 |
| User Profile & Trading Preferences | 3 |
| Linked Brokerage Accounts | 3 |
| Audit & Security | 2 |
| **Total** | **26 Requirements** |