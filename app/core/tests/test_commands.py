"""
Tests for django commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

"""Этот декоратор заменяет метод check класса Command на объект-имитацию,
    который передается в тестовый метод как patched_check"""
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Tests commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db is ready."""
        """Здесь мы указываем, что имитация метода check должна
            возвращать True, когда она вызвана"""
        patched_check.return_value = True

        """Мы вызываем команду wait_for_db, которая в своем коде будет
            вызывать метод check"""
        call_command('wait_for_db')

        """Мы проверяем, что метод check был вызван один раз и с аргументом
            databases=['default']"""
        patched_check.assert_called_once_with(databases=['default'])
