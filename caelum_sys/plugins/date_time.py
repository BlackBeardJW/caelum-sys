"""
Date and time operations plugin for scheduling, timers, and temporal calculations.
"""

import datetime
import threading
import time

import pytz
from dateutil import parser

from caelum_sys.registry import register_command


@register_command("get current timestamp", safe=True)
def get_timestamp():
    """Get the current Unix timestamp."""
    timestamp = int(time.time())
    return f"⏰ Current timestamp: {timestamp}"


@register_command("what time is it in {timezone}", safe=True)
def get_time_in_timezone(timezone: str):
    """Get current time in a specific timezone."""
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.datetime.now(tz)
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        return f"🌍 Time in {timezone}: {formatted_time}"
    except pytz.exceptions.UnknownTimeZoneError:
        return f"❌ Unknown timezone: {timezone}. Try 'America/New_York', 'Europe/London', etc."
    except Exception as e:
        return f"❌ Error getting time: {e}"


@register_command("how many days until {date}", safe=True)
def days_until_date(date: str):
    """Calculate days until a specific date."""
    try:
        target_date = parser.parse(date).date()
        current_date = datetime.date.today()
        days_diff = (target_date - current_date).days

        if days_diff > 0:
            return f"📅 {days_diff} days until {target_date}"
        elif days_diff == 0:
            return f"📅 {target_date} is today!"
        else:
            return f"📅 {target_date} was {abs(days_diff)} days ago"
    except Exception as e:
        return f"❌ Error parsing date: {e}. Try formats like '2024-12-25' or 'December 25, 2024'"


@register_command("add {days} days to today", safe=True)
def add_days_to_today(days: int):
    """Add or subtract days from today's date."""
    try:
        current_date = datetime.date.today()
        new_date = current_date + datetime.timedelta(days=days)

        if days > 0:
            return f"📅 {days} days from today: {new_date}"
        elif days < 0:
            return f"📅 {abs(days)} days ago: {new_date}"
        else:
            return f"📅 Today: {new_date}"
    except Exception as e:
        return f"❌ Error calculating date: {e}"


@register_command("set timer for {minutes} minutes", safe=True)
def set_timer(minutes: int):
    """Set a countdown timer (non-blocking)."""
    try:
        if minutes <= 0:
            return "❌ Timer must be for a positive number of minutes"

        def timer_function():
            time.sleep(minutes * 60)
            print(f"⏰ TIMER: {minutes} minute timer is complete!")

        timer_thread = threading.Thread(target=timer_function, daemon=True)
        timer_thread.start()

        return f"⏰ Timer set for {minutes} minutes. You'll be notified when it's done."
    except Exception as e:
        return f"❌ Error setting timer: {e}"


@register_command("convert timestamp {timestamp}", safe=True)
def convert_timestamp(timestamp: int):
    """Convert Unix timestamp to human-readable date."""
    try:
        dt = datetime.datetime.fromtimestamp(timestamp)
        formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
        return f"📅 Timestamp {timestamp} = {formatted}"
    except Exception as e:
        return f"❌ Error converting timestamp: {e}"


@register_command("get day of week for {date}", safe=True)
def get_day_of_week(date: str):
    """Get the day of the week for a specific date."""
    try:
        target_date = parser.parse(date).date()
        day_name = target_date.strftime("%A")
        return f"📅 {target_date} is a {day_name}"
    except Exception as e:
        return f"❌ Error parsing date: {e}"


@register_command("format date {date} as {format}", safe=True)
def format_date(date: str, format: str):
    """Format a date string using Python strftime format."""
    try:
        parsed_date = parser.parse(date)
        formatted = parsed_date.strftime(format)
        return f"📅 Formatted date: {formatted}"
    except Exception as e:
        return (
            f"❌ Error formatting date: {e}. Try format like '%Y-%m-%d' or '%B %d, %Y'"
        )
