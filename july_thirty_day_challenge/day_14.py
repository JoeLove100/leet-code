"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
"""


def get_angle(hours: int,
              minutes: int) -> float:

    min_hand = 6 * minutes
    hour_hand = 30 * (hours % 12) + minutes / 2
    diff = abs(hour_hand - min_hand)

    return min(diff, 360 - diff)


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return get_angle(hour, minutes)
