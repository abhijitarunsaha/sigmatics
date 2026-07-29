# Notification Experience

## Purpose

Sigmatics notifications deliver high-confidence, time-sensitive trading opportunities while preserving complete user control over trade execution.

Notifications are designed to inform, not automate.

Every notification represents a quantified trading decision that is:

- Explainable
- Time-bound
- Versioned
- Replayable
- User-approved before execution

Notifications shall never place trades directly.

---

# Design Principles

The notification experience follows these principles:

1. Decision-first, not alert-first.
2. High signal, low noise.
3. Human confirmation is mandatory.
4. Every recommendation is time-bound.
5. Recommendations remain explainable.
6. Recommendations may expire when market conditions change.
7. User trust takes precedence over execution speed.
8. Notifications shall present executable recommendations rather than intermediate strategy outputs.

---

# Notification Contents

Every trading notification shall display:

- Recommended Instrument
    - Underlying Index
    - Expiry
    - Strike Price
    - Option Type

Example:

BANKNIFTY • 28 JUL • 56100 CE

- Recommended Entry Price
- Recommended Stop Loss
- Recommended Target
- Opportunity Score
- Confidence Score
- Remaining Recommendation Validity (TTL)

Example Notification

----------------------------------------------------

SIGMATICS DECISION

BANKNIFTY • 28 JUL • 56100 CE

Entry      ₹186.20
SL         ₹175.20
Target     ₹208.00

🟢 Opportunity 96
🎯 Confidence 92%
⏱ Valid 01:42

          [ REVIEW & EXECUTE ]

               [ DISMISS ]

----------------------------------------------------

# Notification Behaviour

Selecting **Review & Execute** shall:

1. Launch the Sigmatics application.
2. Validate that the recommendation is still valid.
3. Validate broker session.
4. Validate available capital.
5. Validate market conditions.
6. Open the Execution Review screen.

Broker execution shall never occur directly from the notification.

---

# Recommendation Time-To-Live (TTL)

Every recommendation shall contain:

- Decision ID
- Generated Timestamp
- Expiration Timestamp
- Remaining Validity

Recommendations are only actionable while valid.

If the recommendation expires before user confirmation, Sigmatics shall:

1. Notify the user that the recommendation has expired.
2. Re-evaluate current market conditions.
3. Generate a fresh recommendation if appropriate.

---

# Notification Lifecycle

Recommendation Generated

↓

Published

↓

Delivered

↓

Viewed

↓

Review Requested

↓

Execution Review

↓

Executed

or

Cancelled

or

Dismissed

or

Expired

---

# Silent Updates

# Recommendation Updates

# Recommendation Expiry

# Recommendation Superseded

# Review & Execute

# Execute Anyway

# Refresh Recommendation

# Compliance Principles

Notifications shall never:

- Place trades automatically.
- Bypass user confirmation.
- Circumvent broker authentication.
- Override regulatory requirements.

All executions require explicit user approval.