import sys, random
import start_project, shutil
from unittest import TestCase

class test_start_Project(TestCase):
    def test_start_project(self):
        # Arrange
        shutil.copyfile('start_project.py', 'start_project.tmp')
        # Act
        # Assert        
        try:
            with open('start_project.tmp') as stream:
                content = stream.read()
                self.assertTrue("main()" in content)
        except IOError:
            self.fail('start_project not have main to run program')
    
    def check_length_position(self):
        # Arrange
        for i in range (len(position)):
            print i

