from __future__ import annotations

from dataclasses import dataclass, field

from app.decision_engine.models.decision_journal_entry import (
    DecisionJournalEntry,
)


@dataclass(slots=True)
class DecisionJournal:

    entries: list[DecisionJournalEntry] = field(
        default_factory=list,
    )

    def add(
        self,
        entry: DecisionJournalEntry,
    ) -> None:

        self.entries.append(entry)

    def pretty_print(self) -> str:

        lines: list[str] = []

        lines.append("=" * 60)
        lines.append("Decision Journal")
        lines.append("=" * 60)

        if not self.entries:

            lines.append("No journal entries recorded.")

            return "\n".join(lines)

        total = len(self.entries)

        for index, entry in enumerate(
            self.entries,
            start=1,
        ):

            lines.append("")
            lines.append(
                f"Stage {index} of {total}"
            )

            lines.append("-" * 60)

            lines.append(
                f"Stage           : {entry.stage}"
            )

            lines.append(
                f"Status          : {entry.status}"
            )

            if entry.decision_state:

                lines.append(
                    f"Decision State  : {entry.decision_state}"
                )

            if entry.evidence_bucket_id:

                lines.append(
                    f"Evidence Bucket : {entry.evidence_bucket_id}"
                )

            lines.append("Observations")

            for observation in entry.observations:

                lines.append(
                    f"  • {observation}"
                )

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)