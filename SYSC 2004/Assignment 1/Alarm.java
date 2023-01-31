
/**
 * We are creating an alarm system that we can set time and turn on or off.
 *
 * @author Tauheed Alamgir 101194927
 * @version January 28, 2022
 */
public class Alarm
{
    // instance variables - replace the example below with your own
    private ClockDisplay12 alarm;
    private boolean alarm_state;

    /**
     * Constructor for objects of class Alarm
     */
    public Alarm()
    {
        // initialise instance variables
        alarm = new ClockDisplay12(); // Opens a new clock
        alarm_state = false; // Sets alarm to "off" from the start
    }

    /**
     * Constructor for objects of class Alarm and creating variables for
     * the alarm
     */
    public Alarm(int hours,int minutes,String AMorPM,boolean alarmOnOff)
    {
        alarm = new ClockDisplay12(hours, minutes, AMorPM);
        // Opens the time input prompt
        alarm_state = alarmOnOff;/** Sets alarm_state value in this case
                                    which is false to alarmOnOff */
    }
    
    /** 
     * Allows the user to set input alarm time
     */
    public void setTime(int hours, int minutes, String AMorPM){
        alarm.setTime(hours, minutes, AMorPM);
        // Allows user to set alarm time
    }
    
    /**
     * Sets the boolean value of true to the alarm
     */
    public void turnOn(){
        alarm_state = true; // Alarm is on 
    }
    
    /**
     * Sets the boolean value of false to the alarm
     */
    public void turnOff(){
        alarm_state = false; // Alarm is off 
    }
    
    /** 
     * Allows user to view the set alarm time
     */
    public String getTime(){
        return alarm.getTime(); // Shows what user put as set alarm time
    }
    
    /**
     * Uses boolean vaalue to let user know if the alarm has been set or 
     * not
     */
    public boolean isSet(){
        return alarm_state; // Lets user know if the alarm has been set 
    }    
}
