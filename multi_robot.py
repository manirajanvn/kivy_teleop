from kivy.config import Config  
Config.set("graphics", "resizable", False)
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")
Config.set("graphics", "fullscreen", "false")
Config.set("input", "mouse", "mouse,disable_on_activity")
Config.set("kivy", "keyboard_mode", "systemanddock")

# kivy imports
from kivy.app import App 
from kivy.lang.builder import Builder  
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Grid_LayoutApp(App):
    title = 'Robot Window'
    def __init__(self):
        super().__init__()
        rclpy.init()
        node = rclpy.create_node('Grid_LayoutApp')
        self.publisher_ = node.create_publisher(Twist, 'cmd_vel', 10)
        self.publisher1_ = node.create_publisher(Twist, 'robot1/cmd_vel', 10)
        self.publisher2_ = node.create_publisher(Twist, 'robot2/cmd_vel', 10)
        self.robot= 'Robot 1'
        
    def build(self):
	
        # adding GridLayouts in App
        # Defining number of column
        # You can use row as well depends on need
        layout = RelativeLayout()
 
        manualbtn = Button(text ="Manual",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.10, 'y':0.5}
                )
        layout.add_widget(manualbtn)
        layout.add_widget(Button(text ="Auto \n Navigation",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.40, 'y':0.5}
                ))
        layout.add_widget(Button(text ="Person Follow",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.70, 'y':0.5}
                ))
        layout.add_widget(Button(text ="Settings",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.10, 'y':0.1}
                ))
        manualbtn.bind(on_press = self.onButtonPress)
        return layout
            
    def onButtonPress(self, button):
          
        layout = RelativeLayout()
        
        dropdown = DropDown()
        
        rob0 = Button(text ='No Name', size_hint_y = None, height = 40)
        rob0.bind(on_release = lambda rob0: dropdown.select(rob0.text))
        dropdown.add_widget(rob0)
        
        rob1 = Button(text ='Robot 1', size_hint_y = None, height = 40)
        rob1.bind(on_release = lambda rob1: dropdown.select(rob1.text))
        dropdown.add_widget(rob1)
        
        rob2 = Button(text ='Robot 2', size_hint_y = None, height = 40)
        rob2.bind(on_release = lambda rob2: dropdown.select(rob2.text))
        dropdown.add_widget(rob2)
        
        menu_btn = Button(text ="Select",font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (150, 50),
                    size_hint = (None, None),
                    pos_hint ={'x':0.70, 'y':0.90})
        menu_btn.bind(on_release = dropdown.open)
        dropdown.bind(on_select = lambda instance, x: setattr(menu_btn, 'text', x))
        layout.add_widget(menu_btn) 
        closeButton = Button(text ="Home",font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (150, 50),
                    size_hint = (None, None),
                    pos_hint ={'x':0.00, 'y':0.90})
  
        layout.add_widget(closeButton) 
        forward = Button(text ="Forward",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.40, 'y':0.6}
                )
        layout.add_widget(forward)
        backward = Button(text ="Backward",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.40, 'y':0.05}
                )
        layout.add_widget(backward)
        left = Button(text ="Left",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.10, 'y':0.3}
                )
        layout.add_widget(left)
        right = Button(text ="Right",
        	    font_size = 25,
        	    color = (0,0,0),
        	    bold = True,
                    background_normal = 'normal.png',
                    background_down = 'clicked.png',
                    border = (30, 30, 30, 30),                   
                    size= (200, 200),
                    size_hint = (None, None),
                    pos_hint ={'x':0.70, 'y':0.3}
                )
        layout.add_widget(right)      
  
        # Instantiate the modal popup and display
        popup = Popup(title ='Manual Navigation',
                      content = layout)  
        popup.open()   
  
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)
        forward.bind(on_press = self.forward)
        backward.bind(on_press = self.backward)
        left.bind(on_press = self.left)
        right.bind(on_press = self.right)
        rob0.bind(on_press = self.select_rob0)
        rob1.bind(on_press = self.select_rob1)
        rob2.bind(on_press = self.select_rob2)
        
        forward.bind(on_release = self.release)
        backward.bind(on_release = self.release)
        left.bind(on_release = self.release)
        right.bind(on_release = self.release)
        
        
    def forward(self, button):
        twist = Twist()
        twist.linear.x = 1.0
        self.publish_cmd_vel(twist)
        
    def backward(self, button):
        twist = Twist()
        twist.linear.x = -1.0
        self.publish_cmd_vel(twist)
        
    def left(self, button):
        twist = Twist()
        twist.angular.z = 0.5
        self.publish_cmd_vel(twist)
    
    def right(self, button):
        twist = Twist()
        twist.angular.z = -0.5
        self.publish_cmd_vel(twist)
    
    def release(self, button):
        twist = Twist()
        self.publish_cmd_vel(twist)
    
    def select_rob0(self, button):
        self.robot = 'No Name'
    
    def select_rob1(self, button):
        self.robot = 'Robot 1'
    
    def select_rob2(self, button):
        self.robot = 'Robot 2'
    
    def publish_cmd_vel(self, twist):
        if self.robot == 'No Name':
            self.publisher_.publish(twist)
        elif self.robot == 'Robot 1':
            self.publisher1_.publish(twist)
        elif self.robot == 'Robot 2':
            self.publisher2_.publish(twist)
        
if __name__ == "__main__":
    Grid_LayoutApp().run()
