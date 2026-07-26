# Functional Requirements

## CAP-002 — Broker Connectivity (BRC)

---

## Overview

The Broker Connectivity capability provides a secure, broker-agnostic integration layer between Sigmatics and supported brokerage platforms.

It is responsible for establishing and maintaining authenticated broker sessions, synchronizing trading data, routing trading requests, and monitoring broker connectivity.

Broker Connectivity abstracts all broker-specific implementations behind a common integration contract, ensuring that the rest of the platform remains independent of individual brokerage APIs.

---

# Functional Area 1 – Broker Discovery

### FR-BRC-001

**Capability:** CAP-002 – Broker Connectivity (BRC)

**Category:** CORE

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall present users with a list of supported brokerage platforms that can be linked to their Sigmatics account.

---

### FR-BRC-002

**Category:** UI

**Priority:** High

**Status:** Approved

**Description**

The platform shall display the connection status of every linked brokerage account.

---

### FR-BRC-003

**Category:** UI

**Priority:** Medium

**Status:** Approved

**Description**

The platform shall display broker-specific information including broker name, linked account identifier and last successful synchronization time.

---

# Functional Area 2 – Broker Authentication

### FR-BRC-004

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall authenticate brokerage accounts using the broker's official authentication mechanism.

---

### FR-BRC-005

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall never request or permanently store brokerage account passwords.

---

### FR-BRC-006

**Category:** SEC

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall securely maintain broker authorization credentials required for accessing approved broker services.

---

### FR-BRC-007

**Category:** SEC

**Priority:** High

**Status:** Approved

**Description**

The platform shall detect expired broker authorizations and request users to reconnect their brokerage account.

---

### FR-BRC-008

**Category:** INT

**Priority:** High

**Status:** Approved

**Description**

The platform shall support multiple linked brokerage accounts under a single Sigmatics identity.

---

# Functional Area 3 – Market Data Access

### FR-BRC-009

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall retrieve market data using the broker-authorized data access mechanism.

---

### FR-BRC-010

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall synchronize holdings, positions, margins and orders from linked brokerage accounts.

---

### FR-BRC-011

**Category:** INT

**Priority:** High

**Status:** Approved

**Description**

The platform shall periodically synchronize broker account information to maintain data consistency.

---

# Functional Area 4 – Order Management

### FR-BRC-012

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall submit trade orders only after explicit user confirmation.

---

### FR-BRC-013

**Category:** CMP

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall prevent fully autonomous trade execution without explicit user authorization.

---

### FR-BRC-014

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall support order placement using market, limit and other broker-supported order types.

---

### FR-BRC-015

**Category:** INT

**Priority:** High

**Status:** Approved

**Description**

The platform shall allow users to modify eligible pending orders.

---

### FR-BRC-016

**Category:** INT

**Priority:** High

**Status:** Approved

**Description**

The platform shall allow users to cancel eligible pending orders.

---

### FR-BRC-017

**Category:** INT

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall continuously monitor the execution status of submitted broker orders.

---

# Functional Area 5 – Trade Synchronization

### FR-BRC-018

**Category:** CORE

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall synchronize executed trades with the Sigmatics Trade Management capability.

---

### FR-BRC-019

**Category:** CORE

**Priority:** High

**Status:** Approved

**Description**

The platform shall synchronize broker positions following every confirmed execution.

---

### FR-BRC-020

**Category:** CORE

**Priority:** High

**Status:** Approved

**Description**

The platform shall synchronize broker account margins and available funds.

---

# Functional Area 6 – Connection Management

### FR-BRC-021

**Category:** OPS

**Priority:** High

**Status:** Approved

**Description**

The platform shall continuously monitor the health of broker connectivity.

---

### FR-BRC-022

**Category:** OPS

**Priority:** High

**Status:** Approved

**Description**

The platform shall automatically retry transient broker communication failures where appropriate.

---

### FR-BRC-023

**Category:** UI

**Priority:** High

**Status:** Approved

**Description**

The platform shall clearly notify users whenever broker connectivity is interrupted.

---

# Functional Area 7 – Audit & Compliance

### FR-BRC-024

**Category:** CMP

**Priority:** Critical

**Status:** Approved

**Description**

The platform shall maintain an immutable audit trail for all broker authentication and order submission events.

---

### FR-BRC-025

**Category:** REP

**Priority:** Medium

**Status:** Approved

**Description**

The platform shall record synchronization history for every linked brokerage account.

---

# Functional Area 8 – Broker Capability Discovery

### FR-BRC-026

**Category:** INT

**Priority:** Future

**Status:** Approved

**Description**

The platform shall maintain a capability profile for every supported brokerage platform to enable broker-agnostic behaviour across the application.

---

### FR-BRC-027

**Category:** INT

**Priority:** Future

**Status:** Approved

**Description**

The platform shall identify and expose broker-supported order types, including but not limited to Market, Limit, Stop Loss and Stop Loss Market orders.

---

### FR-BRC-028

**Category:** INT

**Priority:** Future

**Status:** Approved

**Description**

The platform shall identify supported product types, including Intraday, Delivery and other broker-supported products.

---

### FR-BRC-029

**Category:** INT

**Priority:** Future

**Status:** Approved

**Description**

The platform shall maintain metadata describing broker-specific operational capabilities including API availability, session expiry behaviour, supported exchanges and applicable rate limits.

---

### FR-BRC-030

**Category:** CORE

**Priority:** Future

**Status:** Approved

**Description**

The platform shall dynamically adapt available trading functionality based on the capabilities of the currently connected brokerage platform.

---

# Business Rules

BR-BRC-001

A brokerage account shall be linked to only one Sigmatics account at any given time.

---

BR-BRC-002

Broker authentication shall always occur using the broker's officially supported authentication mechanism.

---

BR-BRC-003

Sigmatics shall never execute trades without explicit user confirmation.

---

BR-BRC-004

Historical trading records imported into Sigmatics shall remain available even if a brokerage account is later disconnected.

---

BR-BRC-005

Failure of one linked brokerage account shall not affect the connectivity or operation of other linked brokerage accounts.

---

BR-BRC-006

Broker-specific implementation details shall remain encapsulated within the Broker Connectivity capability and shall not propagate into Market Intelligence, Trading Intelligence or Trade Management.

---

## Capability Summary

| Functional Area | Requirements |
|-----------------------------|-------------:|
| Broker Discovery | 3 |
| Broker Authentication | 5 |
| Market Data Access | 3 |
| Order Management | 6 |
| Trade Synchronization | 3 |
| Connection Management | 3 |
| Audit & Compliance | 2 |
| Broker Capability Discovery | 5 |
| **Total** | **30 Requirements** |