from django.test import TestCase
from django.utils import timezone
from ..models.scan import Scan


class ScanTestCase(TestCase):
    
    """
    This code defines a ScanTestCase class inherited from the Django TestCase class. 
    It tests various aspects of the Scan model's functionalities such as creation,
    ordering, string representation, and representation. The setUp() method is
    used to create two instances of the Scan model for testing purposes, one 
    with a current time register, and the other with a time register from a 
    day earlier. The underlying methods are:
    
    test_scan_created_and_saved_correctly(): 
        This method tests whether a new instance of the model can be created
        and saved correctly to the database and whether the count of instances 
        is equal to the expected count.
        
    test_scan_ordering(): 
        This method tests whether the ordering of the Scan instances is correct
        and whether the ordering is descending.
        
    test_scan_str_representation(): 
        This method tests whether the string representation of the Scan instance 
        is correct and whether it displays the time register in string format.
    
    test_scan_repr_representation(): 
        This method tests whether the representation of the Scan instance is 
        correct and whether it displays the time register in string format.
        
    All the tests defined in these methods are assertions, 
    which compare the actual results with the expected results.
    """
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
