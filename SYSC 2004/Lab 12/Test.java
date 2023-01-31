
/**
 * A class to test adding exceptions and errors to the Money class.
 * 
 * @author Lynn  Marshall
 * @version November 24, 2012
 * 
 * @author Tauheed Alamgir 101194927
 * @version April 12, 2022
 */
public class Test
{
    /**
     * Constructor for testing Money.
     */
    public Test()
    {     
        Money m = new Money(5,0);
        Money m1 = new Money(-3,-1);
        Object o1 = new Money(-745);
        Object o2 = new Object();
        // Test 1
        // All arguments are valid.
        // This should output $2.30
        try {
        System.out.println(m.addMonies(5,95,o1));
        }
        catch (Exception e) {
            System.out.println(e);
        }
    
        
        // Test 2
        // number is invalid (but calculation works)
        // This should output -$2.45
        // After you complete part 1, Money's addMonies
        // method should throw an IllegalArgumentException.
        try {
        System.out.println(m.addMonies(0,95,o1));
        }
        catch (Exception e) {
            System.out.println(e);
        }
        
        // Test 3
        // cents is invalid (but calculation works)
        // This should output $8.05
        // After you complete part 1, Money's addMonies
        // method should throw an IllegalArgumentException.
        try {
        System.out.println(m.addMonies(10,105,o1));
        }
        catch (Exception e) {
            System.out.println(e);
        }
        
        // Test 4
        // obj is null (null pointer runtime exception thrown
        // by Money's plus method)
        // After you complete part 1, Money's addMonies
        // method should throw a NullPointerException.
        try {
        System.out.println(m.addMonies(5,95,null));
        }
        catch (Exception e) {
            System.out.println(e);
        }
        
        // Test 5
        // obj is invalid (class cast runtime exception thrown
        // by the system)
        // After you complete part 1, Money's addMonies
        // method should throw a ClassCastException. 
        try {
        System.out.println(m.addMonies(5,95,o2));
        }
        catch (Exception e) {
            System.out.println(e);
        }
        
        // Test 6
        // All arguments are valid.
        // This should output $1.99
        try {
        System.out.println(m.addMonies(10,0,m1));
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }
}

        
    
