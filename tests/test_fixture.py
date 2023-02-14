import pytest

from models.events import EventUpdate


@pytest.fixture
def event() -> EventUpdate:
    return EventUpdate(
        title="Example",
        image="https://cats.ru/cat.png",
        description="Look it my cat!",
        tags=["python", "fastapi", "cat", "launch"],
        location="Ru"
    )


def test_event_name(event: EventUpdate) -> None:
    assert event.title == "Example"
