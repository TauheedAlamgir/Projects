
/**
 * Creates a instance where all the items in each room can be
 *
 * @author Tauheed Alamgir 101194927
 * @version March 5, 2022
 */
public class Item
{
    // instance variables
    public String name;
    public String description;
    public double weight;

    /**
     * Constructor for objects of class Item
     * @param weight This will be the weight of the item
     */
    public Item(String name, String description, double weight)
    {
        // initialise instance variables
        this.name = name;
        this.description = description;
        this.weight = weight;
    }

    /**
     * Returns detailed description about the item using its weight and
     * description
     *
     * @param description This will be the description of the item
     * @return    the sum of x and y
     */
    public String getDescription()
    {
        // put your code here
        return description + " that weighs" + weight + " " + "kg.";
    }
    
    /**
     * Returns the items name
     */
    public String ItemName(){
        return name;
    }
}
