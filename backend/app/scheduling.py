"""Scheduling for relay switches."""
from datetime import datetime
from enum import Enum

from app.config import relayBoardAdapter


class Repeat(str, Enum):
    """Enumeration for repeat values."""

    every_day = "every_day"
    weekdays = "weekdays"
    weekends = "weekends"
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"


def task_switch_relay(
    relay_position: int, on: bool
):
    """Trigger function to switch relays.

    :param relay_position:
    :param on:
    :return:
    """
    print(f"position:{relay_position} on:{on}, {datetime.now()}]")
    if on:
        relayBoardAdapter.on(relay_position)
    else:
        relayBoardAdapter.off(relay_position)
