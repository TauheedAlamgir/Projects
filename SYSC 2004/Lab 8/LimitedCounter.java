// Tauheed Alamgir 101194927

public class LimitedCounter extends Counter
{
    /**
     * Creates a counter that has DEFAULT_MINIMUM and DEAFAULT_MAXIMUM
     */
    public LimitedCounter()
    {
        super();
    }
    
    /**
     * Creates a counter that has minCount and maxCount
     */
    public LimitedCounter(int minCount, int maxCount)
    {
        super(minCount, maxCount);
    }
    
    /**
     * Increment this counter by 1.
     */
    public void countUp()
    {
        // If we've reached the maximum count, invoking this
        // method doesn't change the state of the counter.
        if (!super.isAtMaximum()) {
            super.incrementCount();
        }
    }
}
