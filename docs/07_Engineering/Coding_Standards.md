# Coding Standards

## Purpose

This document defines the engineering and coding standards adopted for the Sigmatics platform.

The objective is not only to ensure code consistency, but also to preserve the architectural vision, maintainability, explainability and long-term evolution of the platform.

These standards apply to all backend, frontend, AI, infrastructure and integration components.

---

# Engineering Philosophy

Sigmatics is an AI-driven Decision Intelligence Platform.

Every implementation shall prioritize:

- Simplicity over cleverness.
- Readability over brevity.
- Deterministic behaviour over hidden side-effects.
- Explainability over black-box logic.
- Composition over inheritance.
- Configuration over hardcoding.
- Contracts over assumptions.
- Evidence before execution.

Code should communicate intent before implementation.

---

# Core Engineering Principles

## Single Responsibility

Every class, module and function shall have a single clearly defined responsibility.

Avoid "God Classes".

Examples:

✓ DecisionEngine orchestrates decisions.

✓ MarketAssessment evaluates market state.

✓ NotificationService publishes notifications.

✗ DecisionEngine shall not directly call Broker APIs.

---

## Separation of Concerns

Business logic shall never be mixed with:

- UI
- Database
- HTTP
- Broker SDKs
- LLM Providers

The Decision Engine must remain framework independent.

---

## Dependency Direction

Dependencies shall always point inward.

Example:

React

↓

FastAPI

↓

Application

↓

Decision Engine

↓

Domain

The Domain Layer shall never depend on FastAPI, SQLAlchemy or React.

---

# Decision Engine Principles

The Decision Engine is the heart of Sigmatics.

It shall remain:

- Deterministic
- Stateless during execution
- Explainable
- Fully testable

Every stage shall:

Receive:

DecisionContext

Return:

DecisionContext

No stage shall mutate another stage's internal state.

---

## Stage Independence

Every Decision Stage shall:

- Perform one responsibility.
- Produce evidence.
- Never bypass another stage.
- Never communicate directly with sibling stages.

Communication occurs only through the DecisionContext.

---

## Evidence Driven Decisions

Every recommendation shall be traceable to supporting evidence.

No recommendation shall be produced solely from intuition, heuristics or AI-generated text.

Every recommendation must contain:

- Supporting evidence
- Confidence
- Risk assessment
- Explainability

---

# AI Agent Principles

AI Agents are specialized intelligence providers.

They shall:

- Never execute trades.
- Never directly call brokers.
- Never modify Decision Packages.

Agents provide evidence.

The Decision Engine constructs recommendations.

---

# Decision Package Principles

Decision Packages are immutable once published.

Changes shall create:

- A new Version

or

- A new Decision Package

Never silently overwrite history.

---

# Notification Principles

Notifications are representations of Decision Packages.

Notifications are never the source of truth.

The Decision Package remains authoritative.

---

# Human Governance

Sigmatics shall never perform autonomous trade execution.

Every execution requires explicit human confirmation.

The user remains the final decision maker.

---

# Configuration

Business rules shall be configuration driven wherever practical.

Avoid:

if confidence > 75

Prefer:

settings.minimum_confidence

Configuration examples:

- Confidence threshold
- TTL
- Risk tolerance
- Market timings
- Notification preferences

---

# Error Handling

Errors shall be:

- Meaningful
- Recoverable where possible
- Logged with sufficient context

Avoid swallowing exceptions.

Never expose internal implementation details to end users.

---

# Logging

Log important business events.

Examples:

- Recommendation Created
- Recommendation Updated
- Recommendation Expired
- Trade Executed
- Broker Failure
- User Override

Avoid excessive debug logging in production.

---

# Auditability

Every important business decision shall be auditable.

Examples:

- Recommendation Generation
- Execution Override
- Broker Submission
- Portfolio Recommendation
- Configuration Changes

Audit logs shall never be modified after creation.

---

# Naming Conventions

Names should represent business concepts.

Preferred:

DecisionPackage

MarketSnapshot

ConfidenceScore

TradeConstruction

MarketOpportunity

Avoid:

Manager

Helper

Utility

Processor

Thing

Object

---

# Function Design

Functions should:

- Perform one responsibility.
- Be easy to test.
- Minimize side effects.

Prefer:

Small composable functions.

Avoid:

Large methods exceeding approximately 50–75 lines without clear justification.

---

# Immutability

Prefer immutable domain models wherever practical.

MarketSnapshot

DecisionPackage

RecommendationEvidence

should be treated as immutable once created.

---

# Testing Philosophy

Every capability shall include automated tests.

Recommended hierarchy:

- Unit Tests
- Integration Tests
- Contract Tests
- End-to-End Tests

Critical business logic shall achieve high test coverage.

---

# Performance

Optimise only after measurement.

Prefer clean implementations first.

Premature optimisation shall be avoided.

Performance improvements shall never reduce explainability.

---

# Documentation

Public classes and modules shall include documentation describing:

- Purpose
- Responsibility
- Inputs
- Outputs

Complex algorithms should explain the reasoning behind implementation decisions.

---

# Architecture Compliance

No implementation shall bypass the architectural responsibilities defined in the Capability Specifications or ADRs.

Architectural deviations require an approved Architecture Decision Record (ADR).

---

# Security

Secrets shall never be committed to source control.

Credentials shall be supplied through environment configuration.

Sensitive information shall never be logged.

---

# Git Standards

Every Pull Request shall:

- Compile successfully.
- Pass automated tests.
- Pass linting.
- Include documentation updates where applicable.

Architecture changes require a corresponding ADR update.

---

# Code Review Checklist

Before approving code, reviewers should verify:

✓ Single Responsibility maintained

✓ Business logic separated from infrastructure

✓ No architectural layering violations

✓ Unit tests included

✓ Explainability preserved

✓ Configuration not hardcoded

✓ Logging appropriate

✓ Documentation updated

✓ Capability traceability maintained

---

# Sigmatics Engineering Principles

Every contribution should reinforce the following principles:

1. Evidence precedes Confidence.

2. Confidence precedes Execution.

3. WAIT is a valid recommendation.

4. Recommendations are living entities.

5. Humans make the final decision.

6. The Decision Engine orchestrates; Intelligence Domains provide evidence.

7. Every recommendation must be explainable.

8. Every important decision must be auditable.

9. Architecture should evolve through ADRs.

10. Code should be written for the next engineer, not just the current one.

---

# The Sigmatics Engineering Oath

> We build software that reasons before it reacts.

> We value evidence over assumption.

> We design for clarity before complexity.

> We preserve explainability over convenience.

> We respect human judgement over automation.

> We leave the codebase better than we found it.

> Every line of code should move Sigmatics closer to becoming a trusted Decision Intelligence Platform.