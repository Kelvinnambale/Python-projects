from plyer import notification  
import psutil  
      
      
def check_battery_status(battery, plugged):  
          
        if plugged:  
            percent = battery.percent  
            if percent <= 80:  
                notification.notify(  
                    # title of notification  
                    title="Charger Plugged In",  
          
                    # message of notification  
                    message=" To get the better battery life, charge upto 80%",  
          
                    # displaying time  
                    timeout=2  
                )  
          
            elif percent == 100:  
                notification.notify(  
                    title="Charger Plugged In",  
                    message=" Please plugged out the charger. Battery is charged",  
                    timeout=2  
                )  
          
            else:  
                notification.notify(  
                    title="Charger Plugged In",  
                    message=" Remove the charger please. For better battery life charge up to 80%",  
                    timeout=2  
                )  
          
        else:  
            percent = battery.percent  
            if percent <= 20:  
                notification.notify(  
                    title="Battery Reminder",  
                    message="Your battery is running low. You might want to plug in your PC ",  
                    timeout=2  
                )  
          
            elif percent <= 50:  
                notification.notify(  
                    title="Battery Reminder",  
                    message=f" Battery is {percent}.",  
                    timeout=2  
                )  
          
            elif percent == 100:  
                notification.notify(  
                    title="Battery Reminder",  
                    message="Your System is Fully charged",  
                    timeout=2  
                )  
          
            else:  
                notification.notify(  
                    title="Battery Reminder",  
                    message=f"Battery is {percent}",  
                    timeout=2  
                )  
      
      
    # this method returns a tuple  
battery = psutil.sensors_battery()  
      
    # check power is plugged or not  
plugged = battery.power_plugged  
      
      
print(check_battery_status(battery, plugged))  