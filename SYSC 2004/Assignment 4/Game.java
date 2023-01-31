import java.util.*;
/**
 *  This class is the main class of the "World of Zuul" application. 
 *  "World of Zuul" is a very simple, text based adventure game.  Users 
 *  can walk around some scenery. That's all. It should really be extended 
 *  to make it more interesting!
 * 
 *  To play this game, create an instance of this class and call the "play"
 *  method.
 * 
 *  This main class creates and initialises all the others: it creates all
 *  rooms, creates the parser and starts the game.  It also evaluates and
 *  executes the commands that the parser returns.
 * 
 * @author  Michael Kolling and David J. Barnes
 * @version 2006.03.30
 * 
 * @author Tauheed Alamgir 101194927
 * @version March 5, 2022
 */

public class Game 
{
    private Parser parser;
    private Room currentRoom;
    private Stack<Room> BackStack;
    private Room PreviousRoom;
    private Item currentItem;
    private int HungerLevel;
    private Random random;
        
    /**
     * Create the game and initialise its internal map.
     */
    public Game() 
    {
        createRooms();
        parser = new Parser();
        currentItem = null;
        random = new Random();
        BackStack = new Stack<Room>();
        PreviousRoom = null;
        HungerLevel = 6;
    }

    /**
     * Create all the rooms and link their exits together.
     */
    private void createRooms()
    {
        Room outside, theatre, pub, lab, office, transport;
        Item Jug, Sofa, Table, Speaker, Laptop, Chair, Biryani;
        Beamer beamer;
      
        // create the rooms
        outside = new Room("outside the main entrance of the university");
        theatre = new Room("in a lecture theatre");
        pub = new Room("in the campus pub");
        lab = new Room("in a computing lab");
        office = new Room("in the computing admin office");
        transport = new Room("in the transport room");
        
        // create items
        Jug = new Item("Jug", "Water jug", 3);
        Sofa = new Item("Sofa", "Office sofa", 60);
        Table = new Item("Table", "Long table", 30);
        Speaker = new Item("Speaker", "JBL speaker", 1);
        Laptop = new Item("Laptop", " Lenovo laptop", 4);
        Chair = new Item("Chair", "Spinning Chair", 5);
        Biryani = new Item("Biryani", "Chicken Biryani", 65);
        beamer = new Beamer("beamer", "some beamer", 10);
        
        // add items to rooms
        outside.addItem(Table);
        outside.addItem(Speaker);
        outside.addItem(Biryani);
        outside.addItem(beamer);
        theatre.addItem(Table);
        theatre.addItem(Speaker);
        theatre.addItem(Chair);
        theatre.addItem(beamer);
        pub.addItem(Jug);
        pub.addItem(Speaker);
        pub.addItem(Chair);
        pub.addItem(beamer);
        lab.addItem(Table);
        lab.addItem(Laptop);
        lab.addItem(Chair);
        lab.addItem(beamer);
        lab.addItem(Biryani);
        office.addItem(Table);
        office.addItem(Chair);
        office.addItem(Sofa);
        office.addItem(Biryani);
        office.addItem(beamer);
        
        // initialise room exits
        outside.setExit("east", theatre);
        outside.setExit("south", lab);
        outside.setExit("west", pub);
        outside.setExit("north", transport);

        theatre.setExit("west", outside);

        pub.setExit("east", outside);

        lab.setExit("north", outside);
        lab.setExit("east", office);

        office.setExit("west", lab);

        currentRoom = outside;  // start game outside
    }

    /**
     *  Main play routine.  Loops until end of play.
     */
    public void play() 
    {            
        printWelcome();

        // Enter the main command loop.  Here we repeatedly read commands and
        // execute them until the game is over.
                
        boolean finished = false;
        while (! finished) {
            Command command = parser.getCommand();
            finished = processCommand(command);
        }
        System.out.println("Thank you for playing.  Good bye.");
    }

    /**
     * Print out the opening message for the player.
     */
    private void printWelcome()
    {
        System.out.println();
        System.out.println("Welcome to the World of Zuul!");
        System.out.println("World of Zuul is a new, incredibly boring adventure game.");
        System.out.println("Type 'help' if you need help.");
        System.out.println();
        System.out.println(currentRoom.getLongDescription());
    }

    /**
     * Given a command, process (that is: execute) the command.
     * 
     * @param command The command to be processed
     * @return true If the command ends the game, false otherwise
     */
    private boolean processCommand(Command command) 
    {
        boolean wantToQuit = false;

        if(command.isUnknown()) {
            System.out.println("I don't know what you mean...");
            return false;
        }

        String commandWord = command.getCommandWord();
        if (commandWord.equals("help")) {
            printHelp();
        }
        else if (commandWord.equals("go")) {
            goRoom(command);
        }
        else if (commandWord.equals("quit")) {
            wantToQuit = quit(command);
        }
        else if (commandWord.equals("look")) {
            look(command);
        }
        else if (commandWord.equals("eat")) {
            eat(command);
        }
        else if (commandWord.equals("back")) {
            back(command);
        }
        else if (commandWord.equals("take")) {
            take(command);
        }
        else if (commandWord.equals("drop")) {
            drop(command);
        }
        else if (commandWord.equals("fire")) {
            fire(command);
        }
        else if (commandWord.equals("charge")) {
            charge(command);
        }
        else if (commandWord.equals("stackBack")) {
            stackBack(command);
        }
        
        // else command not recognised.
        return wantToQuit;
    }

    // implementations of user commands:

    /**
     * Print out some help information.
     * Here we print a cryptic message and a list of the 
     * command words.
     */
    private void printHelp() 
    {
        System.out.println("You are lost. You are alone. You wander");
        System.out.println("around at the university.");
        System.out.println();
        System.out.println("Your command words are:");
        System.out.println(parser.getCommands());
    }

    /** 
     * Try to go to one direction. If there is an exit, enter the new
     * room, otherwise print an error message.
     * 
     * @param command The command to be processed
     */
    private void goRoom(Command command) 
    {
    if(!command.hasSecondWord()) {
            // if there is no second word, we don't know where to go...
            System.out.println("Go where?");
            return;
    }

        String direction = command.getSecondWord();

        // Try to leave current room.
        Room nextRoom = currentRoom.getExit(direction);

        if (nextRoom == null) {
            System.out.println("There is no door!");
        }
        else {
            currentRoom = nextRoom;
            PreviousRoom = currentRoom;
            BackStack.push(currentRoom);
            if(nextRoom.getShortDescription().equals("in the transport")){
                nextRoom = Room.rooms.get(random.nextInt(5));
            System.out.println(currentRoom.getLongDescription());
        }
    }
    }

    /** 
     * "Quit" was entered. Check the rest of the command to see
     * whether we really quit the game.
     * 
     * @param command The command to be processed
     * @return true, if this command quits the game, false otherwise
     */
    private boolean quit(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("Quit what?");
            return false;
        }
        else {
            return true;  // signal that we want to quit
        }
    }
    
    /**
     * Returns detailed description of the cuurent room
     * @param command It is the command that will be used
     */
    private void look(Command command){
        if(command.hasSecondWord()){
            System.out.println("Look what?");
        }
        else{
            System.out.println(currentRoom.getLongDescription());
            if(currentItem != null){
                System.out.println("You are carrying " + currentItem.ItemName());
            }
            else {
                System.out.println("You are not carrying an item");
            }
        }            
    }
    
    
    /**
     * Returns if the the user has eaten or not
     * @param command It is the command that will be used
     */
    private void eat(Command command){
        if(currentItem.ItemName().equals("Biryani")) {
            currentItem = null;
            HungerLevel = 1;
            System.out.println("You have eaten and currently have no food.");
        }
        else {
            System.out.println("No food.");
            }
    }
    
    /** 
     * Returns user to the room previously visited
     * @param command It is the command that will be used
     */
      private void back(Command command){
        if(command.hasSecondWord()){
            System.out.println("Back what?");
        }
        else {
            if(PreviousRoom == null){
                System.out.println("No rooms have been visited");
            }
            else {
                Room temp = currentRoom;
                PreviousRoom = temp;
                BackStack.push(temp);
                System.out.println(currentRoom.getLongDescription());
            }
        }
    }
    
    /** 
     * Allows users to go back one room at a time till the the beginning
     * of the game
     * @param command It is the command that will be used
     */
    private void stackBack(Command command){
        if(BackStack.empty()){
            System.out.println("hola what");
        }
        else{
        if(BackStack.empty()) {
            System.out.println(" previous room was not found");
        }
        else {
            Room temp = currentRoom;
            currentRoom = BackStack.pop();
            System.out.println(currentRoom.getLongDescription());
            }
        }
    }
    
    /**
     * Allows user to pick up a item.
     * @param command It is the command that will be used
     */
    private void take(Command command) 
    {
        if(!command.hasSecondWord()) {
            System.out.println("Take what?");
            return;
        }
        else {
            if(currentItem == null){
                String item = command.getSecondWord();
                Item pickedItem = currentRoom.TakeItem(item);
                if(pickedItem != null){
                    if(HungerLevel <= 5 || item.equals("Biryani")){
                        System.out.println("You picked up " + item);
                        currentItem = pickedItem;
                        HungerLevel = HungerLevel + 1;
                    }
                    else{
                        System.out.println("Eat some Biryani");
                    }
                }
                else{
                    System.out.println("Biryani is not in this room.");
                }
            }
            else{
                System.out.println("You are currently holding something.");
            }
        }
    }
    
    /**
     * Allows user to drop items.
     * @param command It is the command that will be used
     */
    private void drop(Command command){
     if(currentItem == null){
            System.out.println("You have nothing to drop");
        }
        else{
            currentRoom.DropItem(currentItem);
            System.out.println("You have dropped " + currentItem.ItemName());
            currentItem = null;
        }
    }
    
    /**
     * Allows user to charge up the beamer.
     * @param command It is the command that will be used
     */
    private void charge(Command command){
        if(currentItem.ItemName().equals("beamer")){
            ((Beamer)currentItem).charge(currentRoom);
        }
        else{
            System.out.println("No beamer");
        }
    }
    
    /**
     * Allows the user the fire the beamer
     * @param command It is the command that will be used
     */
    private void fire(Command command){
        if(currentItem.ItemName().equals("beamer")){
            if(((Beamer)currentItem).isCharged()){
                currentRoom = ((Beamer)currentItem).fire();
            }
            else{
                System.out.println("No charge in the beamer");
            }
        }
        else{
            System.out.println("No beamer");
        }
    }     
}


