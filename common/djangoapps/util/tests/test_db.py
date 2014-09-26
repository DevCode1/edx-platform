"""Tests for util.db module."""

import ddt
import threading
import time
import unittest

from django.contrib.auth.models import User
from django.db import connection, IntegrityError
from django.db.transaction import commit_on_success
from django.test import TransactionTestCase

from util.db import commit_on_success_with_read_committed


@ddt.ddt
class TransactionIsolationLevelsTestCase(TransactionTestCase):
    """
    Tests the effects of changing transaction isolation level to READ COMMITTED instead of REPEATABLE READ.

    Note: This TestCase only works with MySQL.

    To run it on devstack:
    1. Add TEST_RUNNER = 'django_nose.NoseTestSuiteRunner' to envs/devstack.py
    2. Run "./manage.py lms --settings=devstack test util.tests.test_db"
    """

    @ddt.data(
        (commit_on_success, IntegrityError, None, True),
        (commit_on_success_with_read_committed, type(None), False, True),
    )
    @ddt.unpack
    def test_concurrent_requests(self, transaction_decorator, exception_class, created_in_1, created_in_2):
        """
        Test that when isolation level is set to READ COMMITTED get_or_create()
        for the same row in concurrent requests does not raise an IntegrityError.
        """

        if connection.vendor != 'mysql':
            raise unittest.SkipTest('Only works on MySQL.')

        def request(status, delay):
            """A dummy request."""
            try:
                with self.assertRaises(User.DoesNotExist):
                    User.objects.get(username='s1', email='s1@l.com')

                if delay > 0:
                    time.sleep(delay)

                __, created = User.objects.get_or_create(username='s1', email='s1@l.com')
            except Exception as exception:  # pylint: disable=broad-except
                status['exception'] = exception
            else:
                status['created'] = created

        thread1_status = {}
        thread2_status = {}
        thread1 = threading.Thread(target=transaction_decorator(request), args=(thread1_status, 1))
        thread2 = threading.Thread(target=transaction_decorator(request), args=(thread2_status, 0))

        thread1.start()
        thread2.start()
        thread2.join()
        thread1.join()

        self.assertIsInstance(thread1_status.get('exception'), exception_class)
        self.assertEqual(thread1_status.get('created'), created_in_1)

        self.assertIsNone(thread2_status.get('exception'))
        self.assertEqual(thread2_status.get('created'), created_in_2)
