from app.decision_engine.models.decision_journal import DecisionJournal
from app.decision_engine.models.decision_journal_entry import (
    DecisionJournalEntry,
)


class ReasoningRecorder:

    def __init__(
        self,
        journal: DecisionJournal,
    ) -> None:

        self._journal = journal

    def record(
        self,
        entry: DecisionJournalEntry,
    ) -> None:

        self._journal.add(entry)