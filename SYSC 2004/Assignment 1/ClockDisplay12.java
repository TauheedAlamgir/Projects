
/**
 * Tauheed Alamgir 101194927
 * The ClockDisplay class implements a digital clock display for a
 * European-style 24 hour clock. The clock shows hours and minutes. The 
 * range of the clock is 00:00 (midnight) to 23:59 (one minute before 
 * midnight).
 * 
 * The clock display receives "ticks" (via the timeTick method) every minute
 * and reacts by incrementing the display. This is done in the usual clock
 * fashion: the hour increments when the minutes roll over to zero.
 * 
 */
public class ClockDisplay12
{
    private NumberDisplay hours;
    private NumberDisplay minutes;
    private String displayString;    // simulates the actual display
    private String AM = "a.m.";
    private String PM = "p.m.";
    private String AMorPM; // Creates variable for a.m. or p.m.
    
    /**
     * Constructor for ClockDisplay12 objects. This constructor 
     * creates a new clock set at 00:00.
     */
    public ClockDisplay12()
    {
        hours = new NumberDisplay(12); // 12 changes to 0
        minutes = new NumberDisplay(60); // 60 changes to 0
        AMorPM = AM; //Sets AMorPM to AM as the clock starts as "0:00a.m."
        updateDisplay();
    }

    /**
     * Constructor for ClockDisplay12 objects. This constructor
     * creates a new clock set at the time specified by the 
     * parameters.
     */
    public ClockDisplay12(int hour, int minute, String amPm)
    {
        hours = new NumberDisplay(12); // 12 changes to 0
        minutes = new NumberDisplay(60); // 60 changes to 0
        setTime(hour, minute, amPm); 
    }

    /**
     * This method should get called once every minute - it makes
     * the clock display go one minute forward.
     */
    public void timeTick()
    {
        minutes.increment(); // Increments time by one minute
        if(minutes.getValue() == 00) {  // it just rolled over!
            hours.increment(); // Increments time by an hour
            if(AMorPM.equals(AM)){
                AMorPM = PM; // Once time finishes a.m. its starts p.m.
            }
            else{
                AMorPM = AM; // Once time finishes p.m. its starts a.m.
            }
        }
        updateDisplay();
    }

    /**
     * Set the time of the display to the specified hour and
     * minute.
     */
    public void setTime(int hour, int minute, String amPm)
    {
        hours.setValue(hour); // User inputs hour value
        minutes.setValue(minute); // User inputs minute value
        if(hour == 0){
            hour = 12; /**If user inputed value for hour is 0 we automate
                        the system to change it to 12 and its respective
                        a.m. or p.m. */
        }
        if(amPm.equals(AM)){
            AMorPM = AM; // If user inputs AM then AMorPM equals to a.m.
        }
        else{
            AMorPM = PM; // If user inputs PM then AMorPM equals to p.m.
        }
        updateDisplay();
    }

    /**
     * Return the current time of this display in the format HH:MM.
     */
    public String getTime()
    {
        return displayString; // Returns current values of the Clock
    }
    
    /**
     * Update the internal string that represents the display.
     */
    private void updateDisplay()
    {
        String hour = hours.getDisplayValue(); // New variable for hour
        if(hour.equals("00")){
            hour = "12"; // If hour is 00 then change it to 12
        }
        displayString = hour + ":" + minutes.getDisplayValue() + AMorPM;
        // Displays as "hour:minutes a.m./p.m.
    }
}
