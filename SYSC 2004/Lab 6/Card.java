// Tauheed Alamgir 101194927

/**
 * A Card is a playing card from an Anglo-American deck of cards.
 * 
 * @author Tauheed Alamgir
 * @version March 1, 2022
 */
public class Card
{
    /** The card's suit: "hearts", "diamonds", "clubs", "spades". */
    private String suit;
    
    /** 
     * The card's rank, between 1 and 13 (1 represents the ace, 11 represents
     * the jack, 12 represents the queen, and 13 represents the king.)
     */
    private int rank;

    /**
     * Constructs a new card with the specified suit and rank.
     */
    public Card(String suit, int rank)
    {
        this.rank = rank;
        this.suit = suit;
    }
    
    /**
     * Returns this card's suit.
     */
    public String suit()
    {
        return this.suit;
    }
    
    /**
     * Returns this card's rank.
     */
    public int rank()
    {
        return this.rank;
    }
    
    /**
     * Determines if this card has the same rank as the specified card.
     * @param Checks if it is the same rank
     * @return if the rank is the same will return true
     */
    public boolean hasSameRank(Card aCard)
    {
        if(this.rank == aCard.rank){
            return true;
        }
        return false;
    }
    
    /**
     * Determines if this card is equal to the specified card.
     * @param Checks if it is the same rank
     * @return if the cards are the same returns true
     */
    public boolean isEqualTo(Card aCard)
    {
        if(this.suit == aCard.suit){
            if(hasSameRank(aCard)){
                return true;
            }
        }
        return false;
    }
}
