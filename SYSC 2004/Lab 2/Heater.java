/** Tauheed Alamgir 101194927
 * A Heater models a simple space-heater. The operations provided by a Heater
 * object are:
 * 1. Increase and decrease the temperature setting by a set amount.
 * 2. Return the current temperature setting.
 * 3. Change the set amount by which the temperature is increased and lowered.
 * 
 * @author L.S. Marshall, SCE, Carleton University
 * (incomplete implementation for SYSC 2004 Lab 2)
 * Tauheed Alamgir 101194927
 * @version 1.03 September 9th, 2022
 */
public class Heater
{
    /** The temperature setting that the heater should maintain. */
    private int temperature;
    
    /** The temperature setting for a newly created heater. */
    private static final int INITIAL_TEMPERATURE = 15;
    
    /** 
     * The amount by which the temperature setting is raised/lowered when
     * warmer() and cooler() are invoked.
     */
     private int increment;
    
    /** 
     * The default amount by which the temperature setting is 
     * increased when warmer() is invoked and decreased when cooler()
     * is invoked.
     */
    private static final int DEFAULT_INCREMENT = 5;
    
    /** The maximum and minimum values the temperature can be */
    /** We create two variables max and min which are both integers */
    private static final int MAXIMUM_TEMPERATURE = 100;
    private static final int MINIMUM_TEMPERATURE = 0;
    private int max;
    private int min;
    
    /**
     * Constructs a new Heater with an initial temperature setting of 15
     * degrees, and which increments and decrements the temperature
     * setting in increments of 5 degrees.
     */
    public Heater()
    {
        temperature = INITIAL_TEMPERATURE;
        increment = DEFAULT_INCREMENT;
        max = MAXIMUM_TEMPERATURE;/**Initializes max to the maximum 
        temperature which is 100*/
        min = MINIMUM_TEMPERATURE;/**Initializes min to the minimum 
        temperature which is 0*/
    }
 
    /**
     * Initializes the temperature and increment values again.
     * Initializes min and max to minTemp and maxTemp.
     */    
    public Heater(int minTemp, int maxTemp)
    {
        temperature = INITIAL_TEMPERATURE;
        increment = DEFAULT_INCREMENT;
        max = maxTemp;
        min = minTemp;
    }

    /**
     * Returns the current value that is stored in temperature.
     */    
    public int temperature()
    {
        return temperature;
    }
    
    /**
     * Adds the temperature value to the value store in increment with a 
     * maximum of 100.
     */
    public void warmer()
    {
        if ((temperature + increment) <= max){/**Makes sure the increment
            is below 100*/
            temperature = temperature + increment;/**Adds increment value
            to the current stored value in temperature*/
        }
    }

    /**
     * Subtracts the temperature value to the value store in increment with
     * a minimum of 0.
     */    
    public void cooler()
    {
        if ((temperature - increment) >= min){/**Makes sure the increment
            is above 0*/
            temperature = temperature - increment;/**Subtracts increment
            value from the current stored value in temperature*/
        }
    }
    
    
    /**
     * Allows user to change the increment value to the desired value.
     */    
    public void setIncrement(int newIncrement)
    {
        if (newIncrement > 0){/**Makes sure increment values are above 0*/
            increment = newIncrement;/**Assigns new increment value to the
                                        increment variable*/
        }
        }
    }

