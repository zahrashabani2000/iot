from django.test import TestCase
from django.utils import timezone
from ..models.scan import Scan


class ScanTestCase(TestCase):
    def setUp(self):
        self.s1 = Scan.objects.create(uuid=123, time_register=timezone.now())
        self.s2 = Scan.objects.create(
            uuid=123, time_register=timezone.now() - timezone.timedelta(days=1))

    def test_scan_created_and_saved_correctly(self):
        s3 = Scan.objects.create(
            uuid=789, time_register=timezone.now() - timezone.timedelta(days=2))
        self.assertEqual(Scan.objects.count(), 3)
        self.assertIn(s3, Scan.objects.all())

    def test_scan_ordering(self):
        scans = Scan.objects.all()
        self.assertEqual(scans.first().uuid, self.s2.uuid)
        self.assertEqual(scans.last().uuid, self.s1.uuid)

    def test_scan_str_representation(self):
        self.assertEqual(str(self.s1), str(self.s1.time_register))

    def test_scan_repr_representation(self):
        self.assertEqual(repr(self.s1), str(self.s1.time_register))
