import Tkinter
import paho.mqtt.client as mqtt

port = 1883
host = "" # please change the IP address based on the address of Hono instance.
username = "sensor1@DEFAULT_TENANT"
password = "hono-secret"
speed = 380
client = mqtt.Client(client_id="python_client", clean_session=True, userdata=None, protocol=4, transport="tcp")
topic_to_publish = "telemetry"
topic_to_subscribe = "control/+/+/req/#"



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    # added only to test.
    client.subscribe(topic_to_subscribe)
    print("Subscribed to topic "+ str(topic_to_subscribe))
    #client.subscribe("rover/1/RoverCore/usage")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+ str(msg.payload))


def connect():
    client.reinitialise(client_id="python_client",clean_session=True, userdata=None)
    client.username_pw_set(username,password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.connect(host, port, 60)
    client.loop_start()
    print("Trying to connect to the broker.")
    
def disconnect():
    client.disconnect()
    client.loop_stop()
    print("Disconnected from Broker")

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def turn_right():
    client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"E\",\"speed\":"+ str(speed_var.get() + 360) +" }", 0 ,False)
    print("turn right clicked")

def turn_right_back():
    client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"D\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
    print("turn right back clicked")

def turn_left():
   client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"Q\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
   print("turn left clicked")

def turn_left_back():
   client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"A\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
   print("turn left back clicked")

def move_forward():
   client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"W\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
   print("move forward clicked")

def move_back():
   client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"S\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
   print("move back clicked")

def spot_right():
   client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"K\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
   print("move spot right clicked")

def spot_left():
   client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"J\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
   print("move spot left clicked")

def stop_move():
   client.publish(topic_to_publish,"{\"mode\":0,\"command\":\"F\",\"speed\": "+ str(speed_var.get() + 360) +" }", 0 ,False)
   print("Stop clicked")

def set_speed(event):
   #client.publish(topic_to_publish,"Setspeed = "+ str(speed_var.get()) , 0 ,False)
   speed = speed_var.get() + 360
   print("set speed to %d", speed)

# UI widgets definition below.
if __name__ == "__main__":
   parent = Tkinter.Tk()
   #variable for speed setting
   speed_var = Tkinter.DoubleVar()
   parent.title("Rover MQTT mocker")

   B_connect = Tkinter.Button(parent, text ="Connect" , command= connect)
   B_disconnect = Tkinter.Button(parent, text ="Disconnect" , command= disconnect)
   #B_right = Tkinter.Button(parent, text =">" , command= turn_right)
   #B_right_back = Tkinter.Button(parent, text =">" , command= turn_right_back)
   #B_left  = Tkinter.Button(parent, text ="<", command= turn_left)
   #B_left_back  = Tkinter.Button(parent, text ="<", command= turn_left_back)
   #B_up = Tkinter.Button(parent, text ="^", command= move_forward)
   #B_down = Tkinter.Button(parent, text ="v", command= move_back)
   #B_stop = Tkinter.Button(parent, text ="Stop", command= stop_move)
   #B_spot_right = Tkinter.Button(parent, text =">(", command= spot_right)
   #B_spot_left = Tkinter.Button(parent, text ="<)", command= spot_left)
   #speed_label = Tkinter.Label(parent , text = "Speed")
   #speed_scale = Tkinter.Scale(parent, variable = speed_var,orient = Tkinter.HORIZONTAL)
   #speed_scale.bind("<ButtonRelease-1>", set_speed)

   B_connect.place(x = 100 , y = 30 , height = 25 , width = 75)
   B_disconnect.place(x = 100 , y = 60 , height = 25 , width = 75)
   #B_right.place(x = 65, y= 25, height=25, width=25)
   #B_right_back.place(x = 65, y= 55, height=25, width=25)
   #B_left.place(x= 15,y = 25, height=25, width=25)
   #B_left_back.place(x= 15,y = 55, height=25, width=25)
   #B_up.place(x= 40, y = 10 ,  height=25, width=25)
   #B_down.place(x= 40, y = 70, height=25, width=25)
   #speed_label.place(x= 10, y = 105, height=50, width=50)
   #speed_scale.place(x= 60, y = 105, height=50, width=85)
   #B_stop.place(x = 10,y = 160 , height = 30, width=85)
   #B_spot_left.place(x = 100,y = 160 , height = 30, width=35)
   #B_spot_right.place(x = 140,y = 160 , height = 30, width=35)
   
   parent.mainloop()
