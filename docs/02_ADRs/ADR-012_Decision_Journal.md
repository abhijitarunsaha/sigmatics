## Status

Accepted

## Context

Sigmatics is designed as an explainable AI-assisted decision platform.

Every recommendation must answer:

Why was this recommendation made?
Which intelligence layers participated?
What evidence was considered?
Why was another opportunity rejected?
Why did confidence increase or decrease?
Why did the recommendation expire?

Capturing only the final recommendation is insufficient.

The reasoning process itself is a first-class business artifact.

## Decision

Sigmatics introduces two distinct concepts:

Decision Recorder

A runtime service responsible for capturing reasoning events during an evaluation cycle.

## Responsibilities:

Receive observations from Decision Stages
Create structured journal entries
Maintain an in-memory Decision Journal
Freeze the journal when evaluation completes
Hand the completed journal to the persistence layer

The Recorder does not decide.

It observes.

Decision Journal

The immutable record of how a Decision Package was produced.

A Decision Journal contains:

evaluation id
timestamps
executed stages
evidence references
observations
decision transitions
confidence evolution
reasoning notes

Once a Decision Package is finalized:

The Decision Journal becomes immutable.

## Consequences

Advantages

Complete explainability
SEBI audit support
Historical replay
Backtesting
User trust
AI learning
Notification reasoning
Decision evolution analysis

Trade-offs

Slight increase in memory usage
Additional persistence requirements

These are considered acceptable.

## Not a Log File

A Decision Journal is not:

application logging
debugging output
telemetry
tracing

It is business reasoning.

## Consumers

The journal is consumed by:

Explainability Agent
Notification Service
Decision Guardian
Historical Analytics
Backtesting Engine
Portfolio Intelligence
AI Learning
Audit