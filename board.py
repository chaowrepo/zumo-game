import sys, random
from PySide.QtCore import *
from PySide.QtGui import *

class Board(QWidget):
    def __init__(self, position, p1_name, p2_name):
        super(Board, self).__init__()
	self.player = 1
	self.position = position
	self.p1_name = p1_name
	self.p2_name = p2_name
        self.initUI() 	
    
    def set_player(self, player):
	self.player = player
	
    def get_player(self):
	return self.player
    
    def set_p1_name(self, player):
	self.p1_name = p1_name
	
    def get_p1_name(self):
	return self.p1_name    
    
    def set_p2_name(self, player):
	self.p2_name = p2_name
	
    def get_p2_name(self):
	return self.p2_name     
    
    def show_charecter(self):
        #set background
	self.BG_character_label = QLabel(self)
	background_pic = QPixmap(self.get_BG_character_path())
	self.BG_character_label.setPixmap(background_pic)	
	
        #icon character 1
        self.ch01 = QPushButton(QIcon(self.get_ch1_path()), 'Bin', self)
        self.ch01.setIconSize(self.icon_size())
        self.ch01.setMinimumSize(self.minimum_size())
        self.ch01.setGeometry(230, 50, 100, 30)
        self.ch01.clicked.connect(self.ch_info)
	
	#Label Skill of character 1
	self.skill_ch01 = QLabel(self)
	label_pic = QPixmap(self.get_label_skill_path())
	self.skill_ch01.setPixmap(label_pic)
	self.skill_ch01.setGeometry(200, 230, 200, 70)
	
	#Label name Skill of character 1
	self.name_skill_ch01 = QLabel(self)
	label_pic = QPixmap(self.get_label_skill_path())
	self.name_skill_ch01.setText('roll dice + 1')
	self.name_skill_ch01.setGeometry(290, 230, 200, 70)
        
        #icon character 2
        self.ch02 = QPushButton(QIcon(self.get_ch2_path()), 'Tor', self)
        self.ch02.setIconSize(self.icon_size())
        self.ch02.setMinimumSize(self.minimum_size())
        self.ch02.setGeometry(600, 50, 100, 30)        
        self.ch02.clicked.connect(self.ch_info)	
	
	#Label Skill of character 2
	self.skill_ch02 = QLabel(self)
	label_pic = QPixmap(self.get_label_skill_path())
	self.skill_ch02.setPixmap(label_pic)
	self.skill_ch02.setGeometry(570, 230, 200, 70)
	
	#Label name Skill of character 1
	self.name_skill_ch02 = QLabel(self)
	label_pic = QPixmap(self.get_label_skill_path())
	self.name_skill_ch02.setText('move back - 1')
	self.name_skill_ch02.setGeometry(650, 230, 200, 70)	

        #icon character 3
        self.ch03 = QPushButton(QIcon(self.get_ch3_path()), 'Med', self)
        self.ch03.setIconSize(self.icon_size())
        self.ch03.setMinimumSize(self.minimum_size())
        self.ch03.setGeometry(420, 300, 100, 30)        
        self.ch03.clicked.connect(self.ch_info)  
	
	#Label Skill of character 3
	self.skill_ch03 = QLabel(self)
	label_pic = QPixmap(self.get_label_skill_path())
	self.skill_ch03.setPixmap(label_pic)
	self.skill_ch03.setGeometry(390, 480, 200, 70)	

	#Label name Skill of character 3
	self.name_skill_ch03 = QLabel(self)
	label_pic = QPixmap(self.get_label_skill_path())
	self.name_skill_ch03.setText('  stone block \n(Chance 50%)')
	self.name_skill_ch03.setGeometry(475, 480, 200, 70)	

	#Button ok
	self.ok = QPushButton('OK', self)
	self.ok.move(800, 500)
	self.ok.clicked.connect(self.ch_info) 	
	self.ok.hide()        	
    
    def initUI(self):
	self.init_position()
        self.setGeometry(200, 100, 1000, 600) 
	self.setFixedSize(1000, 600)
        
	self.show_charecter()

        #self.setGeometry(200, 100, 1000, 600) 
        self.setWindowTitle('Choose Character')	

	#Show position
	self.main_label = QLabel(self)
	main_pic = QPixmap(self.get_main_progress_path())
	self.main_label.setPixmap(main_pic)
	self.main_label.move(-10, 398)
	self.main_label.hide()
	self.p1_label = QLabel(self)
	p1_pic = QPixmap(self.get_player1_progress_path())
	self.p1_label.setPixmap(p1_pic)
	self.p1_label.move(-900, 398)
	self.p1_label.hide()
	self.p2_label = QLabel(self)
	p2_pic = QPixmap(self.get_player2_progress_path())
	self.p2_label.setPixmap(p2_pic)
	self.p2_label.move(800, 398)
	self.p2_label.hide()
	
	#Background image
	self.background_label = QLabel(self)
	background_pic = QPixmap(self.get_background_farm_path())
	self.background_label.setPixmap(background_pic)
	self.background_label.move(0, 0)
	self.background_label.hide()
		
        #Show roll dice value
        self.roll_dice_label = QLabel(self)
        self.roll_dice_label.move(450, 5)
        self.roll_dice_label.hide()
	
        #Button to roll dice	
        self.btn = QPushButton('Random 2', self)
        self.btn.move(450, 500)
        self.btn.clicked.connect(self.roll_dice)

	self.btn.setAutoFillBackground(True)
	self.btn.setIconSize(self.icon_size())
        self.btn.hide()	
	
	#Button to roll dice 2	
        self.btn2 = QPushButton('Random 1', self)
        self.btn2.move(330, 500)
        self.btn2.clicked.connect(self.roll_dice)

	self.btn2.setAutoFillBackground(True)
	self.btn2.setIconSize(self.icon_size())
        self.btn2.hide()
	
	#Button to roll dice 3	
        self.btn3 = QPushButton('Random 3', self)
        self.btn3.move(570, 500)
        self.btn3.clicked.connect(self.roll_dice)

	self.btn3.setAutoFillBackground(True)
	self.btn3.setIconSize(self.icon_size())
        self.btn3.hide()	
	
	
	#Show player name
	self.p1_name_label = QLabel(self)	
	self.p1_name_label.move(250, 330)
	font = QFont()
	font.setPointSize(28)
	self.p1_name_label.setFont(font)
	self.p1_name_label.hide()
	self.p2_name_label = QLabel(self)
	self.p2_name_label.move(700, 330)
	self.p2_name_label.setFont(font)
	self.p2_name_label.hide()
	
	#Now player
	self.now_player1_label = QLabel(self)	
	self.now_player1_label.move(180, 490)
	font = QFont()
	font.setPointSize(28)
	self.now_player1_label.setFont(font)
	self.now_player1_label.setText('Player 1')
	self.now_player2_label = QLabel(self)
	#self.now_player1_label.hide()
	
	self.now_player2_label.move(680, 490)
	font = QFont()
	font.setPointSize(28)
	self.now_player2_label.setFont(font)
	self.now_player2_label.setText('Player 2')
	self.now_player2_label.hide()
		
	#Show image of each player
	self.pic1_label = QLabel(self)
	self.pic1_label.move(30, 150)
	self.pic1_label.hide()
	self.pic2_label = QLabel(self)
	self.pic2_label.move(800, 150)
	self.pic2_label.hide()	
	
	#Show who win
	self.win_label = QLabel(self)
	win_pic = QPixmap(self.get_p1_win_path())
	self.win_label.setPixmap(win_pic)
	self.win_label.move(200, 250)
	self.win_label.hide()	
	#self.win_label.show()
	
	#Show skill
	font = QFont()
	font.setPointSize(26)	
	self.skill2_label = QLabel(self)	
	self.skill2_label.move(445, 110)
	self.skill2_label.setFont(font)
	self.skill2_label.setText('+ set skill')		
	self.skill2_label.hide()	
	
	#Show position of each player
	font = QFont()
	font.setPointSize(18)	
	self.pos1_label = QLabel(self)
	self.pos1_label.setFont(font)
	self.pos1_label.move(80, 415)
	self.pos1_label.setText('00')
	self.pos1_label.hide()
	self.pos2_label = QLabel(self)
	self.pos2_label.setFont(font)
	self.pos2_label.move(900, 415)
	self.pos2_label.setText('00')
	self.pos2_label.hide()		

	self.show()    
	
    def move_player_image(self):
	pos1 = self.check_current_position(1)
	self.pic1_label.move(30 + (pos1*52), 150)
	pos2 = self.check_current_position(2)
	self.pic2_label.move(800 - ((11-pos2)*52), 150)
            
    def show_player_image(self):
	self.pic1_label.setPixmap(self.p1_pic)
	self.pic2_label.setPixmap(self.p2_pic)
	
    def show_position_of_player(self): 
	pos1 = self.check_current_position(1)
	self.pos1_label.setText(str(pos1))
	pos2 = self.check_current_position(2)
	self.pos2_label.setText(str(11-pos2))	
			
    '''
	Control all even
    '''    
    def roll_dice(self):	   	
    	self.skill2_label.hide()	
    	now_position = self.check_current_position(self.player)
    	dice = self.random_position()
    	self.show_roll_dice_value(dice)
    	dice = self.get_real_dice(self.player, dice)
    	now_position = self.move_forward(dice, now_position, self.player)
        player_win = self.check_win(self.position)
        win = self.show_win(player_win)
    	if(win == True):
	    if win == 1 or win == 2:
		#self.show_win(player_win)
		self.now_player1_label.hide()
		self.now_player2_label.hide()		
	    self.update_progress()
	    self.show_position_of_player()
	    self.move_player_image()
	    self.swapPlayer()
    		
    def update_progress(self):
        p1_position = self.check_current_position(1)
        self.p1_label.move((p1_position*53)-900, 398)
        p2_position = self.check_current_position(2)
        self.p2_label.move(800-((11-p2_position)*53), 398)
    
    @staticmethod
    def random_position():
        return random.randint(1, 3) 
      
    def show_roll_dice_value(self, dice):
	if dice == 1:
	    roll_dice_pic = QPixmap(self.get_number1_image_path())
	    self.roll_dice_label.setPixmap(roll_dice_pic) 
	     
	elif dice == 2:
	    roll_dice_pic = QPixmap(self.get_number2_image_path())
	    self.roll_dice_label.setPixmap(roll_dice_pic) 	     
	else:
	    roll_dice_pic = QPixmap(self.get_number3_image_path())
	    self.roll_dice_label.setPixmap(roll_dice_pic)	    
	self.roll_dice_label.show()
	
    #move position of character
    def move_forward(self, point, now_position, player):
        if(player == 1):
            for i in range(0,point):
            	if(now_position+i <=11):
                	self.position[now_position+i] = 1
            now_position = now_position+point
        else:
            for i in range(0,point):
            	if(now_position-i >=0):
                	self.position[now_position-i] = 2
            now_position = now_position-point
        return now_position
    def show_win(self, player_win):
    	if (player_win == 1):
    		self.win_label.show()
    		win_pic = QPixmap(self.get_p1_win_path())
    		self.win_label.setPixmap(win_pic)		    
    		self.pic2_label.clear()
    		self.btn.hide()
		self.btn2.hide()
		self.btn3.hide()
		self.now_player2_label.hide()
    		return 1
    	elif (player_win == 2):
    		self.win_label.show()
    		win_pic = QPixmap(self.get_p2_win_path())
    		self.win_label.setPixmap(win_pic)	    
    		self.pic1_label.clear()
    		self.btn.hide()
		self.btn2.hide()
		self.btn3.hide()
		self.now_player1_label.hide()
    		return 2
    	else:
    		return True
	    	    	
    def check_win(self, position):
    	p1_win = [1]*12
    	p2_win = [2]*12
    	if(position == p1_win):
    		return 1
    	elif(position == p2_win):
    		return 2
    	else:
    		return False

    def check_current_position(self, player):
	"""
	check now player position
	"""
	if(player == 1):
            i = 0
            while(self.position[i] == 1 and i <11):
                i+=1
        else:
            i = 11
            while(self.position[i] == 2 and i >=0):
                i-=1
        return i	

    #switch player
    #self.count = 1
    def swapPlayer(self):
        if(self.player == 1):
            self.player = 2
	    self.now_player2_label.show()
	    self.now_player1_label.hide()
        else:
            self.player = 1
	    self.now_player1_label.show()
	    self.now_player2_label.hide()	    
    
    #get value from player
    def ch_info(self):
        ch_select = self.sender()
        text = ch_select.text()
	self.select_character(text)
	
    """
    Set player's picture ,name and call show bolder method
    """
    def select_character(self, text):
        if(text == 'Bin'):
            if(self.player == 1):
                self.p1_pic = QPixmap("images/ch_1-1.png")
                self.p1_name = text
		self.show_is_selected_P1(text)
            else:
                self.p2_pic = QPixmap("images/ch_1-2.png")        
                self.p2_name = text
		self.show_is_selected_P2(text)
            self.swapPlayer()
        elif(text == 'Tor'):
            if(self.player == 1):
                self.p1_pic = QPixmap("images/ch_2-1.png")
                self.p1_name = text
		self.show_is_selected_P1(text)
            else:
                self.p2_pic = QPixmap("images/ch_2-2.png")        
                self.p2_name = text
		self.show_is_selected_P2(text)
            self.swapPlayer()
        elif(text == 'Med'):
            if(self.player == 1):
                self.p1_pic = QPixmap("images/ch_3-1.png")
                self.p1_name = text  
		self.show_is_selected_P1(text)
            else:
                self.p2_pic = QPixmap("images/ch_3-2.png")        
                self.p2_name = text  
		self.show_is_selected_P2(text)
            self.swapPlayer()
        if(self.p1_name != '' and self.p2_name != ''): 
	    self.ok.show()
	    self.hide_dont_selected(self.p1_name,self.p2_name)
	    if(text == 'OK'):
		self.show_player_image()     
		self.show_panel_2()	    
		self.setWindowTitle('~SUMO-GAME~')
  
    """
    Hide character is don't selected
    """
    def hide_dont_selected(self,name_1,name_2):
	if(name_1 == 'Med' and name_2 == 'Tor' 
	   or name_2 == 'Med' and name_1 == 'Tor'):
	    self.ch01.hide()
	    self.skill_ch01.hide()
	    self.name_skill_ch01.hide()	    
	elif(name_1 == 'Bin' and name_2 == 'Med' 
	     or name_2 == 'Bin' and name_1 == 'Med'):
	    self.ch02.hide()
	    self.skill_ch02.hide()
	    self.name_skill_ch02.hide()	    
	else:
	    self.ch03.hide()
	    self.skill_ch03.hide()
	    self.name_skill_ch03.hide()	    
    """
    Show Bolder on character is selected by player 1
    """
    def show_is_selected_P1(self,text):
	self.Frame_p1_label = QLabel(self)
	Flame_pic = QPixmap(self.get_frame_P1_path())
	self.Frame_p1_label.setPixmap(Flame_pic)
	if(text == 'Bin'):
	    self.Frame_p1_label.setGeometry(225, 30, 200, 200)
	elif(text == 'Tor'):
	    self.Frame_p1_label.setGeometry(595, 30, 200, 200)
	else:
	    self.Frame_p1_label.setGeometry(415, 280, 200, 200)
	self.Frame_p1_label.show()

    """
    Show Bolder on character is selected by player 2
    """	    
    def show_is_selected_P2(self,text):
	self.Frame_p2_label = QLabel(self)
	Flame_pic = QPixmap(self.get_frame_P2_path())
	self.Frame_p2_label.setPixmap(Flame_pic)
	if(text == 'Bin'):
	    self.Frame_p2_label.setGeometry(225, 30, 200, 200)
	elif(text == 'Tor'):
	    self.Frame_p2_label.setGeometry(595, 30, 200, 200)
	else:
	    self.Frame_p2_label.setGeometry(415, 280, 200, 200)
	self.Frame_p2_label.show()
    
    def show_panel_2(self):
	self.ch01.hide()
	self.ch02.hide()
	self.ch03.hide()
	self.ok.hide()
	self.Frame_p2_label.hide()
	self.Frame_p1_label.hide()	
	self.main_label.show()
	self.p1_label.show()
	self.p2_label.show()
	self.background_label.show()
	self.btn.show()
	self.btn2.show()
	self.btn3.show()
	
	self.p2_name_label.setText(self.p2_name)
	self.p1_name_label.setText(self.p1_name)	
	self.p2_name_label.show()
	self.p1_name_label.show()
	
	self.pos1_label.show()	
	self.pos2_label.show()
	
	self.pic1_label.show()
	self.pic2_label.show()
	
	self.now_player1_label.show()
	

    @staticmethod
    def random_stone_skill():
        return random.randint(1, 2) 
    
    def check_crash(self):
	for i in range(len(self.position)-1):
	    if self.position[i] == 1 and self.position[i+1] == 2:
		return True
	return False
	
    def get_real_dice(self, player, dice):
	if player == 1:
	    if self.p1_name == 'Bin':
		if self.p2_name == 'Tor':
		    if self.check_crash():
			self.skill2_label.show()
			self.skill2_label.setText('+ Block')
			return dice-1
		    else:
			self.skill2_label.show()
			self.skill2_label.setText('+ Move')			
			return dice + 1
		elif self.p2_name == 'Med':
		    if self.check_crash():
			skill = self.random_stone_skill()
			if skill == 1:
			    self.skill2_label.show()
			    self.skill2_label.setText('+ Stone')
			    return 0
			else:
			    self.skill2_label.show()
			    self.skill2_label.setText('+ Move')			    
			    return dice + 1
		    else:
			self.skill2_label.show()
			self.skill2_label.setText('+ Move')			
			return dice + 1
		elif self.p2_name == 'Bin':
		    self.skill2_label.show()
		    self.skill2_label.setText('+ Move')		    
		    return dice + 1 
	    elif self.p1_name == 'Tor' or self.p1_name == 'Med':
		if self.p2_name == 'Tor':
		    if self.check_crash():
			self.skill2_label.show()
			self.skill2_label.setText('+ Block')
			return dice-1
		    else:
			return dice
		elif self.p2_name == 'Med':
		    if self.check_crash():
			skill = self.random_stone_skill()
			if skill == 1:
			    self.skill2_label.show()
			    self.skill2_label.setText('+ Stone')
			    return 0
			else:
			    return dice
		    else:
			return dice
		elif self.p2_name == 'Bin':
		    return dice			
	    
	elif player == 2:
	    if self.p2_name == 'Bin':
		if self.p1_name == 'Tor':
		    if self.check_crash():
			self.skill2_label.show()
			self.skill2_label.setText('+ Block')
			return dice-1
		    else:
			self.skill2_label.show()
			self.skill2_label.setText('+ Move')			
			return dice + 1
		elif self.p1_name == 'Med':
		    if self.check_crash():
			skill = self.random_stone_skill()
			if skill == 1:
			    self.skill2_label.show()
			    self.skill2_label.setText('+ Stone')			    
			    return 0
			else:
			    self.skill2_label.show()
			    self.skill2_label.setText('+ Move')			    
			    return dice + 1
		    else:
			self.skill2_label.show()
			self.skill2_label.setText('+ Move')			
			return dice + 1
		elif self.p1_name == 'Bin':
		    self.skill2_label.show()
		    self.skill2_label.setText('+ Move')		    
		    return dice + 1 
	    elif self.p2_name == 'Tor' or self.p2_name == 'Med':
		if self.p1_name == 'Tor':
		    if self.check_crash():
			self.skill2_label.show()
			self.skill2_label.setText('+ Block')
			return dice-1
		    else:
			return dice
		elif self.p1_name == 'Med':
		    if self.check_crash():
			skill = self.random_stone_skill()
			if skill == 1:
			    self.skill2_label.show()
			    self.skill2_label.setText('+ Stone')
			    return 0
			else:
			    return dice
		    else:
			return dice
		elif self.p1_name == 'Bin':
		    return dice	
	
    @staticmethod 
    def icon_size():
	return QSize(130, 130)
    
    @staticmethod
    def minimum_size():
	return QSize(170, 170)   
    
    def init_position(self):
	self.position[0] = 0
	self.position[11] = 0
	
    @staticmethod
    def get_ch1_path():
	return 'images/ch_1-1.png'
    
    @staticmethod
    def get_ch2_path():
	return 'images/ch_2-1.png'
    
    @staticmethod
    def get_ch3_path():
	return 'images/ch_3-1.png' 
    
    @staticmethod
    def get_main_progress_path():
	return 'images/main_progress.png' 
    
    @staticmethod
    def get_player1_progress_path():
	return 'images/player1_progress.png'
    
    @staticmethod
    def get_player2_progress_path():
	return 'images/player2_progress.png'
    
    @staticmethod
    def get_background_farm_path():
	return 'images/background_farm.png' 

    @staticmethod
    def get_number1_image_path():
	return 'images/number1.png' 
    
    @staticmethod  
    def get_number2_image_path():
	return 'images/number2.png'
    
    @staticmethod
    def get_number3_image_path():
	return 'images/number3.png' 

    @staticmethod
    def get_p1_win_path():
	return 'images/p1_win.png'   
    @staticmethod
    
    def get_p2_win_path():
	return 'images/p2_win.png'     

    @staticmethod
    def get_BG_character_path():
	return 'images/BG_character.png'     
   
    @staticmethod
    def get_frame_P1_path():
	return 'images/frame_ch1.png'      

    @staticmethod
    def get_frame_P2_path():
	return 'images/frame_ch2.png'
    
    @staticmethod
    def get_label_skill_path():
	return 'images/label.png'