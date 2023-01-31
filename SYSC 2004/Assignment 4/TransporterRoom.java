import java.util.Random;

/**
 * Write a description of class TransporterRoom here.
 *
 * @author Tauheed Alamgir 101194927
 * @version 03/19/2022
 */
public class TransporterRoom extends Room
{
    private Random t;
    /**
     * Takes user to a random room
     */
    public TransporterRoom(String description,Random room){
        super("in a transporter room.");
        t = new Random();
        setExit("anywhere", null);
    }

    /**
     *  Overrides previous getExit
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public Room getExit(String direction){
        return findRandomRoom();
    }
    
    /**
     * Finds a random room
     */
    private Room findRandomRoom(){ 
        int RoomNums = Room.GetRooms().size();
        int randomnum = t.nextInt(RoomNums); 
        Room newRoom = Room.GetRooms().get(randomnum);
        return newRoom;
    }
}
