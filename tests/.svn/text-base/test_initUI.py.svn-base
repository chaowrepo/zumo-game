import sys, os
import board, shutil
from board import Board
from PySide.QtCore import QSize
from start_project import *
from unittest import TestCase

class test_initUI(TestCase):
    def test_icon_size(self):
        #Act
        icon = Board.icon_size()
        #Assert
        self.assertEquals(QSize(130, 130),icon)
        
    def test_minimum_size(self):
        #Act
        minimum = Board.minimum_size()
        #Assert
        self.assertEquals(QSize(170, 170),minimum)
        
    def test_init_position(self):
        #Arrange
        position = [0] * 12
        board = Board(position, '', '')
        #Act
        board.init_position()
        #Assert
        self.assertEquals(position[0],0) 
        self.assertEquals(position[11],0)
        
    def test_get_ch1_path(self):
        #Act
        path = Board.get_ch1_path()
        #Arrange
        self.assertTrue(os.path.exists(path))
    
    def test_get_ch2_path(self):
        path = Board.get_ch2_path()
        self.assertTrue(os.path.exists(path))
        
    def test_get_ch3_path(self):
        #Act
        path = Board.get_ch3_path()
        #Assert
        self.assertTrue(os.path.exists(path))
        
    def test_get_main_progress_path(self):
        #Act
        path = Board.get_main_progress_path()
        #Assert
        self.assertTrue(os.path.exists(path)) 
        
    def test_player1_progress_path(self):
        #Act
        path = Board.get_player1_progress_path()
        #Assert
        self.assertTrue(os.path.exists(path))
        
    def test_get_player2_progress_path(self):
        #Act
        path = Board.get_player2_progress_path()
        #Assert
        self.assertTrue(os.path.exists(path)) 
        
    def test_get_background_farm_path(self):
        #Act
        path = Board.get_background_farm_path()
        #Assert
        self.assertTrue(os.path.exists(path))        
        
    def test_get_number1_image_path(self):
        #Act
        path = Board.get_number1_image_path()
        #Assert
        self.assertTrue(os.path.exists(path))  
 
    def test_get_number2_image_path(self):
        #Act
        path = Board.get_number2_image_path()
        #Assert
        self.assertTrue(os.path.exists(path))  
 
    def test_get_number3_image_path(self):
        #Act
        path = Board.get_number3_image_path()
        #Assert
        self.assertTrue(os.path.exists(path)) 
        
    def test_get_p1_win_path(self):
        #Act
        path = Board.get_p1_win_path()
        #Assert
        self.assertTrue(os.path.exists(path))

    def test_get_p2_win_path(self):
        #Act
        path = Board.get_p2_win_path()
        #Assert
        self.assertTrue(os.path.exists(path))         