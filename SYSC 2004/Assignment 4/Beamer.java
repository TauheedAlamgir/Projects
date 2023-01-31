
/**
 * Write a description of class Beamer here.
 *
 * @author Tauheed Alamgir 101194927
 * @version 03/19/2022
 */
public class Beamer extends Item
{
    private boolean isCharged;
    private Room ChargedRoom;
    /**
     * Constructor for objects of class Beamer
     */
    public Beamer(String name, String description, double weight) {
        super(name, description, weight);
        isCharged = false;
        ChargedRoom = null;
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public String getDescription() {
        return super.getDescription();
    }
    
    /**
     * Gets the name 
     */
    public String getName() {
        return super.ItemName();
    }
    
    /**
     * Returns true or false for if the beamer is charged or not
     */
    public boolean isCharged() {
        return isCharged;
    }
    
    /**
     * Lets user know if beamer is charged
     */
    public void charge(Room currentRoom) {
        if(!isCharged){
            ChargedRoom = currentRoom;
            isCharged = true;
            System.out.println("Beamer has been charged");
        }
        else {
            System.out.println("Beamer is already Charged");
        }
    }
    
    /**
     * Fires the beamer and memorized the location
     */
    public Room fire() {
        if(isCharged){
            System.out.println("Beamer has been fired");
            isCharged = false;
            return ChargedRoom;
        }
        else {
            System.out.println("Beamer is not charged");
            return null;
        }
    }
}
