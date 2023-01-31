import java.util.*;

/**
 * Class Room - a room in an adventure game.
 *
 * This class is part of the "World of Zuul" application. 
 * "World of Zuul" is a very simple, text based adventure game.  
 *
 * A "Room" represents one location in the scenery of the game.  It is 
 * connected to other rooms via exits.  For each existing exit, the room 
 * stores a reference to the neighboring room.
 * 
 * @author  Michael Kolling and David J. Barnes
 * @version 2006.03.30
 * 
 * @author Tauheed Alamgir 101194927
 * @version March 5, 2022
 */

public class Room 
{
    private String description;
    private HashMap<String, Room> exits;    // stores exits of this room.
    public static final ArrayList<Room> rooms =new ArrayList<Room>();
    public ArrayList<Item> items;

    /**
     * Create a room described "description". Initially, it has
     * no exits. "description" is something like "a kitchen" or
     * "an open court yard".
     * 
     * @param description The room's description.
     */
    public Room(String description) 
    {
        this.description = description;
        exits = new HashMap<String, Room>();
        items = new ArrayList<Item>();
        rooms.add(this);
    }

    /**
     * Define an exit from this room.
     * 
     * @param direction The direction of the exit
     * @param neighbour The room to which the exit leads
     */
    public void setExit(String direction, Room neighbour) 
    {
        exits.put(direction, neighbour);
    }

    /**
     * Returns a short description of the room, i.e. the one that
     * was defined in the constructor
     * 
     * @return The short description of the room
     */
    public String getShortDescription(){
        return description;
    }

    /**
     * Return a long description of the room in the form:
     *     You are in the kitchen.
     *     Exits: north west
     *     
     * @return A long description of this room
     */
    public String getLongDescription(){
        return "You are " + description + ".\n" + getExitString()
                + "\nItems:" + getItems();
    }

    /**
     * Return a string describing the room's exits, for example
     * "Exits: north west".
     * 
     * @return Details of the room's exits
     */
    private String getExitString(){
        String returnString = "Exits:";
        Set<String> keys = exits.keySet();
        for(String exit : keys) {
            returnString += " " + exit;
        }
        return returnString;
    }

    /**
     * Return the room that is reached if we go from this room in direction
     * "direction". If there is no room in that direction, return null.
     * 
     * @param direction The exit's direction
     * @return The room in the given direction
     */
    public Room getExit(String direction) {
        return exits.get(direction);
    }
    
    /**
     * Adds items to room
     * @param addItem adds items to a list
     */
    public void addItem(Item item){
        items.add(item);
    }
    
    /**
     * Returns the items and description for user
     * @param getItems gets the descriptions
     */
    private String getItems() {
        StringBuilder temp = new StringBuilder();
        for (Item i : items) {
            temp.append("\n" + i.getDescription());
        }
        return temp.toString(); 
    }
    
    /**
     * User picks up item
     * @param Picks up item
     */
    public Item TakeItem(String item){
        for(Item i : items) {
            if(item.equals(i.ItemName())){
                items.remove(i);
                return i;
            }
        }
        return null;
    }
    
    /**
     * Allows user to drop a item
     * @param Drop an item
     */
    public void DropItem(Item item){
        items.add(item);
    }
    
    /**
     * Adds items to a list
     * @param add item
     */
    public void AddItem(Item item){
        items.add(item);
    }
    
    /**
     * Creates rooms
     */
    static public ArrayList<Room> GetRooms()
    {
        return rooms;
    }
}

