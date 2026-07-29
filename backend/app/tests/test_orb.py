from app.decision_engine.orb import SigmaticsOrb
from app.decision_engine.status import OrbStatus


def test_orb_initializes() -> None:

    orb = SigmaticsOrb()

    orb.start()

    assert orb.status == OrbStatus.IDLE


def test_orb_executes_empty_pipeline() -> None:

    orb = SigmaticsOrb()

    orb.start()

    context = orb.execute()

    assert context is not None

    assert orb.status == OrbStatus.IDLE